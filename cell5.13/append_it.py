#!/usr/bin/env python3

import sys;

argc = len(sys.argv);
if (argc < 2):
    print("none");
    sys.exit(1);
else:
    i = 1;
    while (i < argc):
        print(f"{sys.argv[i]}" + "ism");
        i += 1;