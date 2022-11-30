
# version 1 (without txt file)

todos = []
while True:
    action = input('Type add, show, edit, complete or exit: ')
    action = action.strip() # if user writes eg add with space and presses enter
    match action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo.capitalize())
            file = open('todos.txt', 'w')
            file.writelines(todos)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item.title()}"
                print(row)
        case 'edit':
            number = int(input('Type nr of todo you want to edit: '))  # int will convert str (default data type in input function) to int
            number = number - 1  # to account that indexing starts from zero and people count from 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo # replace value from todos list with index nr-1 with new to do (instead of append- replace!)
        case 'complete':
            number = int(input('Type nr of todo you want remove as completed: '))
            number = number - 1
            todos.pop(number)
        case 'exit':
            break
        case _: # '_' is an agreed way for dynamic variable that is different from choices program asks for
            print("unknown command")

print("Bye!")

#version 2 with txt file

while True:
    action = input('Type add, show, edit, complete or exit: ')
    action = action.strip() # if user writes eg add with space and presses enter
    match action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"   # \n to create a list in txt file in separate rows
            file = open('txtfiles/Todolist.txt', 'r')        # open txt file in reading mode
            todos = file.readlines()                # create list todos from reading lines in txt file
            file.close()                            # close the file
            todos.append(todo.capitalize())         # append new todo to todos list
            file = open('txtfiles/Todolist.txt', 'w')        # open txt file in writing mode
            file.writelines(todos)                  # REWRITE (!) the txt file from updated todos list
            file.close()                            # close the file
        case 'show' | 'display':                    # show OR display
            file = open('txtfiles/Todolist.txt', 'r')        # open txt file in reading mode
            todos = file.readlines()                # create list todos from reading lines in txt file
            file.close()                            # close the file
            for index, item in enumerate(todos):        #  for index 0-n (int), item 0-n (str) create a list of tuples of nr and item by enumerate
                row = f"{index + 1}-{item.title()}"     # create f string with index n+1 and item from capital letter
                print(row)
        case 'edit':
            number = int(input('Type nr of todo you want to edit: '))        # int will convert str (default data type in input function) to int
            number = number - 1                                              # to account that indexing starts from zero and people count from 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo                                         # replace value from todos list with index nr-1 with new to do (instead of append- replace!)
        case 'complete':
            number = int(input('Type nr of todo you want remove as completed: '))
            number = number - 1
            todos.pop(number)
        case 'exit':
            break
        case _:                                            # '_' is an agreed way for dynamic variable that is different from choices program asks for
            print("unknown command")

print("Bye!")

# v3 with list comprehension

while True:
    action = input('Type add, show, edit, complete or exit: ')
    action = action.strip() # if user writes eg add with space and presses enter
    match action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"   # \n to create a list in txt file in separate rows

            with open('txtfiles/Todolist.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo.capitalize())         # append new todo to todos list

            with open('txtfiles/Todolist.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':                    # show OR display

            with open('txtfiles/Todolist.txt', 'r')

            file = open('txtfiles/Todolist.txt', 'r')        # open txt file in reading mode
            todos = file.readlines()                # create list todos from reading lines in txt file
            file.close()                            # close the file
            viz_todos = [item.strip('\n') for item in todos]  # list comrehension so shorter version of for loop to create new list with items of todo list but remove '\n' with strip function from each item in todos lis
            for index, item in enumerate(viz_todos):        #  for index 0-n (int), item 0-n (str) create a list of tuples of nr and item by enumerate
                row = f"{index + 1}-{item.title()}"     # create f string with index n+1 and item from capital letter
                print(row)
        case 'edit':
            number = int(input('Type nr of todo you want to edit: '))        # int will convert str (default data type in input function) to int
            number = number - 1                                              # to account that indexing starts from zero and people count from 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo                                         # replace value from todos list with index nr-1 with new to do (instead of append- replace!)
        case 'complete':
            number = int(input('Type nr of todo you want remove as completed: '))
            number = number - 1
            todos.pop(number)
        case 'exit':
            break
        case _:                                            # '_' is an agreed way for dynamic variable that is different from choices program asks for
            print("unknown command")

print("Bye!")

# with context manager
action = input('Type add, show, edit, complete for each todo or type exit if you want to quit: ') + '\n'
action = action.strip()

while True:
    action = input('Type add, show, edit, complete or exit if you want to quit.'
                   'if you choose "add" type a to do after '
                    'if you choose "edit" or "complete" type a nr from a to do list') + '\n'
    action = action.strip() # if user writes eg add with space and presses enter

    if action.startswith('add'):
        todo = action[4:]       # LIST SLICING to extract a to do from input string from 4th index (add ) is 0,1,2,3
        with open('txtfiles/Todolist.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo.capitalize() +'\n')         # append new todo to todos list

        with open('txtfiles/Todolist.txt', 'w') as file:
            file.writelines(todos)

    elif action.startswith('show'):
        with open('txtfiles/Todolist.txt', 'r') as file:
            todos = file.readlines()

        viz_todos = [item.strip('\n') for item in todos]  # list comrehension so shorter version of for loop to create new list with items of todo list but remove '\n' with strip function from each item in todos lis
        for index, item in enumerate(viz_todos):        #  for index 0-n (int), item 0-n (str) create a list of tuples of nr and item by enumerate
            row = f"{index + 1}-{item.title()}"     # create f string with index n+1 and item from capital letter
            print(row)
    elif action.startswith('edit'):
        try:
            number = int(action[5:])        # int will convert str (default data type in input function) to int
            number = number - 1                                              # to account that indexing starts from zero and people count from 1

            with open('txtfiles/Todolist.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'                                      # replace value from todos list with index nr-1 with new to do (instead of append- replace!)

            with open('txtfiles/Todolist.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif action.startswith('complete'):
        try:
            number = int(action[9:])

            with open('txtfiles/Todolist.txt', 'r') as file:
                todos = file.readlines()
            todos_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            with open('txtfiles/Todolist.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo: {todos_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif action.startswith('exit'):
        break
    else:                                           # '_' is an agreed way for dynamic variable that is different from choices program asks for
        print("unknown command")

print("Bye!")


#with custom functions to limit redunduncy of the code

# def get_todos():
 #   with open('txtfiles/Todolist.txt', 'r') as file_local: with hard coded pathfile
def get_todos(filepath):
    with open(filepath, 'r') as file_local:     #with filepath as parameter of the function
        todos_local = file_local.readlines() #local variable
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:     #with filepath as parameter of the function
        file_local.writelines(todos_arg) #local variable
   # here no need for RETURN since we do not need any value from thi function, it just modifies the file


while True:
    action = input('Type add, show, edit, complete or exit if you want to quit.'
                   'if you choose "add" type a to do after '
                    'if you choose "edit" or "complete" type a nr from a to do list') + '\n'
    action = action.strip() # if user writes eg add with space and presses enter

    if action.startswith('add'):
        todo = action[4:]       # LIST SLICING to extract a to do from input string from 4th index (add ) is 0,1,2,3
        todos = get_todos("txtfiles/Todolist.txt")  #global variable; argument of the function

        todos.append(todo.capitalize() +'\n')         # append new todo to todos list

        write_todos("txtfiles/Todolist.txt", todos) #function with 2 arguments matching the parameters od the function

    elif action.startswith('show'):
        todos = get_todos("txtfiles/Todolist.txt")

        viz_todos = [item.strip('\n') for item in todos]  # list comrehension so shorter version of for loop to create new list with items of todo list but remove '\n' with strip function from each item in todos lis
        for index, item in enumerate(viz_todos):        #  for index 0-n (int), item 0-n (str) create a list of tuples of nr and item by enumerate
            row = f"{index + 1}-{item.title()}"     # create f string with index n+1 and item from capital letter
            print(row)
    elif action.startswith('edit'):
        try:
            number = int(action[5:])        # int will convert str (default data type in input function) to int
            number = number - 1                                              # to account that indexing starts from zero and people count from 1

            todos = get_todos("txtfiles/Todolist.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'                                      # replace value from todos list with index nr-1 with new to do (instead of append- replace!)

            write_todos("txtfiles/Todolist.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif action.startswith('complete'):
        try:
            number = int(action[9:])

            todos = get_todos("txtfiles/Todolist.txt")
            todos_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            write_todos("txtfiles/Todolist.txt", todos)

            message = f"Todo: {todos_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif action.startswith('exit'):
        break
    else:                                           # '_' is an agreed way for dynamic variable that is different from choices program asks for
        print("unknown command")

print("Bye!")


