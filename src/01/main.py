with open("input.txt") as file:
    data = file.read().splitlines()

result = sum([int(data[index]) < int(data[index + 1]) for index in range(len(data[1:]))])

print(result)