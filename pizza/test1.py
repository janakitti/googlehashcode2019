
IN_FILE = "problem_sets/b_small.in"
OUT_FILE = "output/" + IN_FILE[13:-3]

with open(IN_FILE, "r", errors="replace") as dataInput:
    # get the dimensions and stuffs of the data
    line = dataInput.readline().split()
    for i in range(len(line)):
        line[i] = int(line[i])

    h = line[0]  # height
    w = line[1]  # width
    each = line[2]  # min of each topping per slice
    max = line[3]  # maximum slice size
    pizza = []

    for i in range(h):
        pizza.append(dataInput.readline().rstrip())

    # the pizza in the list is [y][x] and not [x][y]


# output specification
# integer of total number of slices
# int1 int2 int3 int 4  -> x1, y1  x2, y2 coordinates of a slice, starts at 0
with open(OUT_FILE, "w", errors="replace") as dataOutput:
    pass
