filepath = "todos.txt"
def get_todos():
    """ Read a text file and return the list of
     to-do item. """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg):
    """ Wtrite the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def water_state(temp):
    FREEZING_POINT = 0
    BOILING_POINT = 100
    if temp <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temp < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"