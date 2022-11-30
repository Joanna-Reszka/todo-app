# good practice save functions in separate file
def get_todos(filepath = "txtfiles/Todolist.txt"):
    """ Read the txt file and return list of to-do items""" #DOCSTRINGS
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath = "txtfiles/Todolist.txt"):
    """ Write the to- do items in the txt file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


