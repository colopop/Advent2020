with open("input.txt") as inp:
    program = [line.strip().split() for line in inp]

def get_locations(original, mask):
    original = bin(original)[2:].zfill(36)
    locations = [original]
    for i,bit in enumerate(mask):
        if bit == '1':
            for j,loc in enumerate(locations):
                locations[j] = loc[:i] + '1' + loc[i+1:]
        elif bit == 'X':
            new_locations = []
            for loc in locations:
                new_locations.append(loc[:i]+'0'+loc[i+1:])
                new_locations.append(loc[:i]+'1'+loc[i+1:])
            locations = new_locations
    return [int(loc, 2) for loc in locations] 


mem_locations = {}
for line in program:
    command = line[0]
    if command == "mask":
        mask = line[2]
    else:
        location =int(command[4:-1])
        write_to = get_locations(location, mask)
        entry = int(line[2])
        for loc in write_to:
            mem_locations[loc] = entry

print(sum(mem_locations[l] for l in mem_locations))