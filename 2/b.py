valid = 0
with open("input.txt") as inp:
    for line in inp.readlines():
        line = line.split()
        #format: [idx_1]-[idx_2] [letter]: [password]
        #input is 1-indexed
        idx_1 = int(line[0].split('-')[0]) - 1
        idx_2 = int(line[0].split('-')[1]) - 1
        letter = line[1][0]
        password = line[2]
        #password[idx_1] == letter XOR password[idx_2] == letter
        if (password[idx_1] == letter) != (password[idx_2] == letter):
            valid += 1
print(valid)