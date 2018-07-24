#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time


def profile(func):
    """
    This is a decorator for profiling other features.

    ================= Important !!! =======================
    To function properly, you need to install the following modules:
    - OS
    - cProfile
    - pyprof2calltree
    - musical instruments
    - subprocess
    If any of these modules are missing, please install it.
    You must also have "kcachegrind" installed to preview the account.
    """

    # Importing necessary librarys
    import sys
    from functools import wraps
    import subprocess

    if "os" not in sys.modules.keys():
        import os
    if "cProfile" not in sys.modules.keys():
        import cProfile
    if "pyprof2calltree" not in sys.modules.keys():
        from pyprof2calltree import convert

    @wraps(func)
    def wrap_function(*args, **kwargs):

        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        convert(pr.getstats(), "ptof.tree")
        pr.print_stats(sort="time")
        input("Press the button to continue")
        try:
            subprocess.call("kcachegrind ptof.tree", shell=True)
        except OSError as err:
            if err.errno == os.errno.ENOENT:
                print("The program kcachegrind not found !!!")
            else:
                print("There is another issue with the visualization !!!")
        return result
    return wrap_function


@profile
def my_func():
    """This is test function"""

    print("Process 1")
    time.sleep(10)
    print("Process 2")
    print("Process 3")
    print("Process 4")
    return True


if __name__ == "__main__":
    my_func()
