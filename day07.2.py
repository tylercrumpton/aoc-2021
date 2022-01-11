from typing import Counter


import numpy

with open("day07.input.sample.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

crabs = [int(i) for i in lines[0].split(",")]

crab_counts = Counter(crabs)

min_crab = min(crabs)
max_crab = max(crabs)


# dest = round(numpy.std(crabs))

for dest in range(min_crab, max_crab + 1):
    total = 0
    for crab_count in crab_counts.most_common():
        dist = abs(crab_count[0] - dest)
        total += int(dist * (dist + 1) / 2) * crab_count[1]

    print(total)


# 97164301
