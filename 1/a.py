with open("inp.txt") as inp:
   nums = [int(l) for l in inp.readlines()]

nums.sort()
lower = 0
upper = len(nums) - 1
while nums[lower] + nums[upper] != 2020:
   if nums[lower] + nums[upper] < 2020:
      lower += 1
   else:
      upper -= 1
print(lower, upper, nums[lower], nums[upper], nums[lower] * nums[upper])