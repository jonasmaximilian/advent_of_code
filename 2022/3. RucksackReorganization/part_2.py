import functools

def convert_to_prio(char):
    if char.isupper():
        return ord(char) - 38
    return ord(char) - 96

with open('input.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

#divide into lists of 3
groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

duplicates = []

for group in groups:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            duplicates.append(char)
            break;

duplicates = [convert_to_prio(char) for char in duplicates]

res = functools.reduce(lambda a, b: a + b, duplicates)

print(res)
