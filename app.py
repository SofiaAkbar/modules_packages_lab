from modules.task_list import * 
from modules.output import *
from data.task_list import *
from modules.input import *

# new list or old one
list_of_tasks = new_task(tasks)

while (True):
    print_menu()
    option = user_input_main()

    if (option.lower() == 'q'):
        break
    
    if option == '1':
        print_list(list_of_tasks)
    
    elif option == '2':
        print_list(get_uncompleted_tasks(list_of_tasks))
    
    elif option == '3':
        print_list(get_completed_tasks(list_of_tasks))
    
    elif option == '4':
        print("Enter task description to search for: ")
        description = user_input_description()
        task = get_task_with_description(list_of_tasks, description)
        if task != "Task Not Found":
            mark_task_complete(task)
    
    elif option == '5':
        print("Enter task duration: ")
        time = user_input_time()
        print_list(get_tasks_taking_longer_than(list_of_tasks, time))
    
    elif option == '6':
        print("Enter task description to search for: ")
        description = user_input_description() 
        print(get_task_with_description(list_of_tasks, description))
    
    elif option == '7':
        print("Enter description: ")
        description = user_input_description()
        print("Enter time taken: ")
        time_taken = user_input_time()
        task = create_task(description, time_taken)
        tasks.append(task)
    
    else:
        print("Invalid Input - choose another option")
