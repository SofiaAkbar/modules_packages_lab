def user_input_main():
    option = input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ")
    return option

def user_input_description():
    option = input()
    return option

def user_input_time():
    option = int(input())
    return option

def new_task_list():
    option = input('Would you like a new task list? ').lower()
    return option