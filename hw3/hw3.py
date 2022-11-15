import re
from typing import TypeVar
_T = TypeVar("_T")

##Q1##
## Used https://docs.python.org/3/library/re.html and https://www.w3schools.com/python/python_regex.asp
## for information about Regex in python
def check_valid_email(file_name):
    """
    >>> check_valid_email("mail_list.txt") 
    valid:
    abc.def@mail.com
    abc.def@mail.com.com
    abc@mail.com
    abc_def@mail.com
    abc.def@mail.cc
    abc.def@mail-archive.com
    abc.def@mail.org
    abc.def@mail.com
    invalid:
    abc-@mail.com
    abc..def@mail.com
    .abc@mail.com
    abc#def@mail.com
    abc-d@mail.com
    abc.def@mail.c
    abc.def@mail#archive.com
    abc.def@mail
    abc.def@mail..com
    """
    def check_email(email:str):
        pattern = r'([a-z0-9]+[.-_])*[a-z0-9]+@[a-z0-9-]+(\.[a-z]+[a-z]+)+'
        r = re.fullmatch(pattern,email)
        return False if r is None else True
    with open(file = file_name,mode='r') as f:
            mail_list = f.readlines()
            valid = [mail.rstrip('\n') for mail in mail_list if check_email(mail.rstrip('\n')) is True]
            invalid = [mail.rstrip('\n') for mail in mail_list if check_email(mail.rstrip('\n')) is False]
            print("valid:")
            for mail in valid : print(mail)
            print("invalid:")
            for mail in invalid : print(mail)


##Q2
def lastcall(func):
    output_cache = {}
    def wrapper(x):
        if x in output_cache:
            print(f"I already told you that the answer is {output_cache[x]}")
        else:
            output_cache[x] = func(x)
            return output_cache[x]
    wrapper.__doc__ = func.__doc__
    return wrapper


@lastcall
def func1(x):
    """
    >>> func1(1) 
    1
    >>> func1(1)
    I already told you that the answer is 1
    >>> func1(2)
    2
    >>> func1(1)
    I already told you that the answer is 1
    >>> func1(2)
    I already told you that the answer is 2
    """
    return x

@lastcall
def func2(x):
    """
    >>> func2(2) 
    4
    >>> func2(2)
    I already told you that the answer is 4
    """
    
    return x * x



##Q3 
class List(list):
    """
    >>> List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]]])[0,1,3]
    66
    >>> List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]]])[0]
    [[1, 2, 3, 33], [4, 5, 6, 66]]
    >>> List([[0],List([5,6])])[1,0]
    5
    >>> l = List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]]])
    >>> l[0] = [0]
    >>> l
    [[0], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]]]
    >>> l = List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]]])
    >>> l.remove([[1,2,3,33],[4,5,6,66]])
    >>> l
    [[[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]]]
    >>> List([[0,0]])[0][0]
    0
    """
    

    def __getitem__(self, *args) -> _T:
        if isinstance(*args,tuple) is False:
            return super().__getitem__(args[0])
        ans = super().__getitem__(args[0][0])
        for i in range (1,len(args[0])):
            ans = ans.__getitem__(args[0][i])
        return ans
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
