with open("inp.txt") as inp:
    nums = [int(l) for l in inp.readlines()]
nums.sort()

#pick an i to hold constant, then run same algorithm as previous
for i in range(len(nums)):
    target = 2020 - nums[i]
    lower = i
    upper = len(nums) - 1
    while lower < upper:
        if nums[lower] + nums[upper] < target:
            lower += 1
        elif nums[lower] + nums[upper] > target:
            upper -= 1
        else:
            #found correct configuration
            break
    if nums[lower] + nums[upper] == target:
        print(i, lower, upper, nums[i], nums[lower], nums[upper], nums[i]*nums[lower]*nums[upper])
        break