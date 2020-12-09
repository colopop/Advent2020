with open("input.txt") as inp:
    numbers = [int(line.strip()) for line in inp.readlines()]

def is_valid(num, ls):
    for num2 in ls:
        if num - num2 in ls and num2 != num - num2:
            return True
    return False

for i in range(25,len(numbers)):
    if not is_valid(numbers[i], numbers[i-25:i]):
        print(numbers[i])
