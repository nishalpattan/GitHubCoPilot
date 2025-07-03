# starter_app.py
# Run this in terminal: python starter_app.py add "Buy milk"

def main():
    import sys
    args = sys.argv[1:]
    if not args:
        print("Usage: python starter_app.py [add <task> | list | delete <task#>]")
        return
    command, *rest = args
    if command == "add":
        if not rest:
            print("Please provide a task to add.")
        else:
            task = " ".join(rest)
            main.tasks.append(task)
            print(f'Added task: {task}')
    elif command == "list":
        if not main.tasks:
            print("No tasks.")
        else:
            for i, t in enumerate(main.tasks, 1):
                print(f'{i}. {t}')
    elif command == "delete":
        if not rest:
            print("Please provide the task number to delete.")
        else:
            try:
                idx = int(rest[0]) - 1
                if 0 <= idx < len(main.tasks):
                    print(f'Deleted task: {main.tasks.pop(idx)}')
                else:
                    print("Invalid task number.")
            except:
                print("Invalid task number.")
    else:
        print(f'Unknown command: {command}')
main.tasks = []