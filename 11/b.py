with open("input.txt") as inp:
    layout = [line.strip() for line in inp.readlines()]

def find_seat(startrow, startcol, dr, dc, layout):
    if dr == 0 and dc == 0: return 0
    look_at_row = startrow+dr
    look_at_col = startcol+dc
    while look_at_row >= 0 and look_at_row < len(layout) and look_at_col >= 0 and look_at_col < len(layout[0]):
        if layout[look_at_row][look_at_col] == '#':
            return 1
        if layout[look_at_row][look_at_col] == 'L':
            return 0
        look_at_row += dr
        look_at_col += dc
    return 0

def count_live_neighbors(row, col, layout):
    return sum(find_seat(row, col, dr, dc, layout) for dr,dc in zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]))


def iterate(layout):
    new_layout = layout[:]
    for r, row in enumerate(layout):
        for c, seat in enumerate(row):
            if seat == 'L':
                if count_live_neighbors(r, c, layout) == 0:
                    new_layout[r] = new_layout[r][:c]+'#'+new_layout[r][c+1:]
            elif seat == '#':
                if count_live_neighbors(r,c,layout) > 4:
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