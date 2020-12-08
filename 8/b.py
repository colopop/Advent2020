with open("input.txt") as inp:
    original = [(line.strip().split()[0], int(line.strip().split()[1])) for line in inp]

def run_program(program):
    accumulator = 0
    head = 0

    def acc(arg):
        nonlocal accumulator
        nonlocal head
        accumulator += arg
        head += 1

    def nop(arg):
        nonlocal head
        head += 1

    def jmp(arg):
        nonlocal head
        head += arg

    func_table = {"acc": acc,
                  "nop": nop,
                  "jmp": jmp}

    #run program
    already_run = set()
    while head < len(program):
        if head in already_run:
            return -1 #this program loops infinitely
        already_run.add(head)
        func = program[head][0]
        arg = program[head][1]
        func_table[func](arg)

    return accumulator

#try changing each jmp or nop until getting the right answer
for instruction in range(len(original)):
    if original[instruction][0] == "jmp":
        copy = original[:]
        copy[instruction] = ("nop", original[instruction][1])
    elif original[instruction][0] == "nop":
        copy = original[:]
        copy[instruction] = ("jmp", original[instruction][1])
    else:
        continue
    result = run_program(copy)
    if result == -1:
        continue # we failed
    else:
        print(result)
        break