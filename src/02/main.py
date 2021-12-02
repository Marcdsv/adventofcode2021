with open("input.txt") as file:
    data = file.read().splitlines()

horizontal = 0
depth = 0
aim = 0
for command in data:
    move, value = command.split()
    match move:
        case "forward":
            horizontal += int(value)
            depth += aim * int(value)
        case "down":
            aim += int(value)
        case "up":
            aim -= int(value)
            
print(horizontal * depth)