from collections import defaultdict, Counter, deque

with open("day16.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

line = lines[0]
binary = ""
for char in line:
    binary += f"{int(char, 16):>04b}"
# binary = bin(int(line, 16))[2:]
# expected_len = len(line) * 4
# binary = ("0" * (expected_len - len(binary))) + binary
print(binary)

version_counts = 0


def parse_pkt(pkt):
    global version_counts
    version = int(pkt[:3], 2)
    type = int(pkt[3:6], 2)
    rest = pkt[6:]
    value = None
    length_type = None
    length = number = None
    sub_pkts = None
    if type == 4:  # Literal
        value = ""
        last = False

        while not last:
            value += rest[1:5]
            if rest[0] == "0":
                last = True
            rest = rest[5:]
        value = int(value, 2)

    else:  # Operator
        length_type = int(rest[0], 2)
        rest = rest[1:]
        if length_type == 0:  # length based
            length = int(rest[:15], 2)
            rest = rest[15:]
            sub_pkts = []
            starting_rest_len = len(rest)
            print("starting subs", starting_rest_len)
            while len(rest) > starting_rest_len - length:
                (
                    sub_version,
                    sub_type,
                    sub_value,
                    sub_length_type,
                    sub_length,
                    sub_number,
                    sub_sub_pkts,
                    rest,
                ) = parse_pkt(rest)
                sub_pkts.append(
                    (
                        sub_version,
                        sub_type,
                        sub_value,
                        sub_length_type,
                        sub_length,
                        sub_number,
                        sub_sub_pkts,
                    )
                )

        elif length_type == 1:  # number based
            number = int(rest[:11], 2)
            rest = rest[11:]
            sub_pkts = []
            for _ in range(number):
                (
                    sub_version,
                    sub_type,
                    sub_value,
                    sub_length_type,
                    sub_length,
                    sub_number,
                    sub_sub_pkts,
                    rest,
                ) = parse_pkt(rest)
                sub_pkts.append(
                    (
                        sub_version,
                        sub_type,
                        sub_value,
                        sub_length_type,
                        sub_length,
                        sub_number,
                        sub_sub_pkts,
                    )
                )
        else:
            raise LookupError

    print(
        f"{version=}, {type=}, {value=}, {length_type=}, {length=}, {number=}, {sub_pkts= }, {rest=}"
    )
    version_counts += version
    return version, type, value, length_type, length, number, sub_pkts, rest


parse_pkt(binary)
print(version_counts)
