with open("day09.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

grid = {}
ymax = len(lines)
xmax = len(lines[0])
for x in range(xmax):
    for y in range(ymax):
        grid[f"{x},{y}"] = int(lines[y][x])


min_coords = []
for coord in grid.keys():
    print(f"trying {coord=}")
    x, y = coord.split(",")
    x, y = int(x), int(y)
    keepgoing = True
    if (
        (x == 0 or grid[f"{x-1},{y}"] > grid[f"{x},{y}"])
        and (x == xmax - 1 or grid[f"{x+1},{y}"] > grid[f"{x},{y}"])
        and (y == 0 or grid[f"{x},{y-1}"] > grid[f"{x},{y}"])
        and (y == ymax - 1 or grid[f"{x},{y+1}"] > grid[f"{x},{y}"])
    ):
        min_coords.append(f"{x},{y}")


print(min_coords)
sum = 0
for i in min_coords:
    sum += 1 + grid[i]

print(sum)
