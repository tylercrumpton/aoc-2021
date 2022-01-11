with open("day19.input.sample.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

scanner_number = -1
scanners = {}
for line in lines:
    if line == "":
        continue
    elif line.startswith("---"):
        scanner_number += 1
    else:
        scanners[scanner_number] = scanners.get(scanner_number, []) + [
            [int(i) for i in line.split(",")]
        ]


for coord in scanners[0]:

