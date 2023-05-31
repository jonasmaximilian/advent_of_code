import functools

def convert_to_prio(char):
    if char.isupper():
        return ord(char) - 38
    return ord(char) - 96

with open('input.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

duplicates = []

for line in lines:
    for char in line[:int(len(line)/2)]:
        if char in line[int(len(line)/2):]:
            
            duplicates.append(char)
            break

duplicates = [convert_to_prio(char) for char in duplicates]

res = functools.reduce(lambda a, b: a + b, duplicates)

print(res)

test = [1,2,3,4,5,6,7,8]
print(test[:4])
print(test[4:])
