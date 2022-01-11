from types import new_class


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
mappings = []
for digit in digits:
    # print(digit)
    input_num = digit[0]
    output = digit[1]
    one_digit = None
    seven_digit = None
    four_digit = None
    eight_digit = None
    nine_digit_ish = None # all but 'g'
    nine_digit = None
    zero_digit = None
    two_digit = None
    six_digit = None
    five_digit = None
    three_digit = None
    pattern = {}
    for _ in range(60):
        for number in input_num+output:

            match len(number):
                case 2:
                    one_digit = set(number)
                case 3:
                    seven_digit = set(number)
                case 4:
                    four_digit = set(number)
                case 7:
                    eight_digit = set(number)
                case 6:
                    # print(f"{number=}")
                    if eight_digit and one_digit and four_digit and len((eight_digit-four_digit).union(one_digit)-set(number)) == 0:
                        zero_digit = set(number)
                    if zero_digit and one_digit:
                        if len((zero_digit-one_digit)-set(number)) == 1:
                            nine_digit = set(number)
                        elif set(number) != zero_digit:
                            six_digit = set(number)
                case 5:
                    if six_digit and one_digit:
                        if len(six_digit-one_digit-set(number)) == 2:
                            three_digit = set(number)
                    if nine_digit and three_digit and set(number) != three_digit:
                        if len(set(number) - nine_digit) == 0:
                            five_digit = set(number)
                        else:
                            two_digit = set(number)
                    #num-nine ==0 :5
                    # if zero -one -num == 1: 9

            #     case 6:
            #         if not nine_digit and nine_digit_ish and len(nine_digit_ish-set(number)) == 0:
            #             nine_digit = set(number)
            #             pattern['g'] = (nine_digit - seven_digit - four_digit).pop()
            #         if not zero_digit and one_digit and len(one_digit-set(number)) == 0 and set(number) != nine_digit:
            #             zero_digit = set(number)
            #             # pattern["e"] = (zero_digit - nine_digit).pop()
            #         if not six_digit and zero_digit and nine_digit and (set(number) not in [nine_digit, zero_digit]):
            #             six_digit = set(number)
            #     case 5:
            #         # if not two_digit and zero_digit and one_digit and seven_digit and len(set(number) - set([pattern["a"], pattern["e"], pattern["g"]])) == 2:
            #         #     # if a e g found: and number has all three, then number is 2 and number -  zero-digit is 'd'
            #         #     two_digit = set(number)
            #         #     pattern['d'] = (set(number)-zero_digit).pop()
            #         if not five_digit and six_digit and len(six_digit - set(number)) == 1:
            #             five_digit = set(number)
            #         if five_digit and two_digit and set(number) not in [five_digit, two_digit]:
            #             three_digit = set(number)
            #         if nine_digit and five_digit and len(set(number)-nine_digit) == 0 and set(number) != five_digit:
            #             three_digit = set(number)
            #         if set(number) not in [three_digit, five_digit]:
            #             two_digit = set(number)
            #         # if nine-num = 0 and not num=5, then three


            # if four_digit and seven_digit:
            #     nine_digit_ish = four_digit.union(seven_digit)
            # if one_digit and seven_digit:
            #     pattern["a"] = (seven_digit-one_digit).pop()

    mapping = {}
    mapping["".join(sorted(zero_digit))] = 0
    mapping["".join(sorted(one_digit))] = 1
    mapping["".join(sorted(two_digit))] = 2
    mapping["".join(sorted(three_digit))] = 3
    mapping["".join(sorted(four_digit))] = 4
    mapping["".join(sorted(five_digit))] = 5
    mapping["".join(sorted(six_digit))] = 6
    mapping["".join(sorted(seven_digit))] = 7
    mapping["".join(sorted(eight_digit))] = 8
    mapping["".join(sorted(nine_digit))] = 9

    mappings.append(mapping)
    # print (pattern)
    # print(f"{zero_digit=},{one_digit=},{two_digit=},{three_digit=}{four_digit=},{five_digit=},{six_digit=},{seven_digit=},{eight_digit=},{nine_digit=}")
    # print("\n")

# print (mapping)

total = 0
for i in range(len(digits)):
    output = digits[i][1]
    print(f"{[''.join(sorted(digit)) for digit in digits[i][0]+digits[i][1]]=}")
    print(f"{mappings[i]=}")
    new_output = [mappings[i]["".join(sorted(d))] for d in output]

    print("".join([str(i) for i in new_output]))
    total += int("".join([str(i) for i in new_output]))

print(total)