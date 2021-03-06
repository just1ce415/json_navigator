"""
Laboratory 3.2
GitHub: https://github.com/just1ce415/json_navigator.git
"""
import json
import jmespath

PATH = 'tests/frienfs_list_Obama.json'

def open_json(path:str) -> dict:
    '''
    Opens a json file and returns a dict.
    '''
    filepointer = open(path, 'r', encoding='utf-8')
    return json.load(filepointer, cls=None, object_hook=None, parse_float=None,
    parse_int=None, parse_constant=None, object_pairs_hook=None)


def request_input(printed_path:str, options:object) -> str:
    '''
    Provides the user to pick the key or object in the json file checking its input.
    '''
    usr_input = input(printed_path + ' $ ')
    # THE RANGE GIVEN
    if isinstance(options, type(range(1))):
        while not isinstance(usr_input, int):
            # TRYING CHECK IF INPUT MAY BE CONVERTED TO INT
            try:
                usr_input = int(usr_input)
            except ValueError:
                pass
            # CHECKING IF INPUT IN RANGE
            if not isinstance(usr_input, int) or usr_input not in options:
                usr_input = input(printed_path + ' $ ')
    # THE LIST GIVEN
    elif isinstance(options, list):
        while usr_input not in options:
            usr_input = input(printed_path + ' $ ')
    return usr_input


def get_options(prime_object:object) -> object:
    '''
    Returns options for user to pick.

    >>> get_options([1, 4, -55, 12])
    range(0, 4)
    >>> get_options({'key1': 'val1', 'key2': 'val2'})
    ['key1', 'key2']
    >>> get_options('foo')

    '''
    if isinstance(prime_object, list):
        return range(len(prime_object))
    elif isinstance(prime_object, dict):
        return list(prime_object.keys())
    return None


def update_paths(json_path:str, printed_path:str, command:object, prime_object_type:type) -> tuple:
    '''
    Updates json_path and printed_path depens on command.

    >>> update_paths('section', 'kved.json:/section/', 'group', dict)
    ('section.group', 'kved.json:/section/group/')
    >>> update_paths('section', 'kved.json:/section/', 1, dict)
    ('section.1', 'kved.json:/section/1/')
    >>> update_paths('section', 'kved.json:/section/', 1, list)
    ('section[1]', 'kved.json:/section/[1]/')
    '''
    if prime_object_type == list:
        json_path += '['+str(command)+']'
        printed_path += '['+str(command)+']/'
    elif prime_object_type == dict:
        if json_path == '':
            json_path += str(command)
        else:
            json_path += '.' + str(command)
        printed_path += str(command)+'/'
    else:
        return None
    return (json_path, printed_path)


def start_navigator(json_dict:dict):
    '''
    The main function that provides navigation info to the terminal.
    '''
    # COMPILE-COMMAND FOR JMESPATH
    json_path = ''
    # PATH TO DISPLAY FOR USER
    printed_path = PATH + ':/'
    next_object = json_dict
    # ITERATING WHILE THE OBJECT USER PICKING IS DICT OT LIST
    while isinstance(next_object, (list, dict)):
        # OPTIONS FOR USER
        options = get_options(next_object)
        print(str(options))
        # GETTING USER'S INPUT
        command = request_input(printed_path, options)
        # UPDATING PATHS
        json_path, printed_path = update_paths(json_path, printed_path, command, type(next_object))
        # RECIVENG NEXT OBJECT
        next_object = jmespath.search(json_path, json_dict)
    print(next_object)


if __name__ == '__main__':
    #import doctest
    #print(doctest.testmod())
    start_navigator(open_json(PATH))
