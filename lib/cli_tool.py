import argparse
from lib.models import Task, User

# in-memory user store for this process
users = {}

def add_task(args):
    # get or create user
    user = users.get(args.user)
    if not user:
        user = User(args.user)
        users[args.user] = user

    # add the task
    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return

    task = user.get_task_by_title(args.title)
    if not task:
        print("❌ Task not found.")
        return

    task.complete()

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # add-task
    add_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_parser.add_argument("user", help="User's name")
    add_parser.add_argument("title", help="Task title")
    add_parser.set_defaults(func=add_task)

    # complete-task
    complete_parser = subparsers.add_parser("complete-task", help="Complete a task")
    complete_parser.add_argument("user", help="User's name")
    complete_parser.add_argument("title", help="Task title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()