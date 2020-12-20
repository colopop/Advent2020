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

    def get_borders(self):
        top_border = self.data[0]
        left_border = "".join([line[0] for line in self.data])
        right_border = "".join([line[-1] for line in self.data])
        bottom_border = self.data[-1]
        return [top_border, bottom_border, left_border, right_border]

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

ans = 1
for tile in tiles:
    if tile.edge.count(False) == 2:
        ans *= tile.id
print(ans)