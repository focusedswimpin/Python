# There are two ways to import functions and since this program has less functions we used the simpler import method.
# The main drawback of that is we then need to rename all the other functions to functions.____

# Below is the link for the python date time format codes.
# https://www.w3schools.com/python/gloss_python_date_format_codes.asp


from Modules.functions import get_todos, write_todos
from time import strftime

print(f"It is {strftime('%b %d, %Y %H:%M:%S')}")

while True:
    userInput = input('Type add, show, edit, complete, or exit: ').strip()

    if userInput.startswith('add'):
        todo = userInput[4:]

        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)

    elif userInput.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif userInput.startswith('edit'):
        try:
            userInputIndex = int(userInput[5:]) - 1  # Adjusted to 0-based index
            todos = get_todos()

            if 0 <= userInputIndex < len(todos):
                newTodo = input('Type new todo: ')
                todos[userInputIndex] = newTodo + '\n'
                write_todos(todos)
            else:
                print('Out of range')

        except ValueError:
            print('Your command is not valid.')
        except IndexError:
            print('There is no item with that number.')

    elif userInput.startswith('complete'):
        try:
            userInputIndex = int(userInput[9:]) - 1  # Adjusted to 0-based index
            todos = get_todos()

            if 0 <= userInputIndex < len(todos):
                completedTodo = todos.pop(userInputIndex).strip('\n')
                print(f'Todo {completedTodo} was removed from the list.')
                write_todos(todos)
            else:
                print('Out of range')

        except ValueError:
            print('Your command is not valid.')
        except IndexError:
            print('There is no item with that number.')

    elif userInput.startswith('exit'):
        break
    else:
        print('Invalid command.')

print('Bye!')

