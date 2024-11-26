#!/usr/bin/env python3

import sys;
import re;

argc = len(sys.argv);
if (argc != 3):
    print("none");
    sys.exit(1);
else:
    found = re.findall(sys.argv[1], sys.argv[2]);
    size = len(found);
    print(size);

#re.findall() returns a list of all matches of the first param in the second param.