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

def get_neighbors(coord):
    return [(coord[0]+1,coord[1]),   #east
            (coord[0]+1,coord[1]+1), #northeast
            (coord[0],coord[1]+1),   #northwest
            (coord[0]-1,coord[1]),   #west
            (coord[0]-1,coord[1]-1), #southwest
            (coord[0],coord[1]-1)]   #southeast

def count_neighbors(coord, tiles):
    return sum(1 if t in tiles else 0 for t in get_neighbors(coord))

def next_iteration(tiles):
    new_tiles = tiles.copy()
    for tile in tiles:
        neighbors = count_neighbors(tile, tiles)
        if neighbors == 0 or neighbors > 2:
            new_tiles.remove(tile)
        for neighbor in get_neighbors(tile):
            if neighbor not in tiles:
                if count_neighbors(neighbor, tiles) == 2:
                    new_tiles.add(neighbor)
    return new_tiles

tiles = set()
with open("input.txt") as inp:
    for line in inp.readlines():
        coords = find_tile_coords(line.strip())
        if coords in tiles:
            tiles.remove(coords)
        else:
            tiles.add(coords)

for i in range(100):
    print(i, len(tiles))
    tiles = next_iteration(tiles)

print(len(tiles))