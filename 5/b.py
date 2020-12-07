with open("input.txt") as inp:
    passes = [line.strip() for line in inp.readlines()]


ROWS = 128
COLS = 8
spots = [False] * (127*8+7)

for bpass in passes:
    low = 0
    high = 127
    for i in range(7):
        new_bound = (low + high)//2
        if bpass[i] == "F":
            high = new_bound
        else:
            low = new_bound+1
        #print(low, high)
    row = low
    low = 0
    high = 7
    for i in range(7,10):
        new_bound = (low + high)//2
        if bpass[i] == "L":
            high = new_bound
        else:
            low = new_bound+1
        #print(bpass[i],low,high)
    seat = low
    spots[row*8+seat] = True
for row in range(ROWS):
    for col in range(COLS):
        if row > 10 and row < 115 and not spots[row*8+col]:
            print(row * 8 + col)