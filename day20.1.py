with open("day20.input.sample2.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


input_image = {}
decoder = None
for i, line in enumerate(lines):
    if i == 0:
        decoder = line
    elif i >= 2:
        y = i - 2
        for x, pixel in enumerate(line):
            if pixel == "#":
                input_image[x, y] = 1


def get_affected_coords(lit_coord):
    x, y = lit_coord
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]


flasher_state = False


def check_flasher(input_image, coord):
    for affected in get_affected_coords(coord):
        if affected in input_image:
            return False
    return True


def get_index(input_image, coord):
    binary_string = ""
    for affected in get_affected_coords(coord):
        if check_flasher(input_image, affected):
            binary_string += "1" if flasher_state else "0"
            print(f"{affected} is a flasher")
        else:
            binary_string += str(input_image.get(affected, 0))
    return int(binary_string, 2)


def process_input_image(input_image):
    output_image = {}
    coords_to_process = set()
    for lit_coord in input_image.keys():
        coords_to_process = coords_to_process.union(set(get_affected_coords(lit_coord)))
    for coord in coords_to_process:
        index = get_index(input_image, coord)
        if decoder[index] == "#":
            output_image[coord] = 1

    return output_image


# input_image = {(2, 0): 1, (0, 1): 1, (0, 2): 1, (1, 2): 1}
# print(get_index(input_image, (1, 1)))
# flasher_state = False
# input_image = process_input_image(input_image)
flasher_state = True
input_image = process_input_image(input_image)
print(len(input_image))

# 5400 is too high
