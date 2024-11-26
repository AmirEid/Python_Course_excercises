#!/usr/bin/env python3

import sys;

argc = len(sys.argv);
if (argc != 2):
    print("none");
else:
    print(f"{sys.argv[1].upper()}");