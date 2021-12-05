#!/usr/bin/python3sh pytr

inputs = []
with open('./inputs.txt', 'r') as file:
    inputs = file.read().splitlines()

oxygen = ''
scrubber = ''
remaining = inputs
for pos in range(len(inputs[0])):
    zeroes = []
    ones = []

    for inp in remaining:
        if inp[pos] == '0':
            zeroes.append(inp)
        else:
            ones.append(inp)

    if len(zeroes) > len(ones):
        remaining = zeroes
    else:
        remaining = ones

    if len(remaining) == 1:
        oxygen = remaining[0]
        break

remaining = inputs
for pos in range(len(inputs[0])):
    zeroes = []
    ones = []

    for inp in remaining:
        if inp[pos] == '0':
            zeroes.append(inp)
        else:
            ones.append(inp)

    if len(zeroes) <= len(ones):
        remaining = zeroes
    else:
        remaining = ones

    if len(remaining) == 1:
        scrubber = remaining[0]

print(oxygen)
print(len(oxygen))
print(int(oxygen, 2))
print('===========')
print(scrubber)
print(len(scrubber))
print(int(scrubber, 2))
print('===========')
print(int(oxygen,2) * int(scrubber,2))
