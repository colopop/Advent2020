with open("input.txt") as inp:
    numbers = [int(line.strip()) for line in inp.readlines()]

def is_valid(num, ls):
    for num2 in ls:
        if num - num2 in ls and num2 != num - num2:
            return True
    return False

def find_weakness(target, window, ls):
    for i in range(len(ls)):
        if sum(ls[i:i+window]) == target:
            return min(ls[i:i+window]) + max(ls[i:i+window])
    return None

for i in range(25,len(numbers)):
    if not is_valid(numbers[i], numbers[i-25:i]):
        target = numbers[i]
        break

window = 2
while 1:
    w = find_weakness(target, window, numbers)
    if w is not None:
        print(w)
        break
    else:
        window += 1