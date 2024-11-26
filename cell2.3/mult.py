#!/usr/bin/env python3

try:
    number1 = float(input("Enter the first number: "));
    number2 = float(input("Enter the second number: "));
    result = number1 * number2;
    print(f"{number1} * {number2} = {result}");
    if (result < 0):
        print("The result is negative");
    elif (result > 0):
        print("The result is positive");
    else:
        print("The result is zero");
except ValueError:
    print("Invalid input");
except KeyboardInterrupt:
    print ("You have pressed ctrl + c");
except EOFError:
    print("You have pressed ctrl + d");
except Exception as e:
    print(f"An error occurred: {e}");