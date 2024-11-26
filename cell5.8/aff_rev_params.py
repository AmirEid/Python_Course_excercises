#!/usr/bin/env python3

import sys;

argc = len(sys.argv);

if (argc == 2):
    print("none");
    sys.exit(1);
else:
    while (argc > 1):
        print(sys.argv[argc - 1]);
        argc -= 1;
