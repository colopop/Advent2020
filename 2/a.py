valid = 0
with open("input.txt") as inp:
    for line in inp.readlines():
        line = line.split()
        #format: [lower]-[upper] [letter]: [password]
        lower = int(line[0].split('-')[0])
        upper = int(line[0].split('-')[1])
        letter = line[1][0]
        count = line[2].count(letter)
        if count >= lower and count <= upper:
            valid += 1
print(valid)