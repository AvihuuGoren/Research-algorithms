import inspect
from func_for_test import *

# Q1
def safe_call(f,*args,**kwargs):
    """Checks if the parmaters to the function are valid
    https://stackoverflow.com/questions/12592/can-you-check-that-an-exception-is-thrown-with-doctest-in-python used this to be able to check exceptions
    >>> safe_call(func1,5,6,c=7.0) 
    5
    >>> safe_call(func1,5,6,c="a") # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: Wrong type for argument:c. Should be:<class 'float'> Actual:<class 'int'> 
    >>> safe_call(func1,5.5,6,c=7.0) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: Wrong type for argument:a. Should be:<class 'int'> Actual:<class 'float'>
    """
    # Check for args
    names = f.__code__.co_varnames
    annotations = inspect.getfullargspec(f).annotations
    for index ,arg in enumerate(args):
        if names[index] in annotations:
            if type(arg) is not annotations[names[index]]:
                raise TypeError(f'Wrong type for argument:{names[index]}. Should be:{annotations[names[index]]} Actual:{type(arg)}')
    # Check for kwargs
    for key, value in kwargs.items():
        if key in annotations:
            if type(value) is not annotations[key]:
                raise TypeError(f'Wrong type for argument:{key}. Should be:{annotations[key]} Actual:{type(arg)}')
    if len(args) == 0:
        return f(kwargs)
    if len(kwargs) == 0:
        return f(*args)
    if len(kwargs) == 0 and len(args) == 0:
        return f()
    return f(*args,kwargs)
# Q2

def breadth_first_search(start,end,neighbor_function):
    """Checks if the parmaters to the function are valid
    https://stackoverflow.com/questions/12592/can-you-check-that-an-exception-is-thrown-with-doctest-in-python used this to be able to check exceptions
    >>> breadth_first_search((0,0),(2,2),four_neighbor_function) 
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    >>> breadth_first_search((0,0),(4,4),four_neighbor_function) 
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    >>> breadth_first_search((0,0,0),(2,2,2),six_neighbor_function)
    [(0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0), (2, 2, 0), (2, 2, 1), (2, 2, 2)]
    """
    fathers = {}
    visited = {}
    q = []
    q.append(start)
    visited[start] = True
    fathers[start] = None   
    while q:
        node = q.pop(0)
        for neighbor in neighbor_function(node):
            if neighbor not in visited:
                visited[neighbor] = True
                fathers[neighbor] = node
                q.append(neighbor)
                if neighbor == end:
                    route = []
                    route.append(neighbor)
                    father = fathers[neighbor]
                    while father:
                        route.append(father)
                        father = fathers[father]
                    route.reverse()
                    return route

# Q3
#didnt had time

import doctest
doctest.testmod()