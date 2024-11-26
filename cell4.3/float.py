#!/usr/bin/env python3
try:
    number = float(input("Give me a number: "));
    if (number.is_integer()):
        print("This number is an integer.");
    else:
        print("This number is decimal.");
except ValueError:
    print("Invalid input");
except KeyboardInterrupt:
    print("You have pressed Ctrl+C");
except EOFError:
    print("You have pressed Ctrl+D");
except Exception as e:
    print(f"An error occurred: {e}");

