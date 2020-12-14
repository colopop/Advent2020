with open("input.txt") as inp:
    inp = [(line.strip()[0], int(line.strip()[1:])) for line in inp.readlines()]

facing = 0
distance = (0,0)

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
        d = (degrees_to_dir[facing], d[1])
    if d[0] == 'L':
        facing = (facing + d[1]) % 360
    elif d[0] == 'R':
        facing = (facing - d[1]) % 360
    else:
        mv = move(d[0], d[1])
        distance = (distance[0]+mv[0], distance[1]+mv[1])

print(abs(distance[0]) + abs(distance[1]))