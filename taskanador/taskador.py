

import argparse

from task_list import TaskList
from task import Task

tl = TaskList()

def list_tasks(args):
    # If status argument is provided, use it; otherwise list all tasks
    if args.status:
        tl.list(args.status)
    else:
        tl.list()

def add_task(args):
    tl.add_task(args.task_description) 

def remove_task(args):
    tl.remove_task(args.id)
    
def done(args):
    tl.complete_task(args.id)

def main():

    parser = argparse.ArgumentParser( description="Simple todo CLI app" )
    subparsers = parser.add_subparsers(dest="command",help="Available commands")
    subparsers.required = True

    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("status", type=str, nargs='?', default=None, 
                            choices=['done', 'pending'],
                            help="Filter the results by 'done' or 'pending' (optional)")
    list_parser.set_defaults(func=list_tasks)

    add_parser = subparsers.add_parser( "add", help="Add a new task")
    add_parser.add_argument("task_description",type=str, help="Text describing the task")
    add_parser.set_defaults(func=add_task)

    remove_parser = subparsers.add_parser("delete",help="Delete a task")
    remove_parser.add_argument("id",type=int,help="ID of the task to be deleted")
    remove_parser.set_defaults(func=remove_task)

    done_parser = subparsers.add_parser("done",help="Task is done")
    done_parser.add_argument("id",type=int,help="ID of the task done")
    done_parser.set_defaults(func=done)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()