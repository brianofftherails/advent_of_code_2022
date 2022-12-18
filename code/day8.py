#!/usr/bin/python3

def column_update_visible(map_to_update, the_map, column):
    tallest = 0
    for i in range(len(the_map)):
        #print(f"the_map[{i}][{column}]: {the_map[i][column]}")
        try:
            if int(the_map[i][column]) > tallest:
                #print(f"{int(the_map[i][column])} > {tallest}")
                map_to_update[i][column] = tallest = int(the_map[i][column])
        except ValueError:
            continue
    # bottom to top
    tallest = 0
    for i in range(len(the_map) - 1, -1, -1):
        #print(f"the_map[{i}][{column}]: {the_map[i][column]}")
        if int(the_map[i][column]) > tallest:
            #print(f"{int(the_map[i][column])} > {tallest}")
            map_to_update[i][column] = tallest = int(the_map[i][column])
    return True


def row_update_visible(map_to_update, the_map, row):
    tallest = 0
    for i in range(len(the_map[row])):
        try:
            height = int(the_map[row][i])
        except (ValueError, IndexError):
            continue
        if int(height) > tallest:
            #print(f"{int(height)} > {tallest}")
            map_to_update[row][i] = tallest = int(height)
    tallest = 0
    for i in range(len(the_map[row]) - 1, 0, -1):
        try:
            height = int(the_map[row][i])
        except (ValueError, IndexError):
            continue
        if int(height) > tallest:
            #print(f"{int(height)} > {tallest}")
            map_to_update[row][i] = tallest = int(height)


def update_visible_map(map_to_update, the_map):
    for i in range(len(the_map[0][:-1])): 
        if False == column_update_visible(map_to_update, the_map, i):
            print(f"Failed to update column")
            raise ValueError
    for i in range(len(the_map)):
        row_update_visible(map_to_update, the_map, i)


'''part 1'''
def get_visible(bitmap):
    visible_count = 0
    for row in visible_bmp:
        for char in row:
            if char != 0:
                visible_count += 1
    print(visible_count)
    return visible_count

try:
    fp = open("../input/input8.txt", "r")
except FileNotFoundError:
    print("Failed to open input file")
    raise FileNotFoundError

the_map = fp.readlines()

xmax = len(the_map[0][:-1])
ymax = len(the_map)

visible_bmp = [[0 for x in range(xmax)] for y in range(ymax)]

#print(range(len(the_map[0][:-1])))
update_visible_map(visible_bmp, the_map)
get_visible(visible_bmp)