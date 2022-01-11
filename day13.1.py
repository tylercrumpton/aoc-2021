from collections import defaultdict
import numpy
from numpy.core.numeric import count_nonzero

with open("day13.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

break_found = False
coords = []
instructions = []
max_y = max_x = 0
for line in lines:
    if line == "":
        break_found = True
        continue
    if not break_found:
        x, y = line.split(",")
        x, y, = int(
            x
        ), int(y)
        coords.append((x, y))
        max_x = max(x, max_x)
        max_y = max(y, max_y)
    else:
        instructions.append(line)

points = numpy.zeros((max_y + 1, max_x + 1))

print(points)
print(instructions)

for coord in coords:
    points[coord[1]][coord[0]] = 1
print(points)


fold = 655
top = points[:, :fold]
bottom = points[:, fold + 1 :]

print(top.shape)
print(bottom.shape)
newbottom = top[:, -bottom.shape[1] :] + numpy.fliplr(bottom)
newtop = top[:, : -bottom.shape[1]]

print(f"{top=}")
print(f"{bottom=}")
print(f"{newtop=}")
print(f"{newbottom=}")

print(f"{top.shape=}")
print(f"{bottom.shape=}")
print(f"{newtop.shape=}")
print(f"{newbottom.shape=}")

print(f"{numpy.count_nonzero(top)=}")
print(f"{numpy.count_nonzero(bottom)=}")
print(f"{numpy.count_nonzero(newtop)=}")
print(f"{numpy.count_nonzero(newbottom)=}")

print(f"{numpy.count_nonzero(newbottom)+numpy.count_nonzero(newtop)=}")
