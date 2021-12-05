#!/usr/bin/python3sh pytr

inputs = []
with open('./inputs.txt', 'r') as file:
    inputs = file.read().splitlines()

arr = []
for char in range(len(inputs[0])):
    arr.append(0)

for inp in inputs:
    for idx, val in enumerate(list(inp)):
        arr[idx] = int(arr[idx]) + int(val)


gamma = ''
epsilon = ''

for bit in arr:
    if bit > len(inputs) / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(gamma, epsilon)
print(int(gamma, 2), int(epsilon, 2))
