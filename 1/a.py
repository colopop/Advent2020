with open("inp.txt") as inp:
   nums = set([int(l) for l in inp.readlines()])

for num in nums:
    if (2020 - num) in nums:
        print(num * (2020 - num))
        break