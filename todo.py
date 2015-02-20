__author__ = 'rebeccashen'

def create_todo(todos, title, description, level):
    todo = {
        'title' : title,
        'description' : description,
        'level' : level,
    }

def show_todos(todos):
    output = ("Item Title       Description     Level\n")
    for index, todo in enumerate(todos):
        line = str(index + 1).ljust(8)
        for key,length in [('title', 16),
            ('description', 24),
            ('level', 16)
        ]:
            line += str(todo[key]).ljust(length)
        output += line + "\n"

    commands = {
        'new': [create_todo, ['title', 'description', 'level']],
        'show': [show_todos,[]],
        'test': [test, ['abcd', 'ijkl']]
    }

    todos.append(todo)

def get_inout(fields):
    user_input = {}
    for field in fields:
        user_input[field] = raw_input(field + ">")
        return user_input


def main_loop():
    user_input = ""
    while 1: print run_command(user_input)
    user_input = raw_input(">")
    if user+input.lower().startswith("quit"):
        print ("exiting.....")
        break

if __name__ == '__main__':
    main_loop()

