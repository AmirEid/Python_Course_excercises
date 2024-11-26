#!/usr/bin/env python3

def greetings(name = ""):
    if not name:
        print("Hello, noble stranger!");
    elif not isinstance(name, str):
        print(f"ERROR! It was not a name. It was: {name}");
    else:
        print(f"Hello, {name}!");

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)