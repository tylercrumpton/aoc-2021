with open("day06.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

fishes = [int(i) for i in lines[0].split(",")]

fishes_array = [fishes.count(i) for i in range(9)]

for i in range(256):
    zeroes = fishes_array.pop(0)
    fishes_array[6] += zeroes
    fishes_array.append(zeroes)
print(sum(fishes_array))
