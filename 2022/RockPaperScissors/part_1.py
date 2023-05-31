with open('input.txt') as f:
    guide = f.readlines()

guide = [line.strip().replace(' ', '') for line in guide]

points = 0

for round in guide:
    me = round[1]
    points += ord(me) - 87

    opponent = round[0]

    if (opponent == 'A' and me == 'X') or (opponent == 'B' and me == 'Y') or (opponent == 'C' and me == 'Z'):
        points += 3

    if (opponent == 'A' and me == 'Y') or (opponent == 'B' and me == 'Z') or (opponent == 'C' and me == 'X'):
        points += 6
        
print(points)