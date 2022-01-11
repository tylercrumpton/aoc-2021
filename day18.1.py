with open("day18.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

number = "[[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]"
# after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
# after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
# after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
# after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
# after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]


def explode(number):
    level = 0
    left_number_index = right_number_index = None
    left_number_len = right_number_len = None
    i = 0
    parsing_num = False
    while i < len(number):
        if not parsing_num:
            if number[i] == "[":
                level += 1

            elif number[i] == "]":
                level -= 1

            else:
                parsing_num = True
                left_number_index = i
                left_number_len = 1
        else:
            if number[i] == "," or number[i] == "]":
                parsing_num = False
            else:
                left_number_len += 1
        i += 1


explode(number)
