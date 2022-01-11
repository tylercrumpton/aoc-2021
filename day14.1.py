from collections import defaultdict, Counter
import numpy
import itertools


with open("day14.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

break_found = False
chain = None
rules = {}
for line in lines:
    if not break_found and not chain:
        chain = line
    elif not break_found:
        break_found = True
        continue
    else:
        pattern, value = line.split(" -> ")
        rules[pattern] = value


print(chain, rules)

# Loop over pairs once
counts = Counter([chain[i] + chain[i + 1] for i in range(len(chain) - 1)])

for _ in range(40):
    new_counts = Counter()
    for pair, value in counts.items():
        a, c = pair
        b = rules[pair]
        new_counts[a + b] += value
        new_counts[b + c] += value
    counts = new_counts

final_char_counts = Counter()
for pair, value in counts.items():
    final_char_counts[pair[1]] += value
final_char_counts[chain[0]] += 1
print(final_char_counts.most_common()[0][1] - final_char_counts.most_common()[-1][1])
