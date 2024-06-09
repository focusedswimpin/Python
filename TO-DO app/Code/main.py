# Creating a new list.

# Enumerate = allows you to iterate through a sequence and keep track of the index of each element.
# This function can be useful if you need to access the index of each element in the sequence

todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    if user_action == "add":
        todo = input("Enter a todo: ") + "\n"

        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()
        except FileNotFoundError:
            todos = []

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action == "show":
        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()
        except FileNotFoundError:
            todos = []

        if todos:
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.strip()}")
        else:
            print("No todos to show.")

    elif user_action == "edit":
        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()
        except FileNotFoundError:
            todos = []

        if todos:
            try:
                number = int(input("Enter the number of the to-do to edit: ")) - 1
                if 0 <= number < len(todos):
                    new_todo = input("Enter a new todo: ") + "\n"
                    todos[number] = new_todo
                    with open("todos.txt", "w") as file:
                        file.writelines(todos)
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No todos to edit.")

    elif user_action == "complete":
        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()
        except FileNotFoundError:
            todos = []

        if todos:
            try:
                number = int(input("Enter the number of the to-do to complete: ")) - 1
                if 0 <= number < len(todos):
                    removed_item = todos.pop(number)
                    with open("todos.txt", "w") as file:
                        file.writelines(todos)
                    print(f"Removed: {removed_item.strip()}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No todos to complete.")

    elif user_action == "exit":
        break

    else:
        print("Invalid command. Please enter add, show, edit, complete, or exit.")

print("Bye!")


#
# Enumerate = allows you to iterate through a sequence and keep track of the index of each element.
# This function can be useful if you need to access the index of each element in the sequence

