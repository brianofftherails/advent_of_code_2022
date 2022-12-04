#!/usr/bin/python3

fp = open("input2.txt", "r")
guide = fp.readlines()
score = 0
for line in guide:
    if line[0] == 'A': # opponent chooses rock
        #score += 1
        if line[2] == 'X': # you choose rock
            score += 3 + 1
        elif line[2] == 'Y': # you choose paper
            score += 6 + 2
        elif line[2] == 'Z': # you choose scissors
            score += 0 + 3
    elif line[0] == 'B': # opponent chooses paper
        #score += 2
        if line[2] == 'X': # you choose rock
            score += 0 + 1
        elif line[2] == 'Y': # you choose paper
            score += 3 + 2
        elif line[2] == 'Z': # you choose scissors
            score += 6 + 3
    elif line[0] == 'C': # opponent chooses scissors
        #score += 3
        if line[2] == 'X': # you choose rock
            score += 6 + 1
        elif line[2] == 'Y': # you choose paper
            score += 0 + 2
        elif line[2] == 'Z': # you choose scissors
            score += 3 + 3
    else:
        print("Error!")
print(f"Part 1: {score}")

score = 0

for line in guide:
    if line[0] == 'A': # opponent chooses rock
        #score += 1
        if line[2] == 'X': # lose, scissors
            score += 0 + 3
        elif line[2] == 'Y': # draw, rock
            score += 3 + 1
        elif line[2] == 'Z': # win, paper
            score += 6 + 2
    elif line[0] == 'B': # opponent chooses paper
        #score += 2
        if line[2] == 'X': # lose, rock
            score += 0 + 1
        elif line[2] == 'Y': # tie, paper
            score += 3 + 2
        elif line[2] == 'Z': # win, scissors
            score += 6 + 3
    elif line[0] == 'C': # opponent chooses scissors
        #score += 3
        if line[2] == 'X': # lose, paper
            score += 0 + 2
        elif line[2] == 'Y': # tie, scissors
            score += 3 + 3
        elif line[2] == 'Z': # win, rock
            score += 6 + 1
    else:
        print("Error!")
print(f"Part 2: {score}")