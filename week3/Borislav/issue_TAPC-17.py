# -*- coding: utf8 -*-

# Import library
from functools import wraps


# Function decorator
def func_ann_validation(func):
    """
    This is a function decorator that checks and validates
    the annotation of other features
    """

    @wraps(func)
    def wrapper_function(*args, **kwargs):
        func_args_list = list(args)
        func_args_list.append(func(*args))
        func_ann_tup = tuple(func.__annotations__.values())
        for arts_index in range(len(func_args_list)):
            if type(func_args_list[arts_index]) != func_ann_tup[arts_index]:
                print('Annotattion Eror !!!')
                return func(*args, **kwargs)
        print('Annotation is correct !!!')
        return func(*args, **kwargs)

    return wrapper_function


# The function we need to validate
@func_ann_validation
def som_func(a: str, b: int) -> str:
    """
    This is the test function
    """

    return('Done !!!')


if __name__ == "main":
    som_func('Borislav', 13)  # Called function with Correct Annotation
    som_func('Borislav', "13")  # Called function with Incorrect Anotation
