import copy
import itertools


def count_live_neighbors(w, x, y, z, layout):
    return sum(live(w+dw,x+dx,y+dy,z+dz,layout) if (dw != 0 or dx != 0 or dy != 0 or dz != 0) else 0 for dw,dx,dy,dz in itertools.product([-1,0,1], repeat=4))

def live(w, x,y,z,layout):
    if w >= len(layout) or w < 0:
        return 0
    if x >= len(layout[w]) or x < 0:
        return 0
    if y >= len(layout[w][x]) or y < 0:
        return 0
    if z >= len(layout[w][x][y]) or z < 0:
        return 0
    return 1 if layout[w][x][y][z] == '#' else 0

def prettyprint(layout):
    for layer in layout:
        print("LAYER")
        for sublayer in layer:
            print("SUBLAYER")
            for string in sublayer:
                print(string)

with open("input.txt") as inp:
    layout = [[[line.strip() for line in inp.readlines()]]]



for n in range(6):
    print(n)
    #prettyprint(layout)
    empty_layer = []
    for _ in range(len(layout)):
        empty_layer.append(["."*len(layout[0][0][0])]*len(layout[0][0]))
    layout.insert(0,copy.deepcopy(empty_layer))
    layout.append(copy.deepcopy(empty_layer))
    for layer in layout:
        layer.insert(0,copy.deepcopy(empty_layer[0]))
        layer.append(copy.deepcopy(empty_layer[0]))
    for layer in layout:
        for sublayer in layer:
            sublayer.insert(0,copy.deepcopy(empty_layer[0][0]))
            sublayer.append(copy.deepcopy(empty_layer[0][0]))
    for i,layer in enumerate(layout):
        for j,sublayer in enumerate(layer):
            for k,row in enumerate(sublayer):
                layout[i][j][k] = '.' + row + '.'

    new_layout = copy.deepcopy(layout)
    #prettyprint(layout)
    for i,w in enumerate(new_layout):
        #print("w {}", i)
        for j,x in enumerate(w):
            #print ("x {}", j)
            for k,y in enumerate(x):
                #print ("y {}", k)
                for l,z in enumerate(y):
                    neighbors = count_live_neighbors(i,j,k,l,layout)
                    if z == '#' and neighbors != 2 and neighbors != 3:
                        new_layout[i][j][k] = new_layout[i][j][k][:l] + '.' + new_layout[i][j][k][l+1:]
                    elif z != '#' and neighbors == 3:
                        new_layout[i][j][k] = new_layout[i][j][k][:l] + '#' + new_layout[i][j][k][l+1:]
    
    layout = new_layout


print(sum(sum(sum(y.count('#') for y in x) for x in w) for w in layout))