import pandas as pd

def read_csv_file(file_name):
    '''
    read a csv file and turn it into a dataframe

    Parameters
    ----------
    file_name : string or path object
        path to the file

    Returns
    --------
    df : pandas.DataFrame
        a pandas DataFrame object of the data in the csv file
    '''
    return pd.read_csv(file_name)


def read_txt_file(file_name):
    '''
    read a plain text file


    Parameters
    ----------
    file_name : string or path object
        path to the file

    Returns
    -------
    text : string
        text of the file as a single string
    '''
    with open(file_name,'r') as f:
        txt = f.read()

    return txt

def split_txt_file(text):
    '''
    split a blob of text into a list

    Parameters
    ----------
    text : string
        text as read from a todo.txt file

    Returns
    -------
    list_txt : the same text, split into a list of items
    '''
    return text.split('\n')[:-1]


def is_file_extension(file_name, text_extension):
    '''
    check if the given file has the specified extension

    Parameters
    ----------
    file_name : string or path object
        path to the file

    text_extension : string
        the file extension (the part after the .) to be checked for

    Returns
    --------
    is_match : boolean
        True if the file has the specified extension

    '''
    name, ext = file_name.split('.')

    return ext == text_extension




def count_tasks(todo_list):
    '''
    count items overall or by group

    Parameters
    ----------
    todo_list : list or dictionary
        todo list as a list or a grouped todo list as a dictionary


    Returns
    --------
    count : integer or dictionary
        the count of items in the list or a dictionary with the same keys as
    input and the number of items in each value as the values

    '''
    counters_by_type = {list:lambda l: len(l),
                       dict: lambda d: {k:len(v) for k,v in d.items()}
                       }
    return counters_by_type[type(todo_list)](todo_list)


def group_tasks(todo_list, by='project'):
    '''
    group tasks by a specific feild of the todo.txt standard

    Parameters
    -----------
    todo_list : list
        todo list to work with
    by : {'project', 'context', or 'due_date'}
        type of content to group by

    '''
    symbol = {'project':'+',
              'context':'@',
              'due_date':'due:'}
    num_chars = {k:len(v) for k,v in symbol.items()}

    n = num_chars[by]

    # parse the list to find the keys
    keys = [w[n:] for task in todo_list for w in task.split() if w[:n] == symbol[by]]

    # setup empty
    grouped_tasks = {k:[] for k in set(keys)}
    grouped_tasks['none'] = []

    for task in todo_list:
        if symbol[by] in task:
            cur_key = [w[n:] for w in task.split() if w[:n] == symbol[by]][0]
            grouped_tasks[cur_key].append(task)
        else:
            grouped_tasks['none'].append(task)

    return grouped_tasks

def grouped_to_list(grouped_tasks,order_dicts=None,ascending=False ):
    '''
    take grouped tasks and put them back to a list, optionally ordered by
    a dictionary otherwise sorted ascending


    Parameters
    -----------
    grouped_tasks : dict

    '''

    if order_dicts:
        key_order = sorted(order_dicts,reverse=not(ascending))
    else:
        key_order = grouped_tasks.keys()

    out_list = []

    for key in key_order:
        out_list.extend(grouped_tasks[key])

    return out_list


def search_code_file(file_name, comment_type = '#'):
    '''
    find comments in a code file that have todo items


    Parameters
    '''
    todo_list = []

    with open(file_name,'r') as f:
        line = f.readline()
        while line:
            if 'todo' in line.lower():
                uncommented = line.replace(comment_type,'').strip()

                #remove 'todo' by splitting into words, checkign each, then joining back
                task = ' '.join([word for word in uncommented if not('todo' in word.lower())])

                todo_list.append(task)


    return todo_list


def combine_lists(todolist1,todolist2):
    '''
    combine two lists

    Parameters
    ----------
    todolist1 : list
        list of todo items
    todolist2 : list
        list of todo items

    Returns
    -------
    combined_list : list
        one list with all items
    '''
    return todolist1 + todolist2

def write_file(todo_list,file_name):
    '''
    write a lit out to a file

    Parameters
    ----------
    todo_list : list
        list of todo items
    file_name : string or path object
        path to the file

    Returns
    -------
    '''
    with open(file_name,'w') as f:
        for item in todo_list:
            f.write(item)
            f.write('\n')


def remove_complete_tasks(todo_list):
    '''
    remove items that are marked complete (first character is x, then space)


    Parameters
    ----------
    todo_list : list
        list of todo items

    Returns
    -------
    todo_list : list
        list of todo items without complete items

    '''
    return [item for item in todo_list if not(is_complete(item))]


def is_complete(todo_item):
    '''
    check if a single item is complete  (first character is x, then space)

    Parameters
    ----------
    todo_item : string
        one item from a todolist

    Returns
    -------
    is_done : boolean
        true if the line starts with 'x '

    '''
    return todo[:2] == 'x '
