with open("input.txt") as inp:
    program = [line.strip().split() for line in inp]

def update_mask(new_mask):
    update = {"ones" : 0, "zeros" : 2**37-1}
    for i,bit in enumerate(reversed(new_mask)):
        if bit =='X': continue
        elif bit == '1': update["ones"] += 2**i
        elif bit == '0': update["zero"] -= 2**i
    return update

mask = {"ones" : 0. "zeros" : 2**37-1}
mem_locations = {}
for line in program:
    command = line[0]
    if command == "mask":
        mask = update_mask(line[2])
    else:
        location = command[4:-1]
        entry = int(line[2])
        entry |= mask["ones"]
        entry &= mask["zeros"]
        mem_locations[location] = entry

print(sum(mem_locations[l] for l in mem_locations))