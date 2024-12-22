import utils


def build_initial_stone_list(input_string: str) -> list[int]:
    input_list = input_string.split(" ")
    return list(map(int, input_list))


def blink(stone_list: list[int]) -> list[int]:
    new_list: list[int] = []

    for stone in stone_list:
        if stone == 0:
            new_list.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_string = str(stone)
            stone_half = len(stone_string) // 2
            new_list.append(int(stone_string[:stone_half]))
            new_list.append(int(stone_string[stone_half:]))
        else:
            new_list.append(stone * 2024)

    return new_list


def part_1(input_file: str, num_blinks=25) -> int:
    input_string = utils.read_file_into_string(input_file)
    stone_list = build_initial_stone_list(input_string)
    new_stone_list: list[int] = stone_list

    for _ in range(num_blinks):
        new_stone_list = blink(new_stone_list)

    return len(new_stone_list)


def main():
    print(f"Part 1 answer: {part_1('../input/day11.txt')}")
    # print(f"Part 2 answer: {part_1('../input/day11.txt', 75)}")


if __name__ == '__main__':
    main()
