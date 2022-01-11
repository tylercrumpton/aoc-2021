from collections import defaultdict


with open("day05.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    # whole_file = f.read()

spots = defaultdict(lambda: 0)
for line in lines:
    xy1, xy2 = line.split(" -> ")
    x1, y1 = [int(c) for c in xy1.split(",")]
    x2, y2 = [int(c) for c in xy2.split(",")]

    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2 + 1):
                spots[f"{x1},{i}"] += 1
        else:
            for i in range(y2, y1 + 1):
                spots[f"{x1},{i}"] += 1
    elif y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                spots[f"{i},{y1}"] += 1
        else:
            for i in range(x2, x1 + 1):
                spots[f"{i},{y1}"] += 1
    else:
        if x1 < x2:
            if y1 < y2:
                for i in range(0, x2 - x1 + 1):
                    spots[f"{x1+i},{y1+i}"] += 1
            else:
                for i in range(0, x2 - x1 + 1):
                    spots[f"{x1+i},{y1-i}"] += 1
        else:
            if y1 < y2:
                for i in range(0, x1 - x2 + 1):
                    spots[f"{x1-i},{y1+i}"] += 1
            else:
                for i in range(0, x1 - x2 + 1):
                    spots[f"{x1-i},{y1-i}"] += 1

print(spots)
print(len([key for key, value in spots.items() if value > 1]))
