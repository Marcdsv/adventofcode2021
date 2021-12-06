from itertools import groupby

with open("input.txt") as file:
    data = [list(group) for key, group in groupby(file.read().splitlines(), key=bool) if key]

calls = list(map(int, data[0][0].split(',')))
grids = []
for grid in data[1:]:
    grids.append([list(map(int, line.split())) for line in grid])

def won(grid, calls):
    for row in grid:
        if all([value in calls for value in row]):
            return True
    for col in zip(*grid):
        if all([value in calls for value in col]):
            return True
    return False

def score(grid, calls):
    return sum([value for flatten in grid for value in flatten if value not in calls])

def play(grids, calls):
    wins = []
    past_calls = []
    for call in calls:
        past_calls.append(call)
        for grid in list(grids):
            if won(grid, past_calls):
                wins.append(call * score(grid, past_calls))
                grids.remove(grid)
    return wins

if __name__ == "__main__":
    results = play(grids, calls)
    print(f"First win score: {results[0]}")
    print(f"Last win score: {results[-1]}")