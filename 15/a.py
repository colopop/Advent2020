with open("input.txt") as inp:
    ages = [int(num)for num in inp.readline().split(',')]


for i in range(2020-7):
    print(ages[-1])
    if ages[-1] in ages[:-1]:
        ages.append(list(reversed(ages[:-1])).index(ages[-1])+1)
    else:
        ages.append(0)

print(ages[-1])