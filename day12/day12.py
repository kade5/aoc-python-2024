import utils


def generate_garden(input_str: str) -> list[list[str]]:
    garden = []
    input_list = input_str.split("\n")
    for line in input_list:
        garden.append(list(line))

    return garden


def calculate_fence(column: int, row: int, plant: str, exists: set[(int, int)], garden: list[list[str]]) -> (int, int):
    area = 0
    perimeter = 0
    movement = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    if column < 0 or row < 0 or column >= len(garden) or row >= len(garden[column]):
        perimeter = 1
    elif (column, row) not in exists and garden[column][row] == plant:
        exists.add((column, row))
        area += 1

        for move in movement:
            a, p = calculate_fence(column + move[0], row + move[1], plant, exists, garden)
            area += a
            perimeter += p
    elif garden[column][row] != plant:
        perimeter = 1

    return area, perimeter


def part_1(file_path: str) -> int:
    input_str = utils.read_file_into_string(file_path)
    garden = generate_garden(input_str)
    result = 0
    exists: set[(int, int)] = set()
    for col, line in enumerate(garden):
        for row, plant in enumerate(line):
            a, p = calculate_fence(col, row, plant, exists, garden)
            result += a * p

    return result


def main():
    print(f"Part 1 Answer: {part_1("../input/day12.txt")}")


if __name__ == '__main__':
    main()
