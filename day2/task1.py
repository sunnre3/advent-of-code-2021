#!/usr/bin/python3

horizontal_inputs = []
depth_inputs = []

def get_int_from_string(str):
    for word in str.split():
        if word.isdigit():
            return int(word)

with open('./inputs.txt', 'r') as file:
    for line in file:
        if 'up' in line:
            depth_inputs.append(-abs(get_int_from_string(line)))
        elif 'down' in line:
            depth_inputs.append(get_int_from_string(line))
        else:
            horizontal_inputs.append(get_int_from_string(line))

print(sum(horizontal_inputs) * sum(depth_inputs))