#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2];
duplicated = set();
new_array = set();
array_new = set(array);
print("Array: ", array);
print("Duplicated: ", duplicated);
print("New Array: ", new_array);
print("array_new: ", array_new);
print("");
for integer in array:
    if integer in new_array:
        duplicated.add(integer);
    else:
        new_array.add(integer);
print("");
print("Array: ", array);
print("Duplicated: ", duplicated);
print("New Array: ", new_array);
print("");
array_new = set();
for integer in array:
    if integer not in duplicated:
        array_new.add(integer + 2);
print("array_new: ", array_new);