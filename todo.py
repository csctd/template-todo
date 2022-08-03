import pandas as pd

def read_csv_file(file_name):
    '''
    read a file and turn it into a dataframe
    '''
    return pd.read_csv(file_name)


def read_txt_file(file_name):
    '''
    
    '''
    with open(file_name,'r') as f:
        txt = f.read()
    
    return txt

def split_txt_file(text):
    '''
    '''
    return txt.split('\n')[:-1]
    


def count_tasks(todo_list):
    '''
    count items 
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
    
    '''
    sybmol = {'project':'+',
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
        if by in task:
            cur_key = [w[n:] for w in task.split() if w[:n] == symbol[by]]
            grouped_task[cur_key].append(task)
        else: 
            grouped_tasks['none'].append(task)
    
    
    
    
def search_code_file(file_name, comment_type = '#'):
    '''
    '''
    todo_list = []
    
    with open(file_name,'r') as f:
        line = f.readline()
        while line:
            if 'todo' in line.lower():
                uncommented = line.replace(comment_type,'').strip()
                
                #remove 'todo' y splitting into words, checkign each, then joining back
                task = ' '.join([word for word in uncommented if not('todo' in word.lower())])
                
                todo_list.append(task)
                
                
    return todo_list


        
