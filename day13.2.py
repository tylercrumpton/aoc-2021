import numpy

with open("day13.input.chip.txt", "r") as f:
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

points = numpy.zeros((max_y + 1, max_x + 1), dtype=int)

print(points.shape)
print(instructions)

for coord in coords:
    points[coord[1]][coord[0]] = 1
# print(points)


def fold_paper(paper, axis, index):
    if axis == "x":
        half1 = paper[:, :index]
        half2 = paper[:, index + 1 :]
        return half1 + numpy.flip(half2, axis=1)
    else:
        half1 = paper[:index, :]
        half2 = paper[index + 1 :, :]
        return half1 + numpy.flip(half2, axis=0)


for instruction in instructions:
    axis = instruction.split("=")[0][-1:]
    index = int(instruction.split("=")[1])
    print("YO", axis, index)

    points = fold_paper(points, axis, index)
    print(points)
points[points > 0] = 2
numpy.set_printoptions(edgeitems=30, linewidth=100000)
print(points)
