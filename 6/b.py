from collections import Counter
groups = []
nums = []
with open("input.txt") as inp:
    group = 0
    num_in_group = 0
    groups.append(Counter())
    nums.append(0)
    for line in inp.readlines():
        line = line.strip()
        if line == "":
            nums.append(0)
            group += 1
            groups.append(Counter())
            continue
        nums[group] += 1
        for char in line:
            groups[group][char] += 1

ans = 0
for i in range(len(groups)):
    for q in groups[i]:
        if groups[i][q] == nums[i]:
            ans += 1
print(ans)