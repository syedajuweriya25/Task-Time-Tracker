import os
import re
import sys
import csv
from datetime import datetime
from tabulate import tabulate


# defining main function
def main():
    task_list = 'task_list.csv'
    if is_task_list(task_list):
        directs(s_options())
    else:
        directs(no_options())

# checking if task-list exists or not
def is_task_list(task_list):
    return os.path.isfile(task_list)

# displaying options if task-list present
def s_options():
    print('\nInput serial number of the option you want to choose')
    options = ['1. Add task', '2. Mark task completion', '3. Status of tasks', '4. Productivity report']
    for option in options:
        print(option)
    return input('\nChoice: ')

# displaying options if task-list absent
def no_options():
    print('Do you want to open a task list? ')
    options = ['Yes', 'No']
    for option in options:
        print(option)
    return input('\nAnswer: ').lower()

# directs to particular function based on choosen option
def directs(string):
    # (whitespace may or not, a digit, period may or not, txt may or may not)
    if value := re.search(r"^ *(\d)\.*.*$", string):
        direct = int(value.group(1))
        if direct == 1:
            add_task()
        elif direct == 2:
            mark_task()
        elif direct == 3:
            task_status()
        elif direct == 4:
            productivity_report()
        else:
            sys.exit('Option not present')

    elif value := re.search(r"^ *(yes|no) *$", string):
        direct = value.group()
        if direct == 'yes':
            open_list()
        else:
            sys.exit()
    else:
        raise ValueError('Selected option invalid')

# opening csv task-list file
def open_list():
    with open('task_list.csv', 'w') as tasks:
        task = csv.DictWriter(tasks, fieldnames=['task_name', 'start_time', 'end_time', 'duration', 'status'])
        task.writeheader()
    add_task()

# adding tasks and notes start time of task
def add_task():
    try:
        n = int(input('How many task you want to add? '))
    except ValueError:
        sys.exit('Not an integer. Run the function again')
    with open('task_list.csv', 'a') as tasks:
        task = csv.DictWriter(tasks, fieldnames=['task_name', 'start_time', 'end_time', 'duration', 'status'])
        for _ in range(n):
            task_name = input('Task name: ').lower().strip()
            start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            task.writerow({'task_name':task_name, 'start_time':start_time, 'end_time':' ', 'duration':' ', 'status':'Incomplete'})
        print('\nTask added')

# marking task completion and noting time
def mark_task():
    task_list = []
    print('\nEnter name of the task you completed')
    task_name = input('Task: ').lower().strip()
    # adding dicts present in csv to a list to alter some keys values
    with open('task_list.csv', 'r') as tasks:
        task = csv.DictReader(tasks)
        for rows in task:
            task_list.append(rows)
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # altering key values
    found = False
    for row in task_list:
        if row['task_name'] == task_name and row['status'] == 'Incomplete':
            row['end_time'] = end_time
            row['status'] = 'complete'
            found = True
    if found == False:
        sys.exit('Task not available or Task completed')
    # rewriting csv file using altered list
    with open('task_list.csv', 'w') as new_tasks:
        new_task = csv.DictWriter(new_tasks, fieldnames=['task_name', 'start_time', 'end_time', 'duration', 'status'])
        new_task.writeheader()
        new_task.writerows(task_list)
    print('\nTask marked completed')
    durations(task_name)

# calulating duration of each task after completion
def durations(task_name):
    task_list = []
    # csv dicts append to a list then rewriting csv after alteration
    with open('task_list.csv') as tasks:
        task = csv.DictReader(tasks)
        for rows in task:
            task_list.append(rows)
    for row in task_list:
        if row['task_name'] == task_name and row['status'] == 'complete':
            start_time = datetime.strptime(row['start_time'], '%Y-%m-%d %H:%M:%S')
            end_time = datetime.strptime(row['end_time'], '%Y-%m-%d %H:%M:%S')
            duration = end_time - start_time
            row['duration'] = duration
    with open('task_list.csv', 'w') as new_tasks:
        new_task = csv.DictWriter(new_tasks, fieldnames=['task_name', 'start_time', 'end_time', 'duration', 'status'])
        new_task.writeheader()
        new_task.writerows(task_list)


# checking the status of task completion
def task_status():
    incomplete = []
    with open('task_list.csv') as tasks:
        task = csv.DictReader(tasks)
        for rows in task:
            if rows['status'] == 'Incomplete':
                incomplete.append(rows['task_name'])
        remaining = len(incomplete)
    with open('task_list.csv') as tasks:
        task = csv.reader(tasks)
        total = int(len(list(task))) - 1
    if remaining == 0:
        print('\nCongratulations! You completed all your tasks')
        # asking the user if he wants to remove csv file
        answer = input('Do you want to remove Task list? (yes/no) \n').lower().strip()
        if answer == 'yes':
            task_list = 'task_list.csv'
            remove_list(task_list)
        elif answer == 'no':
            print('Okay')
        else:
            sys.exit('Run again as input invalid')
    elif remaining == 1:
        print(f'Out of {total}, {remaining} task is pending')
    else:
        print(f'Out of {total}, {remaining} tasks are pending')

# displaying the productivity report that is tasks status along with duration taken to complete
def productivity_report():
    table = []
    with open('task_list.csv', 'r') as tasks:
        task = csv.DictReader(tasks)
        print(tabulate(task, "keys", "pretty"))

# removing task_list if user wants
def remove_list(task_list):
    print('Task list sucessfully removed')
    os.remove(task_list)

if __name__ == "__main__":
    main()
