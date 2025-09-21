# commands/system.py

import psutil
import datetime

def cpu(args):
    """Displays CPU usage and information."""
    print("--- CPU Usage ---")
    usage = psutil.cpu_percent(interval=1)
    print(f"Usage: {usage}%")
    
    cores_physical = psutil.cpu_count(logical=False)
    cores_total = psutil.cpu_count(logical=True)
    print(f"Physical Cores: {cores_physical}")
    print(f"Total Cores (including logical): {cores_total}")

def mem(args):
    """Displays memory information."""
    print("--- Memory Usage ---")
    memory = psutil.virtual_memory()
    
    def to_gb(bytes_val):
        return round(bytes_val / (1024**3), 2)

    print(f"Total: {to_gb(memory.total)} GB")
    print(f"Available: {to_gb(memory.available)} GB")
    print(f"Used: {to_gb(memory.used)} GB")
    print(f"Percentage: {memory.percent}%")

def ps(args):
    """Lists running processes."""
    print("--- Running Processes ---")
    print(f"{'PID':<10} {'User':<15} {'Name'}")
    print("-" * 40)

    for i, proc in enumerate(psutil.process_iter(['pid', 'name', 'username'])):
        if i > 20: # Limit to the first 20 processes for brevity
            break
        try:
            pid = proc.info['pid']
            user = proc.info['username'] or 'N/A'
            name = proc.info['name']
            
            if len(user) > 13: user = user[:10] + '...'
            if len(name) > 30: name = name[:27] + '...'

            print(f"{pid:<10} {user:<15} {name}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass