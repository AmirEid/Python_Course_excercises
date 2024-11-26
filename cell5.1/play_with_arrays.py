#!/usr/bin/env python3

array = [1, 2, 3, 4, 5];
new = [];
for integer in array:
    new.append(integer + 2);
print(array);
print(new);

print("");
new = [];
for i in range(len(array)):
    new.append(array[i] + 2);
print(array);
print(new);

print("");
print("easy code in 3 lines: ")
new_array = [x + 2 for x in array];
print(array);
print(new_array);
