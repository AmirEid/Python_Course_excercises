#!/usr/bin/env python3

try:
    number = float(input("Enter a number: "));
    if number < 0:
        print ("The number is negative.");
    elif number > 0:
        print ("The number is positive.");
    else:
        print ("The number is both positive and negative.");
except ValueError:
    print ("You did not enter a number.");
except KeyboardInterrupt:
    print ("You pressed Ctrl+C.");
except Exception as e:
    print (f"An error occurred, {e}.");