#!/usr/bin/python3
from math import floor
try:
    fp = open("../input/input3.txt", "r")
except OSError:
    print("Failed to open file")
    exit

priority = 0

for rucksack in fp.readlines():
    compartment_1 = rucksack[0:floor(len(rucksack)/2)]
    compartment_2 = rucksack[floor(len(rucksack)/2):-1]
    for item in [*compartment_1]:
        if item in [*compartment_2]:
            item = ord(item)
            if item > 96 and item < 123: # lower case
                priority += item - 96
            elif item > 64 and item < 91: # upper case
                priority += item - 64 + 26
            else:
                print("Error!")
                exit
            break
print(f"Priority for part 1 is {priority}")

elf_idx = 0
elf_trio_ruck = [""] * 3
priority = 0

fp.seek(0)

for rucksack in fp.readlines():
    elf_idx += 1
    elf_trio_ruck[elf_idx % 3] = rucksack
    if elf_idx % 3 == 0:
        for item in [*elf_trio_ruck[0]]:
            if item in [*elf_trio_ruck[1]] and item in [*elf_trio_ruck[2]]:
                item = ord(item)
                if item > 96 and item < 123: # lower case
                    priority += item - 96
                elif item > 64 and item < 91: # upper case
                    priority += item - 64 + 26
                else:
                    print("Error!")
                    exit
                break

print(f"Priority for part 2 is {priority}")     
