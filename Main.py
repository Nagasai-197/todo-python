import json

def ShowMenu():
    print("\nMenu:\n1. Add Task\n2. View Tasks\n3. Mark Task as Complete\n4. Update Task\n5. Delete Task\n6. View Tasks by Priority\n7. Exit")
    print("Please select an option:")
#adding Task
def addTask(task):
    taskName = input("Enter the task name: ")
    if taskName.strip() == "":
        print("Task name cannot be empty. Please enter a valid name.")
        return
    if taskName in task:
        print("Task already exists. Please choose a different name.")
        return
    taskPriority = input("Enter the task priority (High/Medium/Low): ")
    if taskPriority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")
        return
    task[taskName] = {"status": "Incomplete", "priority": taskPriority}
    print("Task added successfully.")
    saveTasks(task)

#displaying Task
def displayTasks(task):
    print(f"\nTasks count: {len(task)}")
    if not task:
        print("No tasks available.")
    else:
        i=1
        for taskName, status in task.items():
            print(i,"Task Name:", taskName)
            print(f"   Status: {status['status']}")
            print(f"   Priority: {status['priority']}")
            i += 1
    

#marking Task as complete
def markTaskComplete(task):    
    taskName = input("Enter the task name to mark as complete: ")
    if taskName in task:
        task[taskName]["status"] = "Complete"
        saveTasks(task)
        print("Task marked as complete.")
    else:        
        print("Task not found.")


#updating Task
def updateTask(task):
    taskName = input("Enter the task name to update: ")
    if taskName in task:
        print("\nWhat do you want to update?\n1. Task Name\n2. Task Priority")
        choice = input("Enter your choice: ")
        if choice == "1":
            newTaskName = input("Enter the new task name: ")
            if newTaskName.strip() == "":
                print("Task name cannot be empty. Please enter a valid name.")
                return
            if newTaskName not in task:
                task[newTaskName] = task.pop(taskName)
                saveTasks(task)
                print("Task name updated successfully.")
            else:
                print("Task name already exists.")
        elif choice == "2":
            newPriority = input("Enter the new priority (High/Medium/Low): ")
            if newPriority in ["High", "Medium", "Low"]:
                task[taskName]["priority"] = newPriority
                saveTasks(task)
                print("Task priority updated successfully.")
            else:
                print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")
    else:
        print("Task not found.")

#deleting Task
def deleteTask(task):
    taskName = input("Enter the task name to delete: ")
    if taskName in task:
        del task[taskName]
        saveTasks(task)
        print("Task deleted successfully.")
    else:
        print("Task not found.")

#viewing tasks by priority
def viewTasksByPriority(task):
    priority = input("Enter the priority to filter by (High/Medium/Low): ")
    if priority in ["High", "Medium", "Low"]:
        filteredTasks = {name: details for name, details in task.items() if details["priority"] == priority}
        if filteredTasks:
            print(f"\nTasks with {priority} priority:")
            i=1
            for taskName, status in filteredTasks.items():
                print(i,"Task Name:", taskName)
                print(f"   Status: {status['status']}")
                print(f"   Priority: {status['priority']}")
                i += 1
        else:
            print(f"No tasks with {priority} priority found.")
    else:
        print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")

#saving tasks to a file
def saveTasks(task):
    with open("tasks.json", "w") as f:
        json.dump(task, f,indent=4)

#loading tasks from a file
def loadTasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

task = loadTasks()
ShowMenu()
option = input()
while option != "7":
    if option == "1":
        print("Adding a new task...")
        # Code to add a task goes here
        addTask(task)
    elif option == "2":
        print("Viewing tasks...")
        # Code to view tasks goes here
        displayTasks(task)
    elif option == "3":
        print("Marking a task as complete...")
        # Code to mark a task as complete goes here
        markTaskComplete(task)
    elif option == "4":
        print("Updating a task...")
        # Code to update a task goes here
        updateTask(task)
    elif option == "5":
        print("Deleting a task...")
        # Code to delete a task goes here
        deleteTask(task)
    elif option == "6":
        print("Viewing tasks by priority...")
        # Code to view tasks by priority goes here
        viewTasksByPriority(task)
    elif option == "7":
        break
    else:
        print("Invalid option. Please try again.")

    ShowMenu()
    option = input()
print("Exiting the program. Goodbye!")
