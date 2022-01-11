with open("day08.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

{
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


digits = [
    (line.split("|")[0].strip().split(), line.split("|")[1].strip().split())
    for line in lines
]


count = 0

for digit in digits:
    output = digit[1]
    for number in output:
        if len(number) in [2, 3, 4, 7]:
            count += 1
    print(output)

print(count)
