"""Module providing the reduce method"""
import functools

with open('content.txt', encoding="utf-8") as f:
    content = f.readlines()

content = [int(line.strip()) if line != '\n' else -1 for line in content]

sublist = [[]]

for item in content:
    if item == -1:
        sublist.append([])
    else:
        sublist[-1].append(item)

for inventory in sublist:
    inventory_sum = functools.reduce(lambda a, b: a + b, inventory)
    inventory[:] = [inventory_sum]

maximum_wrapped = [max(inventory) for inventory in sublist]

maximum = max((inventory for inventory in maximum_wrapped))

print(maximum)
