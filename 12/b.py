with open("input.txt") as inp:
    inp = [(line.strip()[0], int(line.strip()[1:])) for line in inp.readlines()]

wp = (10,1)
loc = (0,0)

degrees_to_dir = {0 : 'E', 90 : 'N', 180: 'W', 270 : 'S'}

def move(direction, dist):
    if direction == 'E':
        return (dist, 0)
    if direction == 'W':
        return (-1*dist, 0)
    if direction == 'N':
        return (0, dist)
    if direction == 'S':
        return (0, -1*dist)

for d in inp:
    if d[0] == 'F':
        for _ in range(d[1]):
            loc = (loc[0] + wp[0], loc[1] + wp[1])
    elif d[0] == 'L':
        while d[1] > 0:
            wp = (-1*wp[1],wp[0])
            d = (d[0], d[1] - 90)
    elif d[0] == 'R':
        while d[1] > 0:
            wp = (wp[1],-1*wp[0])
            d = (d[0], d[1] - 90)
    else:
        mv = move(d[0], d[1])
        wp = (wp[0]+mv[0], wp[1]+mv[1])

print(abs(loc[0]) + abs(loc[1]))