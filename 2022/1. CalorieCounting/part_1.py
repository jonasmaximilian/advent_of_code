import functools

with open('input.txt') as f:
    input = f.readlines()

input = [int(line.strip()) if line != '\n' else -1 for line in input]

sublist = [[]]

for item in input:
    if item == -1:
        sublist.append([])
    else:
        sublist[-1].append(item)

for inventory in sublist:
    sum = functools.reduce(lambda a, b: a + b, inventory)
    inventory[:] = [sum]

maximum_wrapped = [max(inventory) for inventory in sublist]

maximum = max([inventory for inventory in maximum_wrapped])

print(maximum)
