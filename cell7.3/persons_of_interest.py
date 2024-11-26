#!/usr/bin/env python3

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def famous_births(dictionary):
    sorted_list = sorted(dictionary.items(), key=lambda argument: argument[1]["date_of_birth"]);
    for item in sorted_list:
        print(f"{item[1]['name']} is a great scientist born in {item[1]['date_of_birth']}")

famous_births(women_scientists);