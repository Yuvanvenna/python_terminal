# commands/file_ops.py

import os

def ls(args):
    """Lists files and directories."""
    try:
        path = args[0] if args else '.'
        items = os.listdir(path)
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory")
    except Exception as e:
        print(f"Error: {e}")

def mkdir(args):
    """Creates a new directory."""
    if len(args) != 1:
        print("Usage: mkdir <directory_name>")
        return
    dir_name = args[0]
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created.")
    except FileExistsError:
        print(f"mkdir: cannot create directory '{dir_name}': File exists")
    except Exception as e:
        print(f"Error: {e}")

def touch(args):
    """Creates an empty file."""
    if len(args) != 1:
        print("Usage: touch <filename>")
        return
    filename = args[0]
    try:
        with open(filename, 'a'):
            os.utime(filename, None)
        print(f"File '{filename}' created.")
    except Exception as e:
        print(f"Error: {e}")

def rm(args):
    """Removes a file."""
    if len(args) != 1:
        print("Usage: rm <filename>")
        return
    
    path = args[0]
    try:
        if os.path.isdir(path):
            print(f"rm: cannot remove '{path}': Is a directory")
            return
        os.remove(path)
        print(f"File '{path}' removed.")
    except FileNotFoundError:
        print(f"rm: cannot remove '{path}': No such file or directory")
    except Exception as e:
        print(f"Error: {e}")