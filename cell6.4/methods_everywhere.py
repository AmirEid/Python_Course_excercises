#!/usr/bin/env python3

import sys;

def shrink(string):
    print(string[:8]);

def enlarge(string):
    while (len(string) < 8):
        string += "Z";
    print(string);

argc = len(sys.argv);
if (argc > 1):
    for args in sys.argv[1:]:
        if (len(args) > 8):
            shrink(args);
        elif (len(args) < 8):
            enlarge(args);
        else:
            print(args);
else:
    print("none");