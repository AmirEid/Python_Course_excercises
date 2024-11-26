#!/usr/bin/env python3

import sys;

argc = len(sys.argv);
if (argc != 2):
    print("none");
    sys.exit(1);
else:
    for char in sys.argv[1]:
        if (char == 'z'):
            print("z", end="");