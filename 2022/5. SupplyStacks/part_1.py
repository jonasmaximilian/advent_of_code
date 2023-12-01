with open('test_input.txt') as f:
    lines = f.readlines()

lines = [line.split(' ') for line in lines]

for i in range(0, len(lines)):
    if lines[i] == ['\n']:
        crates = lines[0:i-1]
        commands = lines[i+1:len(lines)]



print('Crates: ', crates)
print('Commands: ', commands)