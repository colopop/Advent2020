field = []
with open("input.txt") as inp:
    field = [line.strip() for line in inp.readlines()]

trees = 0
x = 0
y = 0
while y < len(field):
    if field[y][x] == '#':
        trees += 1
    x = (x + 3) % len(field[0])
    y = y + 1

print(trees)