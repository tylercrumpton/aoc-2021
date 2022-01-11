from typing import List


with open("day03.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


while len(lines) > 1:
    for bit_num in range(len(lines[0])):
        print(f"{len(lines)=}, working on {bit_num=}")
        lines_to_delete = []
        num_ones = 0
        for line_num in range(len(lines)):
            print(f"{line_num=}: {lines[line_num]}")
            if lines[line_num][bit_num] == "1":
                num_ones += 1
        bit_value_to_keep = "1" if num_ones >= len(lines) / 2 else "0"
        print(f"{bit_value_to_keep=}")

        lines = [line for line in lines if line[bit_num] == bit_value_to_keep]
        if len(lines) == 1:
            break

print(f"first: {lines[0]}")

with open("day03.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

while len(lines) > 1:
    for bit_num in range(len(lines[0])):
        # print(f"{len(lines)=}, working on {bit_num=}")
        lines_to_delete = []
        num_ones = 0
        for line_num in range(len(lines)):
            # print(f"{line_num=}: {lines[line_num]}")
            if lines[line_num][bit_num] == "1":
                num_ones += 1
        bit_value_to_keep = "0" if num_ones >= len(lines) / 2 else "1"
        # print(f"{bit_value_to_keep=}")

        lines = [line for line in lines if line[bit_num] == bit_value_to_keep]
        if len(lines) == 1:
            break
print(f"second: {lines[0]}")
