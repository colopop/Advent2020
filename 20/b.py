class Tile(object):
    def __init__(self, t_string):
        info = t_string.split('\n')
        self.id = int(info[0].split()[1][:-1])
        self.data = []
        for line in info[1:]:
            if line.strip() != '':
                self.data.append(line.strip())
        #neighbors: top, bottom, left, right
        self.edge = [False]*4
        self.borders = self.get_borders()
        self.frozen = False

    def get_borders(self):
        top_border = self.data[0]
        left_border = "".join([line[0] for line in self.data])
        right_border = "".join([line[-1] for line in self.data])
        bottom_border = self.data[-1]
        return [top_border, bottom_border, left_border, right_border]

    def flip(self, axis):
        if self.frozen: return
        tmp = self.edge[:]
        if axis == 'v':
            old_data = self.data[:]
            self.data = [row[::-1] for row in old_data]
            self.edge[2] = tmp[3]
            self.edge[3] = tmp[2]
        elif axis == 'h':
            self.data = self.data[::-1]
            self.edge[0] = tmp[1]
            self.edge[1] = tmp[0]
        self.borders = self.get_borders()

    def rotate90(self):
        if self.frozen: return
        old_data = self.data[:]
        for i in range(len(self.data)):
            self.data[i] = "".join([line[-1*(i+1)] for line in old_data])
        self.borders = self.get_borders()
        tmp = self.edge[:]
        self.edge[0] = tmp[3]
        self.edge[1] = tmp[2]
        self.edge[2] = tmp[0]
        self.edge[3] = tmp[1]

    def freeze(self):
        self.frozen = True

    def strip_border(self):
        self.data = self.data[1:-1]
        for i,row in enumerate(self.data):
            self.data[i] = row[1:-1]

    def printdata(self):
        print(self.id)
        for row in self.data:
            print(row)

def prettyprint(pic):
    print('')
    for row in pic:
        for i in range(10):
            print( " ".join( [tile.data[i] if tile is not None else "~"*10 for tile in row] ) )
        print('')

def prettyprint_stripped(pic):
    for row in pic:
        for i in range(8):
            print( "".join( [tile.data[i] if tile is not None else "~"*8 for tile in row] ) )

def prettyprint_joined(pic):
    for row in pic:
        print(row)

def join_pic(pic):
    new_pic = []
    for i,row in enumerate(pic):
        for j in range(8):
            new_pic.append( "".join( [tile.data[j] for tile in row] ) )
    return new_pic

with open("input.txt") as inp:
    inp = inp.read().split("\n\n")

tiles = []
for tile in inp:
    new_tile = Tile(tile)
    tiles.append(new_tile)

for tile in tiles:
    for i,border in enumerate(tile.borders):
        found = False
        for tile2 in tiles:
            if tile.id == tile2.id: continue
            for j,border2 in enumerate(tile2.borders):
                if border == border2 or border == border2[::-1]:
                    found = True
        tile.edge[i] = found

picture = []
for row in range(12):
    picture.append([None]*12)

corners = []
edges = []
for tile in tiles:
    if tile.edge.count(False) == 2:
        corners.append(tile)
    if tile.edge.count(False) == 1:
        edges.append(tile)

#build the frame
#pick top left corner
while corners[0].edge[0] or corners[0].edge[2]:
    corners[0].rotate90()
    corners[0].freeze()
picture[0][0] = corners[0]
#build down
for i in range(10):
    border = picture[i][0].borders[1]
    for tile in edges:
        if tile.frozen: continue
        while tile.edge[2]:
            tile.rotate90()
        if tile.borders[0] != border:
            tile.flip('v')
            tile.rotate90()
            tile.rotate90()
        if tile.borders[0] == border:
            picture[i+1][0] = tile
            tile.freeze()
            break
#find bottom left corner
border = picture[10][0].borders[1]
for tile in corners:
    if tile.frozen: continue
    while tile.edge[1] or tile.edge[2]:
        tile.rotate90()
    if tile.borders[0] != border:
            tile.flip('v')
            tile.rotate90()
            tile.rotate90()
            tile.rotate90()
    if tile.borders[0] == border:
        picture[11][0] = tile
        tile.freeze()
        break
#build right
for i in range(10):
    border = picture[11][i].borders[3]
    for tile in edges:
        if tile.frozen: continue
        while tile.edge[1]:
            tile.rotate90()
        if tile.borders[2] != border:
            tile.flip('h')
            tile.rotate90()
            tile.rotate90()
        if tile.borders[2] == border:
            picture[11][i+1] = tile
            tile.freeze()
            break
#find bottom right corner
border = picture[11][10].borders[3]
for tile in corners:
    if tile.frozen: continue
    while tile.edge[1] or tile.edge[3]:
        tile.rotate90()
    if tile.borders[2] != border:
            tile.flip('h')
            tile.rotate90()
            tile.rotate90()
            tile.rotate90()
    if tile.borders[2] == border:
        picture[11][11] = tile
        tile.freeze()
        break
#build up
for i in range(1,11):
    border = picture[12-i][11].borders[0]
    for tile in edges:
        if tile.frozen: continue
        while tile.edge[3]:
            tile.rotate90()
        if tile.borders[1] != border:
            tile.flip('v')
            tile.rotate90()
            tile.rotate90()
        if tile.borders[1] == border:
            picture[11-i][11] = tile
            tile.freeze()
            break
#find top right corner
border = picture[1][11].borders[0]
for tile in corners:
    if tile.frozen: continue
    while tile.edge[0] or tile.edge[3]:
        tile.rotate90()
    if tile.borders[1] != border:
            tile.flip('h')
            tile.rotate90()
    picture[0][11] = tile
    tile.freeze()
#build left
for i in range(1,11):
    border = picture[0][12-i].borders[2]
    for tile in edges:
        if tile.frozen: continue
        while tile.edge[0]:
            tile.rotate90()
        if tile.borders[3] != border:
            tile.flip('h')
            tile.rotate90()
            tile.rotate90()
        if tile.borders[3] == border:
            picture[0][11-i] = tile
            tile.freeze()
            break
#fill middle left to right
for i in range(1,11):
    for j in range(1,11):
        border = picture[i][j-1].borders[3]
        try:
            for tile in tiles:
                if tile.frozen: continue
                #check borders one by one
                for _ in range(4):
                    if tile.borders[2] == border:
                        picture[i][j] = tile
                        tile.freeze()
                        raise StopIteration
                    tile.flip('h')
                    if tile.borders[2] == border:
                        picture[i][j] = tile
                        tile.freeze()
                        raise StopIteration
                    tile.flip('h')
                    tile.rotate90()
        except StopIteration:
            continue
#strip borders
for row in picture:
    for tile in row:
        tile.strip_border()

#now we look for sea monsters...
import re
SEA_MONSTER1 = re.compile("..................#.")
SEA_MONSTER2 = re.compile("#....##....##....###")
SEA_MONSTER3 = re.compile(".#..#..#..#..#..#...")

SEA_MONSTER_REPLACEMENT1 = "..................O."
SEA_MONSTER_REPLACEMENT2 = "O....OO....OO....OOO"
SEA_MONSTER_REPLACEMENT3 = ".O..O..O..O..O..O..."

#make the picture a little more convenient for sea monster searches. we need 8 configurations to search through
picture = join_pic(picture)
picture90 = []
for i in range(len(picture)):
    picture90.append( "".join([line[-1*(i+1)] for line in picture]) )
picture180 = []
for i in range(len(picture90)):
    picture180.append( "".join([line[-1*(i+1)] for line in picture90]) )
picture270 = []
for i in range(len(picture)):
    picture270.append( "".join([line[-1*(i+1)] for line in picture180]) )
flipped = [row[::-1] for row in picture]
flipped90 = []
for i in range(len(flipped)):
    flipped90.append( "".join([line[-1*(i+1)] for line in flipped]) )
flipped180 = []
for i in range(len(picture90)):
    flipped180.append( "".join([line[-1*(i+1)] for line in flipped90]) )
flipped270 = []
for i in range(len(picture)):
    flipped270.append( "".join([line[-1*(i+1)] for line in flipped180]) )

for pic in [picture, picture90, picture180, picture270, flipped, flipped90, flipped180, flipped270]:
    new_pic = pic[:]
    for i in range(len(pic)-3):
        for j in range(len(pic[i])-len(SEA_MONSTER_REPLACEMENT1)):
            if re.match(SEA_MONSTER1, pic[i][j:j+len(SEA_MONSTER_REPLACEMENT1)]) and re.match(SEA_MONSTER2, pic[i+1][j:j+len(SEA_MONSTER_REPLACEMENT2)]) and re.match(SEA_MONSTER3, pic[i+2][j:j+len(SEA_MONSTER_REPLACEMENT3)]):
                tmp = list(new_pic[i])
                for k, c in enumerate(SEA_MONSTER_REPLACEMENT1):
                    if c == 'O':
                        tmp[j+k] = 'O'
                new_pic[i] = ''.join(tmp)
                tmp = list(new_pic[i+1])
                for k, c in enumerate(SEA_MONSTER_REPLACEMENT2):
                    if c == 'O':
                        tmp[j+k] = 'O'
                new_pic[i+1] = ''.join(tmp)
                tmp = list(new_pic[i+2])
                for k, c in enumerate(SEA_MONSTER_REPLACEMENT3):
                    if c == 'O':
                        tmp[j+k] = 'O'
                new_pic[i+2] = ''.join(tmp)
    if new_pic != pic:
        print(sum(row.count('#') for row in new_pic))