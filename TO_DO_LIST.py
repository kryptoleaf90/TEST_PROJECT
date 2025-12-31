task={}

def add_task():
    index=input("TASK NO:")
    while index in task:
        index=input("ENTER VALID INDEX:")
    new_task=input("ENTER TASK:")
    task[index]=new_task
    print("TASK ADDED!!")

def remove_task():
    remove_index=input("ENTER INDEX TO REMOVE:")
    if remove_index in task:
        del task[remove_index]
        print("TASK REMOVED")
    else :
        print("WRONG INDEX")

def show_tasks():
    for key,value in task.items():
        print(f"TASK {key:01}: {value}")


def main():
    is_running = True
    print("*******************")
    print("MY TO TO-DO LIST")
    print("*******************")
    while is_running:
        print("*******************")
        print("PRESS '1' TO SEE TASKS")
        print("PRESS '2' TO ADD A TASK")
        print("PRESS '3' TO MARK TASK DONE")
        print("PRESS Q/q to quit")
        print("*******************")
        choice = input("YOUR CHOICE:").lower()
        while choice != '1' and choice != '2' and choice != '3':
            choice = input("ENTER VALID CHOICE:")
        if choice =="1":
            show_tasks()
        if choice == "2":
            add_task()
        if choice== "3":
            remove_task()
        if choice=="q":
            is_running=False





main()