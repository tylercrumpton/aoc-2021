import numpy

with open("day11.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

octopuses = numpy.array([[int(char) for char in row] for row in lines])

grid_width = 10

iterations = 19500
flash_count = 0
for i in range(iterations):
    octopuses += 1
    # print(octopuses)
    flashers = []
    # print(numpy.where(octopuses > 9))
    while True:
        more_than_niners = numpy.where(octopuses > 9)
        num_of_more_than_niners = len(more_than_niners[0])
        if num_of_more_than_niners == 0 or num_of_more_than_niners == len(flashers):
            break
        else:
            # print(f"{num_of_more_than_niners=}, {len(flashers)=}")
            pass
        for j in range(num_of_more_than_niners):
            x, y = more_than_niners[0][j], more_than_niners[1][j]
            if (x, y) in flashers:
                continue
            else:
                octopuses[
                    max(0, x - 1) : min(grid_width, x + 2),
                    max(0, y - 1) : min(grid_width, y + 2),
                ] += 1
                # print(octopuses)
                flashers.append((x, y))
                flash_count += 1
    print(octopuses)
    octopuses = numpy.where(octopuses > 9, 0, octopuses)
    if not numpy.any(octopuses):
        break
print(i)
print(octopuses)
# print(flash_count)
