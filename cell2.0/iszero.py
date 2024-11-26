#!/usr/bin/env python3

try: 
    number = float(input("Enter a number: "));
    if number == 0:
        print ("The number is zero.");
    else:
        print ("The number is not zero.");
except ValueError:
    print ("You did not enter a number.");
except KeyboardInterrupt:
    print ("\nYou pressed Ctrl+C.");
except Exception as e:
    print (f"An error occurred, {e}.");