with open("input.txt") as inp:
    adapters = [int(i) for i in inp.readlines()]

adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()
ones = 0
threes = 0
for i in range(1,len(adapters)):
    if adapters[i] - adapters[i-1] == 1:
        ones += 1
    elif adapters[i] - adapters[i-1] == 3:
        threes += 1
print(ones*threes)