#!/usr/bin/env python3

import sys;

def add_one(x):
    return x + 1;

argc = len(sys.argv);
if argc != 1:
    print("none");
    sys.exit(1);
else:
    variable = 0;
    print(variable);
    variable = add_one(variable);
    print(variable);