#!/usr/bin/env python3

class MyClass:
    def __init__(self, name):
        self.name = name;
        print(f"Class created!");

    def hello(self):
        print(f"Hello, everyone! my name is {self.name}")

new_class = MyClass("Amir");
print("");
new_class.hello();