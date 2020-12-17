import copy
import itertools


def count_live_neighbors(x, y, z, layout):
    return sum(live(x+dx,y+dy,z+dz,layout) if (dx != 0 or dy != 0 or dz != 0) else 0 for dx,dy,dz in itertools.product([-1,0,1], repeat=3))

def live(x,y,z,layout):
    if x >= len(layout) or x < 0:
        return 0
    if y >= len(layout[x]) or y < 0:
        return 0
    if z >= len(layout[x][y]) or z < 0:
        return 0
    return 1 if layout[x][y][z] == '#' else 0

def prettyprint(layout):
    for layer in layout:
        print("LAYER")
        for string in layer:
            print(string)

with open("input.txt") as inp:
    layout = [[line.strip() for line in inp.readlines()]]



for n in range(6):
    empty_layer = ["."*len(layout[0][0])]*len(layout[0])

    layout.insert(0,empty_layer[:])
    layout.append(empty_layer[:])
    for layer in layout:
        layer.insert(0,'.'*len(empty_layer[0]))
        layer.append('.'*len(empty_layer[0]))
    for i,layer in enumerate(layout):
        for j,row in enumerate(layer):
            layout[i][j] = '.' + row + '.'

    new_layout = copy.deepcopy(layout)
    prettyprint(layout)
    for i,x in enumerate(new_layout):
        for j,y in enumerate(x):
            for k,z in enumerate(y):
                neighbors = count_live_neighbors(i,j,k,layout)
                if z == '#' and neighbors != 2 and neighbors != 3:
                    new_layout[i][j] = new_layout[i][j][:k] + '.' + new_layout[i][j][k+1:]
                elif z != '#' and neighbors == 3:
                    new_layout[i][j] = new_layout[i][j][:k] + '#' + new_layout[i][j][k+1:]
    
    layout = new_layout


print(sum(sum(y.count('#') for y in x) for x in layout))