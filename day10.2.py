with open("day10.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


scoring = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

opening = ["(", "{", "<", "["]
closing = [")", "}", ">", "]"]

scores = []
stack = []
for line in lines:
    print(line)
    for char in line:
        if len(stack) == 0:
            if char in closing:
                pass  # TODO CORRUPTED
            else:
                stack.append(char)
        elif stack[-1] in opening and char in closing:
            if opening.index(stack[-1]) != closing.index(char):
                print(
                    f"expected {closing[opening.index(stack[-1])]} but found {char} instead"
                )
                stack = []
                break
            else:
                stack.pop()
        else:
            stack.append(char)
    if stack != []:
        score = 0
        for _ in range(len(stack)):
            char = stack.pop()
            closing_char = closing[opening.index(char)]
            score = score * 5 + scoring[closing_char]
        scores.append(score)

print(sorted(scores)[len(scores) // 2])
