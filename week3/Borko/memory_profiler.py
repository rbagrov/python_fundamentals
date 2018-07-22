#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import cProfile
from pyprof2calltree import convert
from functools import wraps
import time


def profile(func):
    """
    This is finction decorator for profiling other functions
    """
    @wraps(func)
    def wrap_function(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        convert(pr.getstats(), "ptof.tree")
        print(pr.print_stats(sort="time"))
        input("Press the button to continue")
        os.system("kcachegrind ptof.tree ")
        return result
    return wrap_function


@profile
def my_func():
    print("Process 1")
    time.sleep(10)
    print("Process 2")
    print("Process 3")
    print("Process 4")
    return True


if __name__ == "__main__":
    my_func()
