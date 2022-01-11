with open("day02.input.txt", "r") as f:
    lines = f.readlines()

depth = 0
aim = 0
pos = 0
for line in lines:
    command, value = line.split(" ")
    match command:
        case "forward":
            pos += int(value)
            depth += int(value) * aim
        case"up":
            aim -= int(value)
        case "down":
            aim += int(value)

print(depth * pos)
