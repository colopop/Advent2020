with open("inp.txt") as inp:
    nums = set([int(l) for l in inp.readlines()])

#pick an i to hold constant, then run same algorithm as previous
for i in nums:
    target = 2020 - i
    found = False
    for j in nums:
        if i == j: continue
        if target - j in nums:
            print(i*j*(2020-i-j))
            found = True
            break
    if found:
        break