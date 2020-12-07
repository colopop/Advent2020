req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open("input.txt") as inp:
    passports = []
    current_pp = {}
    for line in inp.readlines():
        if line.strip() == "":
            if len(current_pp) > 0:
                passports.append(current_pp)
            current_pp = {}
        for entry in line.split():
            splt = entry.split(":")
            current_pp[splt[0]] = splt[1]

num_valid = 0
for passport in passports:
    valid = True
    for field in req_fields:
        if field not in passport:
            print(field, passport)
            valid = False
            break
    if valid:
        num_valid += 1

print(num_valid)