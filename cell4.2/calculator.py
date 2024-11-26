#!/usr/bin/env python3
try:
    number1 = float(input("Give me the first number: "));
    number2 = float(input("Give me the second number: "));
    print("Thank you!");
    print(f"{number1} + {number2} = {number1 + number2}");
    print(f"{number1} - {number2} = {number1 - number2}");
    print(f"{number1} / {number2} = {number1 / number2}");
    print(f"{number1} * {number2} = {number1 * number2}");
except ValueError:
    print("Invalid input");
except ZeroDivisionError:
    print("You cannot divide by zero");
except KeyboardInterrupt:
    print("You have pressed Ctrl+C");
except EOFError:
    print("You have pressed Ctrl+D");
except Exception as e:
    print(f"An error occurred: {e}");