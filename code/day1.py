#!/usr/bin/python3

try:
    fp = open("input.txt", "r")
except OSError:
    print("Failed to open file")
    exit
all_contents = fp.readlines()
knapsacks = list()
knapsacks.extend([0])
idx = 0
for line in all_contents:
    try:
        knapsacks[idx] += int(line)
    except ValueError:
        idx += 1
        knapsacks.extend([0])
knapsacks.sort()
print(sum(knapsacks[-3::]))