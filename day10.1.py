with open("day10.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}

opening = ["(", "{", "<", "["]
closing = [")", "}", ">", "]"]

score = 0
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
                score += scoring[char]
                break
            else:
                stack.pop()
        else:
            stack.append(char)
print(score)
