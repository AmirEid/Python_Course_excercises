#!/usr/bin/env python3

import sys

def downcase_it(string):
    return string.lower();

argc = len(sys.argv);
if argc == 1:
    print("none");
    sys.exit(1);
else:
    for args in sys.argv[1:]:
        print(downcase_it(args));