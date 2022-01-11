import re

with open("day04.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    # whole_file = f.read()


called_nums = [
    "0",
    "56",
    "39",
    "4",
    "52",
    "7",
    "73",
    "57",
    "65",
    "13",
    "3",
    "72",
    "69",
    "96",
    "18",
    "9",
    "49",
    "83",
    "24",
    "31",
    "12",
    "64",
    "29",
    "21",
    "80",
    "71",
    "66",
    "95",
    "2",
    "62",
    "68",
    "46",
    "11",
    "33",
    "74",
    "88",
    "17",
    "15",
    "5",
    "6",
    "98",
    "30",
    "51",
    "78",
    "76",
    "75",
    "28",
    "53",
    "87",
    "48",
    "20",
    "22",
    "55",
    "86",
    "82",
    "90",
    "47",
    "19",
    "25",
    "1",
    "27",
    "60",
    "94",
    "38",
    "97",
    "58",
    "70",
    "10",
    "43",
    "40",
    "89",
    "26",
    "34",
    "32",
    "23",
    "45",
    "50",
    "91",
    "61",
    "44",
    "35",
    "85",
    "63",
    "16",
    "99",
    "92",
    "8",
    "36",
    "81",
    "84",
    "79",
    "37",
    "93",
    "67",
    "59",
    "54",
    "41",
    "77",
    "42",
    "14",
]

i = 0
board = 0
boards = []
while i < len(lines):
    if lines[i] == "":
        new_board = []
        for line in lines[i + 1 : i + 6]:
            new_board += line.split()
        i += 6
        boards.append(new_board)
    else:
        i += 1


def check_board(board):
    for i in range(5):
        # check rows:
        if board[i * 5 : i * 5 + 5] == ["-"] * 5:
            return True

        # check cols:
        winner = True
        for j in range(5):
            if board[j * 5 + i] != "-":
                winner = False
                break
        if winner:
            return True


# print(whole_file.replace("\n", "\n"))
for called_num in called_nums:
    print(called_num)
    boards_to_del = []
    for i in range(len(boards)):
        # print(boards[i])
        boards[i] = ["-" if num == called_num else num for num in boards[i]]
        if check_board(boards[i]):
            print(boards[i])
            boards_to_del.append(i)
    for i in sorted(boards_to_del, reverse=True):
        del boards[i]
print("no ")
