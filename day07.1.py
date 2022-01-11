from typing import Counter
from statistics import median

with open("day07.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

crabs = [int(i) for i in lines[0].split(",")]

crab_counts = Counter(crabs)
dest = int(median(crabs))

total = 0
for crab_count in crab_counts.most_common():
    total += abs(crab_count[0] - dest) * crab_count[1]

print(total)
