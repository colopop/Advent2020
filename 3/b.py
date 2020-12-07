def count_trees(dx, dy, field):
    trees = 0
    x = 0
    y = 0
    while y < len(field):
        if field[y][x] == '#':
            trees += 1
        x = (x + dx) % len(field[0])
        y = y + dy
    return trees

input_field = []
with open("input.txt") as inp:
    input_field = [line.strip() for line in inp.readlines()]

trees31 = count_trees(3,1,input_field)

trees11 = count_trees(1,1,input_field)

trees51 = count_trees(5,1,input_field)

trees71 = count_trees(7,1,input_field)

trees12 = count_trees(1,2,input_field)

print(trees11*trees31*trees51*trees71*trees12)