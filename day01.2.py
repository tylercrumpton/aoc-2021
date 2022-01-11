with open("day01.input.txt", "r") as f:
    depths = f.readlines()

depths = [int(i) for i in depths]

count = 0
old_i = 99999
for index in range(len(depths) - 2):
    new_i = sum(depths[index : index + 3])
    print(f"new_i:{new_i}, old_i:{old_i}, index:{index}")
    if new_i > old_i:
        count += 1
        print(count)
    old_i = new_i

print(count)
