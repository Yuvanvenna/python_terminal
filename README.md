# Python Command Terminal

This project is a fully-functioning command terminal built in Python, created as a submission for the **CodeMate Hackathon**. It mimics the behavior of a real system terminal, supporting file system navigation, operations, and system resource monitoring.

## Features

This terminal supports a variety of commands, covering all the mandatory requirements of the hackathon project.

#### 📂 File & Directory Operations
- `ls [path]`: Lists files and directories in the specified path or current directory.
- `cd [path]`: Changes the current working directory. Supports `..` for parent and `~` for home.
- `pwd`: Prints the current working directory path.
- `mkdir <dirname>`: Creates a new directory.
- `rm <filename>`: Removes a file (with a safety check to prevent removing directories).
- `touch <filename>`: Creates a new empty file.

#### ⚙️ System Monitoring
- `cpu`: Displays current CPU usage percentage and core count.
- `mem`: Shows system memory usage (Total, Used, Available in GB).
- `ps`: Lists the currently running processes.

#### ✨ Enhancements
- **Command History**: Use the Up and Down arrow keys to navigate through previous commands.
- **Auto-Completion**: Press the Tab key to auto-complete file and directory names.
- **Dynamic Prompt**: The command prompt always shows the current working directory.

## Tech Stack

- **Language**: Python 3
- **Core Libraries**:
  - `psutil`: For fetching system monitoring information.
  - `prompt-toolkit`: For advanced command history and auto-completion.

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone <your-github-repo-url>
   cd <your-repo-name>
