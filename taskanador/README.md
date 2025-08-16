# Taskador - CLI Todo App

A simple and elegant command-line todo application built with Python, featuring Object-Oriented Programming principles, comprehensive logging, and persistent data storage.

## Features

- ✅ **Add tasks** with descriptive titles
- 📋 **List tasks** with optional filtering (done/pending/all)
- ✅ **Mark tasks as complete**
- 🗑️ **Delete tasks** by ID
- 💾 **Persistent storage** using JSON
- 📝 **Comprehensive logging** with timestamps
- 🎨 **Pretty table formatting** using tabulate
- 🔧 **Clean CLI interface** with argparse

## Project Structure

```
Final_Project/
├── taskador.py          # Main CLI application entry point
├── task.py              # Task class definition
├── task_list.py         # TaskList class with core functionality
├── logger.py            # Logger class for activity tracking
├── requirements.txt     # Python dependencies
├── data/
│   └── tasks.json      # Persistent task storage
└── logs/
    └── log.txt         # Application logs
```

## Installation

1. **Clone or download** the project files

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Make sure you're in the project directory:**
   ```bash
   cd Final_Project
   ```

## Usage

### Basic Commands

```bash
# Show help
python3 taskador.py --help

# Show help for specific command
python3 taskador.py <command> --help
```

### Adding Tasks

```bash
# Add a new task
python3 taskador.py add "Buy groceries"
python3 taskador.py add "Finish homework"
python3 taskador.py add "Call mom"
```

### Listing Tasks

```bash
# List all tasks
python3 taskador.py list

# List only pending tasks
python3 taskador.py list pending

# List only completed tasks
python3 taskador.py list done
```

### Managing Tasks

```bash
# Mark a task as done (use the task ID)
python3 taskador.py done 1

# Delete a task (use the task ID)
python3 taskador.py delete 2
```

## Example Workflow

```bash
# Add some tasks
$ python3 taskador.py add "Learn Python"
$ python3 taskador.py add "Build a CLI app"
$ python3 taskador.py add "Write documentation"

# List all tasks
$ python3 taskador.py list
 ID  title               Status
----  ------------------  --------
   1  Learn Python        pending
   2  Build a CLI app     pending
   3  Write documentation pending

# Complete a task
$ python3 taskador.py done 1

# List only pending tasks
$ python3 taskador.py list pending
 ID  title               Status
----  ------------------  --------
   2  Build a CLI app     pending
   3  Write documentation pending

# List only completed tasks
$ python3 taskador.py list done
 ID  title         Status
----  ------------  ------
   1  Learn Python  done
```

## Architecture

### Classes

#### `Task`
- Simple data class representing a single task
- Properties: `id`, `title`, `status`
- Methods: `to_dict()` for JSON serialization

#### `TaskList`
- Core business logic for task management
- Handles JSON persistence and file operations
- Methods: `add_task()`, `remove_task()`, `complete_task()`, `list()`
- Integrated logging for all operations

#### `Logger`
- Handles all application logging with timestamps
- Creates log files and directories automatically
- Logs all task operations for audit trail

### Data Storage

- Tasks are stored in `data/tasks.json`
- JSON structure:
  ```json
  {
    "tasks": [
      {
        "id": 1,
        "title": "Sample task",
        "status": "pending"
      }
    ],
    "count": 1
  }
  ```

### Logging

- All operations are logged to `logs/log.txt`
- Log format: `YYYY-MM-DD [ HH:MM:SS ] => Operation details`
- Tracks successful operations and errors

## Dependencies

- **tabulate** - For pretty table formatting in the terminal
- **python-dotenv** - For environment variable management (if needed)

## Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `add <title>` | Add a new task | `python3 taskador.py add "New task"` |
| `list [status]` | List tasks (all/done/pending) | `python3 taskador.py list pending` |
| `done <id>` | Mark task as complete | `python3 taskador.py done 1` |
| `delete <id>` | Delete a task | `python3 taskador.py delete 2` |

## Development Features

- **OOP Design**: Clean separation of concerns with dedicated classes
- **Error Handling**: Robust error handling with user feedback
- **Validation**: Input validation through argparse choices
- **Extensibility**: Easy to add new commands and features
- **Logging**: Comprehensive activity tracking
- **Data Persistence**: Automatic file and directory creation

## Contributing

This is a learning project demonstrating:
- Object-Oriented Programming in Python
- Command-line interface design with argparse
- File I/O and JSON data persistence
- Logging and error handling
- Clean code architecture

Feel free to fork, modify, and extend this project for your own learning!

## License

This project is for educational purposes. Feel free to use and modify as needed.ct