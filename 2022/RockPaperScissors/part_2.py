with open('input.txt') as f:
    guide = f.readlines()

guide = [line.strip().replace(' ', '') for line in guide]

points = 0

for round in guide:
    me = round[1]
    if me == 'Y':
        points += 3
    if me == 'Z':
        points += 6

    opponent = round[0]

    # Choose rock
    if (opponent == 'A' and me == 'Y') or (opponent == 'B' and me == 'X') or (opponent == 'C' and me == 'Z'):
        points += 1
    
    # Choose paper
    if (opponent == 'A' and me == 'Z') or (opponent == 'B' and me == 'Y') or (opponent == 'C' and me == 'X'):
        points += 2

    # Choose scissor
    if (opponent == 'A' and me == 'X') or (opponent == 'B' and me == 'Z') or (opponent == 'C' and me == 'Y'):
        points += 3
        
print(points)
