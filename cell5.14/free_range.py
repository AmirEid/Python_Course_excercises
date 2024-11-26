#!/usr/bin/env python3

import sys

argc = len(sys.argv);
if (argc != 3):
    print("none");
    sys.exit(1);
else :
    number1 = int(sys.argv[1]);
    number2 = int(sys.argv[2]);
    array = [];
    for number in range(number1, number2 + 1):
        array.append(number);
    print(array);
    # while (number1 <= number2):
    #     array.append(number1);
    #     number1 += 1;
    # print(array);