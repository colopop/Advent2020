req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
import re

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
    print(passport)
    valid = "byr" in passport and int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002
    print(valid)
    valid = valid and "iyr" in passport and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020
    print(valid)
    valid = valid and "eyr" in passport and int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030
    print(valid)
    if "hgt" in passport:
        if passport["hgt"].strip()[-2:] == "in":
            valid = valid and int(passport["hgt"].strip()[:-2]) >= 59 and int(passport["hgt"].strip()[:-2]) <= 76
        elif passport["hgt"].strip()[-2:] == "cm":
            valid = valid and int(passport["hgt"].strip()[:-2]) >= 150 and int(passport["hgt"].strip()[:-2]) <= 193
        else:
            valid = False
    else:
        valid = False
    print(valid)
    valid = valid and "hcl" in passport and re.match(r"^#[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]$",passport["hcl"])
    print(valid)
    valid = valid and "ecl" in passport and (passport["ecl"] == "amb" or passport["ecl"] == "blu" or passport["ecl"] == "brn" or passport["ecl"] == "gry" or passport["ecl"] == "grn" or passport["ecl"] == "hzl" or passport["ecl"] == "oth")
    print(valid)
    valid = valid and "pid" in passport and re.match(r"^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$",passport["pid"])
    print(valid)
    if valid:
        num_valid += 1

print(num_valid)