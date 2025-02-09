### Function that prints arguments and exits program at that line (debugger)

import sys

def check(*args):
    for arg in args:
        print(arg)
    sys.exit()