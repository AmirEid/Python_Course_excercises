#!/usr/bin/env python3

try:
    number = float(input("Enter a number: "));
    i = 0;
    while (i < 10):
        print(f"{i} * {number} = {i * number}");
        i += 1.0;
except ValueError:
    print("Invalid number");
except KeyboardInterrupt:
    print("\nYou have pressed Ctrl+C");
except EOFError:
    print("\nYou have pressed Ctrl+D");
except Exception as e:
    print(f"An error occurred: {e}");