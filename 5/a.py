with open("input.txt") as inp:
    passes = [line.strip() for line in inp.readlines()]


highest_id = 0
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
    s_id = row*8 + seat
    highest_id = max(highest_id, s_id)
    #print(row, seat, s_id)
print(highest_id)