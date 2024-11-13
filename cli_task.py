import  argparse
from task_manager import TaskManager

task_manager = TaskManager('tasks.json')


def main():
    parser = argparse.ArgumentParser(prog='cli_task', description='Task Tracker CLI')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    list_parser = subparsers.add_parser('list', help='List the tasks')
    list_parser.add_argument('--status', choices=["to-do", "in-progress", "done"], help='Filter the tasks by status')

    update_parser = subparsers.add_parser('update', help='Update task')
    update_parser.add_argument('id', type=int, help='ID of the task')
    update_parser.add_argument('--description', type=str, help='Updates the description of task')
    update_parser.add_argument('--status', choices=["to-do", "in-progress", "done"], help='Updates the status of task')

    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='ID of the task you want to delete')

    args = parser.parse_args()
    if args.command == "add":
        task_manager.add_task(args.description)
    elif args.command == "list":
        task_manager.list_tasks(args.status)
    elif args.command == "update":
        task_manager.update_task(args.id, args.description, args.status)
    elif args.command == "delete":
        task_manager.delete_task(args.id)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()