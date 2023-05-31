# in format 'x-y' to return x, y
def range_to_list(range):
    [left, right] = range.split('-')
    return [int(left), int(right)]

with open('input.txt') as f:
    lines = f.readlines()

teams = [line.strip().split(',') for line in lines]

count = 0

for team in teams:
    member_1 = range_to_list(team[0])
    member_2 = range_to_list(team[1])
    if member_1[0] <= member_2[0] and member_1[1] >= member_2[1]:
        print(member_1, member_2)
        count += 1
    elif member_2[0] <= member_1[0] and member_2[1] >= member_1[1]:
        count += 1
        print(member_1, member_2)
    
print(count)