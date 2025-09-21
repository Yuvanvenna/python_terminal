# commands/navigation.py

import os

def pwd(args):
    """
    Prints the current working directory.
    Ignores any arguments
    """
    if args:
        print("pwd: command takes no arguments")
        return
    try:
        current_directory = os.getcwd()
        print(current_directory)
    except OSError as e:
        print(f"Error: {e}")

# cd command
def cd(args):
    """
    Changes the current working directory.
    Usage: cd [path]
    """
    try:
        # If no path is given, change to the user's home directory
        if not args:
            path = os.path.expanduser('~')
        elif len(args) > 1:
            print("cd: too many arguments")
            return
        else:
            path = args[0]
        
        os.chdir(path)

    except FileNotFoundError:
        print(f"cd: no such file or directory: {path}")
    except Exception as e:
        print(f"Error: {e}")