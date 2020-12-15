with open("input.txt") as inp:
    ages = [int(num)for num in inp.readline().split(',')]

seed = ages[-1]
ages = ages[:-1]
ages = {num : idx for idx,num in enumerate(ages)}

for i in range(6,30000000):
    old_seed = seed
   # print(seed)
    if seed in ages:
        new_seed = i - ages[seed]
        ages[seed] = i
        seed = new_seed
    else:
        ages[seed] = i
        seed = 0

print(old_seed)