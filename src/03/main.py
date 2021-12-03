import copy

with open("input.txt") as file:
    data = file.read().splitlines()

# part1
def gamma_rate(data: list[str]) -> str:
    return "".join([max(sorted(bits, reverse=True), key=bits.count) for bits in zip(*data)])

def epsilon_rate(data: list[str]) -> str:
    return "".join([min(sorted(bits), key=bits.count) for bits in zip(*data)])

print(f"Power consumtion: {int(gamma_rate(data), 2) * int(epsilon_rate(data), 2)}")

# part2
oxygen = copy.deepcopy(data)
co2 = copy.deepcopy(data)
for index in range(len(data[0])):
    gamma = gamma_rate(oxygen)
    oxygen = [value for value in oxygen if value[index] == gamma[index]] if len(oxygen) > 1 else oxygen
    epsilon = epsilon_rate(co2)
    co2 = [value for value in co2 if value[index] == epsilon[index]] if len(co2) > 1 else co2

print(f"Life support rating: {int(oxygen[0], 2) * int(co2[0], 2)}")