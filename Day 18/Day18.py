with open("input.txt", "r") as file:
    data = [x.split() for x in file.read().splitlines()]
    grid_1, grid_2, current_1, current_2, steps_1, steps_2 = [(0, 0)],[(0, 0)], (0, 0), (0, 0), 0, 0
    walk = lambda n, d, x, y: {"U" : ((x, y - n)), "D" : ((x, y + n)), "L" : ((x - n, y)), "R" : ((x + n, y))}[d]
    for direction, steps, color in data:
        (grid_1.append(current_1 := walk((steps := int(steps)), direction, *current_1)), (steps_1 := steps_1 + steps))
        (grid_2.append(current_2 := walk((steps := int(color[2:-2], 16)), {"0" : "R", "1" : "D", "2" : "L", "3" : "U"}[color[-2]], *current_2)), (steps_2 := steps_2 + steps))
    result = []
    for grid, steps, inner in [(grid_1, steps_1, 0), (grid_2, steps_2, 0)]:
        for i in range(len(grid) - 1):
            (a, b), (c, d) = grid[i : i + 2]
            inner += a * d - b * c
        result.append(abs(inner) // 2 + steps // 2 + 1)
    print(result)