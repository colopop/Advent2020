with open("inp.txt") as inp:
    nums = set()
    for line in inp.readlines():
        num = int(line)
        if 2020-num in nums:
            print(num * (2020-num))
            break
        else:
            nums.add(num)