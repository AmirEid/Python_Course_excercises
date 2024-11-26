#!/usr/bin/env python3

import sys

argc = len(sys.argv)
if (argc != 2):
    print("none");
    sys.exit(1)
else:
    answer = input("What was the parameter? ");
    if (answer == sys.argv[1]):
        print("Good job!");
    else:
        print("Nope, sorry...");