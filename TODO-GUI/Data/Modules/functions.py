FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):

    """Read the text file and return the list of to-do items"""

    with open(filepath, 'r') as file:  # Fixed the filename from 'todo.txt' to 'todos.txt'
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):

    """Write the list of to-do items to the text file"""

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

