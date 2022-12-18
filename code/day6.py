#!/usr/bin/python3

try:
    fp = open("../input/input6.txt", "r")
except OSError:
    print("Failed to open input file")
    raise OSError

data = list(fp.readlines()[0])
for i in range(4, len(data)):
    if len(set(data[i-4:i])) == 4:
        print(f"found start of packet at idx {i}")
        break
for i in range(14, len(data)):
    if len(set(data[i-14:i])) == 14:
        print(f"found start of message at idx {i}")