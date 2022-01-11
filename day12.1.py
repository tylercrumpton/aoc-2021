from collections import defaultdict

with open("day12.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

caves = defaultdict(lambda: [])
for line in lines:
    start, end = line.split("-")
    caves[start].append(end)
    caves[end].append(start)

count = 0

used_twice = False


def find_all_paths(start, end, current_path):
    global count, used_twice
    used_twice = False
    used_twice_this_time = False
    if start == end:
        # print(current_path)

        # for cave in current_path:
        # if cave not in ["start", "end"] and cave.islower():
        count += 1
        # break
    else:
        for next_cave in caves[start]:
            if (
                next_cave.isupper()
                or next_cave not in current_path
                or (
                    next_cave in current_path
                    and not used_twice
                    and next_cave not in ["start", "end"]
                )
            ):
                if next_cave in current_path and next_cave.islower():
                    used_twice = True
                    used_twice_this_time = True

                new_current_path = current_path + [next_cave]
                try:
                    new_current_path += find_all_paths(next_cave, end, new_current_path)
                    return new_current_path
                except TypeError:
                    new_current_path.pop()
                    if used_twice_this_time:
                        used_twice = False
            else:
                pass  # bad path


print(caves)
print(find_all_paths("start", "end", ["start"]))
print(count)
