#!/usr/bin/env python3

def array_of_names(persons):
    names = [];
    for first_name, last_name in persons.items():
        names.append(first_name.capitalize() + " " + last_name.capitalize());
    return names;

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
names = array_of_names(persons);
print(names);
print(array_of_names(persons));
