#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2];
new_array = [];
for i in range(len(array)):
    if (array[i] > 5):
        new_array.append(array[i] + 2);
print(new_array);

print("");
new_array = [];
for integer in array:
    if (integer > 5):
        new_array.append(integer + 2);
print(new_array);