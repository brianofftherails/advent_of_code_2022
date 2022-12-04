#!/usr/bin/python3

try:
    fp = open("../input/input4.txt", "r")
except OSError:
    print("Failed to open input")
    exit

count = 0 # found set A in set B or vice versa

for line in fp.readlines():
    id_first = line.split(',')[0]
    id_second = line.split(',')[1]
    id_first = [i for i in range(int(id_first.split('-')[0]), int(id_first.split('-')[1]) + 1)]
    id_second = [i for i in range(int(id_second.split('-')[0]), int(id_second.split('-')[1]) + 1)]
    needed_matches = min(len(id_first), len(id_second))
    found_matches = 0
    for identifier in id_first:
        if identifier in id_second:
            found_matches += 1
    if found_matches == needed_matches:
        count += 1

print(f"Count for first part is {count}")
fp.seek(0)
count = 0

for line in fp.readlines():
    id_first = line.split(',')[0]
    id_second = line.split(',')[1]
    id_first = [i for i in range(int(id_first.split('-')[0]), int(id_first.split('-')[1]) + 1)]
    id_second = [i for i in range(int(id_second.split('-')[0]), int(id_second.split('-')[1]) + 1)]
    for identifier in id_first:
        if identifier in id_second:
            count += 1
            break
print(f"Count for second part is {count}")


