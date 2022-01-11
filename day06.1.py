import numpy

with open("day06.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    # whole_file = f.read()


fishes = [int(i) for i in lines[0].split(",")]
fishes_vector = numpy.array(fishes)

for i in range(256):
    print(i)
    print(fishes_vector)
    fishes_vector = fishes_vector - 1

    (fishes_to_reset,) = numpy.where(fishes_vector == -1)
    fishes_to_add = len(fishes_to_reset)
    print(fishes_to_add)

    numpy.put(fishes_vector, numpy.where(fishes_vector == -1), 6)
    fishes_vector = numpy.append(fishes_vector, numpy.full(fishes_to_add, 8))

print(len(fishes_vector))
