#!/usr/bin/env python3

import sys

argc = len(sys.argv)
if (argc != 2):
    print("none");
    sys.exit(1)
else:
    print(sys.argv[1].lower());