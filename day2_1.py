
fp = open("input2.txt", "r")
guide = fp.readlines()
score = 0
for line in guide:
    if line[0] == 'A': # opponent chooses rock
        score += 1
        if line[2] == 'X':
            score += 3
        elif line[2] == 'Y':
            score += 6
        elif line[2] == 'Z':
            score += 0
    elif line[0] == 'B': # opponent chooses paper
        score += 2
        if line[2] == 'X':
            score += 0
        elif line[2] == 'Y':
            score += 3
        elif line[2] == 'Z':
            score += 6
    elif line[0] == 'C': # opponent chooses scissors
        score += 3
        if line[2] == 'X':
            score += 6
        elif line[2] == 'Y':
            score += 0
        elif line[2] == 'Z':
            score += 3
    else:
        print("Error!")
print(score)
