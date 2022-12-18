#!/usr/bin/python3

try:
    fp = open("../input/input7.txt", "r")
except OSError:
    print("Failed to open input file")
    raise OSError

current_dir = list("/") # maintained kind of sort of like a dentry
all_directories = dict()

# add all directories, irrespective of hierarchy
for entry in fp.readlines()[1::]:
    print(f"----------------\n{entry}")
    line = entry.split()
    if line[1] == "cd":
        if line[2] == "..":
            print("move up directory")
            current_dir = current_dir[0:-1]
        else:
            print(f"moved to {line[2]} directory")
            current_dir.append(line[2])
    curr_dir = "/" + "/".join(current_dir[1::])
    print(f"Directory is {curr_dir}")
    try:
        file_size = int(line[0])
    except ValueError:
        continue # skip doing anything
    curr_dir = "/" + "/".join(current_dir[1::])
    if curr_dir in all_directories.keys():
        all_directories[curr_dir] = all_directories[curr_dir] + file_size
    else:
        all_directories.update({curr_dir : file_size})
    print(f"----------------")

# Add sizes of child directories to parent directories
for directory in all_directories.keys():
    parent = "/".join(directory.split("/")[:-1])
    if parent in all_directories.keys():
        all_directories[parent] += all_directories[directory]

count = 0
for size in all_directories.values():
    if size <= 100000:
        count += 1
print(all_directories)
print(f"Count for part 1: {count}")
