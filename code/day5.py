#!/usr/bin/python3
from math import ceil

'''
get_cargo : get cargo from input, storing in a list
will return an empty list on fail
'''
def get_cargo(data):
    if not isinstance(data, list):
        return list()
    num_rows = 0
    for line in data:
        if line[0] != "[":
            break
        else:
            num_rows += 1
    num_columns = ceil(len(data[0]) / 4)

    cargo = list()
    for cargo_row in range(num_columns):
        cargo.append(list())
    for cargo_row in data[num_rows-1::-1]:
        for i in range(num_columns):
            letter = cargo_row[1 + 4 * i]
            if letter != ' ':
                cargo[i].append(letter)
    return cargo



try:
    fp = open("../input/input5.txt", "r")
except OSError:
    print("Failed to open input")
    raise SystemExit

data = fp.readlines()
cargo = get_cargo(data)
if cargo == []:
    raise ValueError

for instruction in data:
    instructions = instruction.split(" ")
    if instructions[0] != "move":
        continue
    for i in range(int(instructions[1])):
        cargo[int(instructions[5]) - 1].append(cargo[int(instructions[3]) - 1].pop())
print("Part 1:")
for stack in cargo:
    print(stack[-1])

cargo = get_cargo(data)
if cargo == []:
    raise ValueError

for instruction in data:
    instructions = instruction.split(" ")
    if instructions[0] != "move":
        continue
    cargo[int(instructions[5]) - 1].extend(cargo[int(instructions[3]) - 1][-int(instructions[1])::])
    for i in range(int(instructions[1])):
        cargo[int(instructions[3]) - 1].pop()
print("Part 2:")
for stack in cargo:
    print(stack[-1])