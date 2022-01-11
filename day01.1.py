with open("day01.input.txt", "r") as f:
    depths = f.readlines()

count = 0
old_i = 999
for i_str in depths:
    i = int(i_str)
    if i > old_i:
        count += 1
    old_i = i

print(count)
