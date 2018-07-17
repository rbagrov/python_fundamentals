# -*-config: utf_8 -*-

# Import library
from functools import wraps


def doc_validation(func):
    """"
    Function decorator
    Validates the docstring based on the given model
    Records the results of the validation of the docstring in the log file
    log.txt
    """
    @wraps(func)
    def wrapper_function(*args, **kwargs):

        m1 = func.__doc__.find("Accepts:")
        m2 = func.__doc__.find("Returns:")
        m3 = func.__doc__.find("Raises:")

        if (m1 > -1 and m1 < m2 and m2 < m3):
            validation_flag = 'Validation completed successfully !!!'
        else:
            validation_flag = 'Validation failed !!!'

        with open('log.txt', 'w', encoding="utf-8") as log:
            log.write(validation_flag)

        return func(*args, **kwargs)

    return wrapper_function


@doc_validation
def som_func():      # The function of which we read docstring
    """
    Calculate the square root of a number.
    Accepts:
    n: the number to get the square root of.
    Returns:
    the square root of n.
    Raises:
    TypeError: if n is not a number.
    ValueError: if n is negative.
    """
    pass


# if __name__ == "main":
som_func()
