# main.py

import os
# Import the command functions
from commands.navigation import pwd, cd
from commands.file_ops import ls, mkdir, touch, rm
from commands.system import cpu, mem, ps

# Create a dictionary to map command strings to functions
COMMANDS = {
    "pwd": pwd,
    "ls": ls,
    "cd": cd,
    "mkdir": mkdir,
    "touch": touch,
    "rm": rm,
    "cpu": cpu,
    "mem": mem,
    "ps": ps,
}

def main():
    """The main loop for our command terminal."""
    while True:
        try:
            current_dir = os.getcwd()
            # We are back to using the simple, built-in input() function
            command_input = input(f"{current_dir} mate-shell > ").strip()

            if not command_input:
                continue

            parts = command_input.split()
            command = parts[0].lower()
            args = parts[1:]

            if command == "exit":
                print("Exiting Mate.AI Shell...")
                break

            if command in COMMANDS:
                command_function = COMMANDS[command]
                command_function(args)
            else:
                print(f"Command '{command}' not found.")
        except KeyboardInterrupt:
            # Handle Ctrl+C by printing a newline
            print()
            continue
        except EOFError:
            # Handle Ctrl+D to exit
            print("Exiting Mate.AI Shell...")
            break


if __name__ == "__main__":
    print("Welcome to Mate.AI Shell! Type 'exit' to quit.")
    main()