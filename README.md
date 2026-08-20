# To-Do List App

A simple desktop to-do list app built with Python's built-in `tkinter` GUI library.

## Features
- Add tasks to a running list via a text entry box with placeholder text
- Delete a selected task from the list
- Clean, minimal green-themed interface

## How it works
- The entry field uses a `StringVar` to bridge the on-screen box with the task text, and shows/hides placeholder text on focus in/out.
- Tasks are stored and displayed using a `Listbox` widget.
- Adding and deleting are wired to buttons via `command=` callbacks.

## Requirements
- Python 3.x
- `tkinter` (included with most standard Python installations)

## Run it
```bash
python todo_app.py
```

## Possible next steps
- Persist tasks to a file or database so they survive closing the app
- Add task editing
- Add due dates / priority levels
