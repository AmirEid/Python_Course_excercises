#!/usr/bin/env python3

#iterate over the string way

string_input = input("Give me a string: ");
swap_case = "";
for char in string_input:
    if (char.isupper()):
        swap_case += char.lower();
    else:
        swap_case += char.upper();
print(swap_case);


print("Another way with 3 lines code:");
string_input = input("Give me a string: ");
swap_case = string_input.swapcase();
print(swap_case);
