import re
from math import prod

with open('input.txt') as f:
    txt = f.read()

lines = txt.split('\n')

part1 = 0
limit = {'red' : 12, 'green' : 13, 'blue' : 14}
part2 = 0

for game in lines:
    game_id = int(re.match('Game (\d+)', game).group(1))
    tokens = re.split('[:;]', game)
    valid = True
    minimum = {'red' : 0, 'green' : 0, 'blue' : 0}

    for random_draws in tokens[1:]:
        for rd in random_draws.strip().split(', '):
            quan, color = rd.split(' ')
            quan = int(quan)
            if limit[color] < quan:
                valid = False
            minimum[color] = max(minimum[color], quan)

    if valid:
        part1 += game_id
    part2 += prod(minimum.values())

print(part1)
print(part2)