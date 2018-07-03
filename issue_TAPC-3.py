#-*-config: utf_8 -*import






#The function of which we read docstring
def som_func():
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

def doc_validation(func):
""""
Function decorator
Records the results of the validation of the docstring in the log file 'log.txt'
"""
def wrapper_function(*args, **kwargs):

doc_str = str(args)
if (doc_str.count('Accepts:')>0)and(doc_str.find('Raises:')>0)and(doc_str.find('Returns:')>0) :
validation_flag = 'Validation completed successfully !!!'
else:
validation_flag = 'Validation failed !!!'

with open('log.txt', 'w', encoding="utf-8") as log:
log.write(validation_flag)

return func(*args, **kwargs)

return wrapper_function

@doc_validation
def get_doc(d_func):
return True

get_doc(som_func.__doc__)
