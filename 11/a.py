with open("input.txt") as inp:
    layout = [line.strip() for line in inp.readlines()]


def count_live_neighbors(row, col, layout):
    neighbors = 0
    if row > 0 and col > 0:
        if layout[row-1][col-1] == '#': neighbors += 1
    if row > 0:
        if layout[row-1][col] == '#': neighbors += 1
    if row > 0 and col < len(layout[0])-1:
        if layout[row-1][col+1] == '#': neighbors += 1
    if col > 0:
        if layout[row][col-1] == '#': neighbors += 1
    if col < len(layout[0])-1:
        if layout[row][col+1] == '#': neighbors += 1
    if row < len(layout)-1 and col > 0:
        if layout[row+1][col-1] == '#': neighbors += 1
    if row < len(layout)-1:
        if layout[row+1][col] == '#': neighbors += 1
    if row < len(layout)-1 and col < len(layout[0])-1:
        if layout[row+1][col+1] == '#': neighbors += 1
    return neighbors

def iterate(layout):
    new_layout = layout[:]
    for r, row in enumerate(layout):
        for c, seat in enumerate(row):
            if seat == 'L':
                if count_live_neighbors(r, c, layout) == 0:
                    new_layout[r] = new_layout[r][:c]+'#'+new_layout[r][c+1:]
            elif seat == '#':
                if count_live_neighbors(r,c,layout) > 3:
                    new_layout[r] = new_layout[r][:c]+'L'+new_layout[r][c+1:]
    return new_layout

new_layout = []
i=0
while 1:
    new_layout = iterate(layout)
    if layout == new_layout:
        break
    layout = new_layout[:]
    #for row in layout:
    #    print(row)
    #print("---")
    i+=1
for row in layout:
    print(row)
print(sum(row.count('#') for row in new_layout))