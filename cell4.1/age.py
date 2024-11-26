#!/usr/bin/env python3

try:
    age = int(input("Please tell me your age: "));
    print(f"You are currently {age} years old.");
    i = 10;
    while (i < 40):
        print(f"In {i} years, you'll be {age + i} years old.");
        i += 10;
except ValueError:
    print("Please enter a valid number.");
except KeyboardInterrupt:
    print("You've pressed Ctrl+C.");
except EOFError:
    print("You've pressed Ctrl+D.");
except Exception as e:
    print(f"An error occurred: {e}");