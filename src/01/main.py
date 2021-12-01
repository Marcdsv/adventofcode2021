with open("input.txt") as file:
    data = list(map(int, file.read().splitlines()))

def part1(data: list[int]) -> int:
    result = sum([data[index] < data[index + 1] for index in range(len(data[1:]))]) 
    return result

def part2(data: list[int]) -> int:
    windows = [sum(data[index:index + 3]) for index in range(len(data[1:-1]))]
    return part1(windows)

print(part1(data))
print(part2(data))