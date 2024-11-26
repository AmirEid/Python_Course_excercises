#!/usr/bin/env python3

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck" : "red"
}

def my_function(family):
    for key, value in family.items():
        print(key, ":", value);

def has_redhead(person):
    if person[1] == "red":
            return True;
    return False;

def find_the_redheads(family):
    redheads = list(filter(has_redhead, family.items()));
    redheads_names = [person[0] for person in redheads];
    return redheads_names;
    
        
print(find_the_redheads(dupont_family));
my_function(dupont_family);