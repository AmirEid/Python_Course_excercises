#!/usr/bin/env python3

try: 
    number = float(input("Enter a number less that 25: \n"));
    if (number > 25):
        raise Exception("ERROR");
    i = 0;
    while (i <= number):
        print(f"Inside the loop, my variable is {i}");
        i += 1;
except ValueError:
    print ("invalid input");
except KeyboardInterrupt:
    print ("\nYou pressed Ctrl+C.");
except Exception as e:
    print (f"{e}.");
