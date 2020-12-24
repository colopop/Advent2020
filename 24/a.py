def get_next_direction(directions):
    if len(directions) == 0:
        return ('','')
    if len(directions) >= 2:
        if directions[:2] == 'nw':
            return ('ne', directions[1:])
        elif directions[:2] == 'se':
            return ('sw', directions[1:])
    if directions[0] == 'n' or directions[0] == 's':
        return (directions[:2], directions[2:])
    else:
        return (directions[:1], directions[1:])

def find_tile_coords(directions):
    coords = (0,0)
    while directions != "":
        nextdir, directions = get_next_direction(directions)
        if nextdir == 'e':
            coords = (coords[0]+1, coords[1])
        elif nextdir == 'ne':
            coords = (coords[0]+1, coords[1]+1)
        elif nextdir == 'w':
            coords = (coords[0]-1, coords[1])
        elif nextdir == 'sw':
            coords = (coords[0]-1, coords[1]-1)
    return coords


tiles = set()
with open("input.txt") as inp:
    for line in inp.readlines():
        coords = find_tile_coords(line.strip())
        if coords in tiles:
            tiles.remove(coords)
        else:
            tiles.add(coords)

print(len(tiles))