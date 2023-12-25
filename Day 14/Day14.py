import itertools

FILENAME = "input.txt"
ROUNDED = "O"
SQUARED = "#"
CYCLE_COUNT = 1_000_000_000


def transpose(matrix):
    return tuple(["".join(row) for row in zip(*matrix)])


def tilt(matrix, reverse_bool):
    tilted = []
    for row in matrix:
        row_split = [
            sorted(fragment, reverse=reverse_bool) for fragment in row.split(SQUARED)
        ]
        row_combined = "#".join("".join(fragment) for fragment in row_split)
        tilted.append(row_combined)
    return tuple(tilted)


def calculate_load(matrix):
    return sum(
        sum(len(row) - i for i, char in enumerate(row) if char == ROUNDED)
        for row in matrix
    )


def perform_cycle(matrix):
    for order in [True, True, False, False]:
        matrix = transpose(matrix)
        matrix = tilt(matrix, order)
    return matrix


def perform_cycles(matrix):
    memo, order = {}, {}
    for counter in itertools.count(1):
        matrix = perform_cycle(matrix)
        if matrix in memo:
            second_appearance, first_appearance = counter, memo[matrix]
            index = (CYCLE_COUNT - first_appearance) % (
                second_appearance - first_appearance
            ) + first_appearance
            return transpose(order[index])
        memo[matrix] = counter
        order[counter] = matrix


def main():
    with open(FILENAME) as f:
        matrix = [list(row) for row in f.read().split("\n")]

    tilted_part_one = tilt(transpose(matrix), True)
    print(calculate_load(tilted_part_one))

    tilted_part_two = perform_cycles(matrix)
    print(calculate_load(tilted_part_two))


if __name__ == "__main__":
    main()
