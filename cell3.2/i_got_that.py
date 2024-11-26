#!/usr/bin/env python3

try:
    text = input("What you gotta say? : ");
    while (True):
        if (text == "STOP"):
            break;
        else:
            text = input("I got that! Anything else? : ");
except KeyboardInterrupt:
    print("You stopped me c!");
except EOFError:
    print("You stopped me d!");
except Exception as e:
    print(f"An error occurred: {e}");
