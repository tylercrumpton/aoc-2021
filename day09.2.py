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
    # print(f"trying {coord=}")
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


def size_basin(min_point):
    coords_to_check = set([min_point])
    visited_coords = set([min_point])

    while len(coords_to_check) > 0:
        coord = coords_to_check.pop()
        x, y = coord.split(",")
        x, y = int(x), int(y)

        if (
            x - 1 >= 0
            and f"{x-1},{y}" not in visited_coords
            and grid[f"{x-1},{y}"] != 9
            and grid[f"{x-1},{y}"] >= grid[f"{x},{y}"]
        ):
            coords_to_check.add(f"{x-1},{y}")
            visited_coords.add(f"{x-1},{y}")

        if (
            x + 1 < xmax
            and f"{x+1},{y}" not in visited_coords
            and grid[f"{x+1},{y}"] != 9
            and grid[f"{x+1},{y}"] >= grid[f"{x},{y}"]
        ):
            coords_to_check.add(f"{x+1},{y}")
            visited_coords.add(f"{x+1},{y}")

        if (
            y - 1 >= 0
            and f"{x},{y-1}" not in visited_coords
            and grid[f"{x},{y-1}"] != 9
            and grid[f"{x},{y-1}"] >= grid[f"{x},{y}"]
        ):
            coords_to_check.add(f"{x},{y-1}")
            visited_coords.add(f"{x},{y-1}")

        if (
            y + 1 < ymax
            and f"{x},{y+1}" not in visited_coords
            and grid[f"{x},{y+1}"] != 9
            and grid[f"{x},{y+1}"] >= grid[f"{x},{y}"]
        ):
            coords_to_check.add(f"{x},{y+1}")
            visited_coords.add(f"{x},{y+1}")

    return len(visited_coords)


basin_sizes = []
for min_coord in min_coords:
    basin_sizes.append(size_basin(min_coord))

print(sorted(basin_sizes)[-3:])
