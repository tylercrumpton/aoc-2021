with open("day03.input.txt", "r") as f:
    lines = f.readlines()

print(f"lines{len(lines)}")
a=[0,0,0,0,0,0,0,0,0,0,0,0,0]
for line in lines:
    # print(line)
    for i, char in enumerate(line):
        print(char, " ", i)

        if char == "1":
            a[i] += 1



print(a)
