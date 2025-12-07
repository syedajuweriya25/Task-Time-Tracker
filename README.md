# Task-Time-Tracker
### Description:
#### One-Line:<br/> A productivity tracker that logs tasks and times and **shows where your hours go**.

#### Project Summary: <br/>A command line task-time tracker that helps user log tasks, track time spent,and realise where their hours go along with data permanently stored in csv file till the user dosen't want to remove the csv file.


#### Overview:
#### It creates a CSV file named 'task_list.csv' if it isn't already existing.
#### The features present in the project:
+ The user can add any number of tasks and for each task automatically start time is logged
+ Whenever user marks a task as complete the end time and duration is automatically logged and status value is changed to complete
+ The user can view task status the is out total, number of pending tasks
+ The user can generate the productivity report which is clean and readable even for non-programmers
+ The user can remove the task list when desired after completion of all the tasks

<!-- listing library used-->
#### Libraries used are:
1. os
2. re
3. sys
4. csv
5. datetime
6. tabulate (pip install tabulate)

<!-- listing functions defined-->
#### Excluding main 11 functions are defined
1. is_task_list
2. s_options
3. no_options
4. directs
5. open_list
6. add_task
7. mark_task
8. durations
9. task_status
10. productivity_report
11. remove_list

<!-- describing the role of main function-->
#### Main Function: It calls out 'is_task_list' function along with conditionals and file name. If it returns true it directs to 's_options' function if false it directs to 'no_options' and form both to eventually 'directs' function.

### Why particular choice over others? :
<!-- why I used sys library-->
#### In 'directs' function in some places, in 'add_task' function and in 'mark_task' function we use 'sys' library to exit to be user friendly and harsh to the user. Based on the requirements in some places an exit message is also provided

<!-- why use regex concept and not any other-->
#### In 'directs' function we use 're' library and the concept of regex to evaluate the user input to direct to correct function.Regex concept is used to evaluate user input to be user friendly and also to increase the effectiveness of the program by avoiding usage

<!-- why I raised a vaue error-->
#### In 'directs' function we raised 'ValueError' along with an error message if the input provided by user doesn't even match the specified requirement.

<!--why did I use datetime instead of date-->
#### The 'datetime' class is used instead of 'date' class to ensure that duration calculation is precise even if the user completes the task the next day

<!-- why did I use csv file to store the data-->
#### The data provided by the user that is task name and the program collected data such as datetime values and duration of task are stored in csv file so as to provide user friendly experience; as the user will have the ability to mark the task as complete, add more tasks and many more possibilities as the data stored in **csv file** will eventually persist information between sessions and are exportable for analysis.

<!-- why did I use tabulate library-->
#### 'tabulate' library is used instead of directly printing csv file as the csv is a bit hard to read for a user with bare minimum knowledge about programming. Using the library creates clean readable tables that provides understandable task insights at a glance

### TODO :
#### 1. Before running the function run in terminal window to change directory<br/>**cd task_time_tracker**
#### 2. Then run in your terminal<br/> **python tracker.py**

#### 1. Before running the function run in terminal window to change directory<br/>**cd project**
#### 2. Then run in your terminal<br/> **python project.py**
