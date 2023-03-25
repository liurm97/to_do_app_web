FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """
    Read a file path and write contents of the file to a list.
    """

    with open(filepath, 'r') as file:
        box = file.readlines()
    return box

# Flip the position of filepath and mode as positional argument needs to come before optional argument.
def write_todos(box,filepath=FILEPATH):
    """
    :param mode: Provide either 'r','w','a','r+','w+'
    :param filepath: Read the file at the filepath provided
    :return: Write elements of the box list to todos.txt file.
    """
    with open(filepath, 'w') as file:
        file.writelines(box)

# Include IF statement to not run below code in mainCLI.py
if __name__ == '__main__':
    print(f'functions.py: {__name__}')
    # print('Hello from FUNCTIONS.PY !!!')