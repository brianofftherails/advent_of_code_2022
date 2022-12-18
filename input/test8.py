#!/usr/bin/python3 

def column_update_visible(map_to_update, the_map, column):
    tallest = 0
    # top to bottom
    for i in range(len(the_map)):
        if the_map[i][column] > tallest:
            map_to_update[i][column] = tallest
            tallest = the_map[i][column]
    # bottom to top
    tallest = 0
    for i in range(len(the_map), -1, -1):
        if the_map[i][column] > tallest:
            map_to_update[i][column] = tallest
            tallest = the_map[i][column]

try:
    fp = open("../input/sample8.txt", "r")
except FileNotFoundError:
    print("Failed to open input file")
    raise FileNotFoundError

the_map = fp.readlines()

xmax = len(the_map[0][:-1])
ymax = len(the_map)

visible_bmp = [[0 for y in range(xmax)] for x in range(ymax)]

column_update_visible(the_map, visible_bmp, 0)
print(visible_bmp)