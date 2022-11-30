
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