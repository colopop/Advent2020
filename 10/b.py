with open("input.txt") as inp:
    adapters = [int(i) for i in inp.readlines()]

adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()

#dynamic programming approach
WAYS = [0]*len(adapters)
WAYS[0] = 1
WAYS[1] = 1 if adapters[1] - adapters[0] <= 3 else 0
WAYS[2] = (WAYS[1] if adapters[2] - adapters[1] <= 3 else 0) + (WAYS[0] if adapters[2] - adapters[0] <= 3 else 0)

for i in range(3,len(adapters)):
    if adapters[i] - adapters[i-1] <= 3:
        WAYS[i] += WAYS[i-1]
    if adapters[i] - adapters[i-2] <= 3:
        WAYS[i] += WAYS[i-2]
    if adapters[i] - adapters[i-3] <= 3:
        WAYS[i] += WAYS[i-3]

print(WAYS[len(adapters)-1])