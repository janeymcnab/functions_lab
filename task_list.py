tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]



def print_uncompleted_tasks(list):
    uncompleted_tasks = []

    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)

    
    print(uncompleted_tasks)

# print_uncompleted_tasks(tasks)

def print_completed_tasks(list):
    completed_tasks = []

    for task in list:
        if task["completed"] == True:
            completed_tasks.append(task)
    
    print(completed_tasks)

# print_completed_tasks(tasks)

def print_all_descriptions(list):
    for task in list:
        print(task["description"])
    
# print_all_descriptions(tasks)
    


def given_time_taken(list, time):
    time_taken = []

    for task in list:
        if task["time_taken"] > time:
            time_taken.append(task)
    print(time_taken)

# given_time_taken(tasks, 20)

def print_given_description(list, description):
    
    for task in list:
        if task["description"] == description:
            print(task)

print_given_description(tasks, 'Wash Dishes')

   

def update_a_task(list):
    task_name = input("Enter task name here: ")

    if task_name == tasks["descriptions"]:
        tasks["completed"] = True
        print()











