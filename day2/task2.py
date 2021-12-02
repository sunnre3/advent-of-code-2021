#!/usr/bin/python3

horizontal = 0
depth = 0
aim = 0

def get_int_from_string(str):
    for word in str.split():
        if word.isdigit():
            return int(word)

with open('inputs.txt', 'r') as file:
    for line in file:
        if 'down' in line:
            aim = aim + get_int_from_string(line)
        elif 'up' in line:
            aim = aim - get_int_from_string(line)
        else:
            value = get_int_from_string(line)
            horizontal = horizontal + value
            depth = depth + (aim * value)

print(horizontal*depth)
