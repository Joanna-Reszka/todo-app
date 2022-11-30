from functions import get_todos, write_todos
import time

# if mor funnctions better import function and everywhere where function
# is required eg todos = get_todos() should instead be:
#               todos = functions.get_todos()
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    action = input('Type add, show, edit, complete or exit if you want to quit.'
                   'if you choose "add" type a to do after '
                    'if you choose "edit" or "complete" type a nr from a to do list') + '\n'
    action = action.strip()

    if action.startswith('add'):
        todo = action[4:]
        todos = get_todos()

        todos.append(todo.capitalize() +'\n')

        write_todos(todos)

    elif action.startswith('show'):
        todos = get_todos()

        viz_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(viz_todos):
            row = f"{index + 1}-{item.title()}"
            print(row)
    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif action.startswith('complete'):
        try:
            number = int(action[9:])

            todos = get_todos()
            todos_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            write_todos(todos)

            message = f"Todo: {todos_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif action.startswith('exit'):
        break
    else:
        print("unknown command")

print("Bye!")


