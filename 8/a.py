with open("input.txt") as inp:
    program = [(line.strip().split()[0], int(line.strip().split()[1])) for line in inp]

accumulator = 0
head = 0

def acc(arg):
    global accumulator
    global head
    accumulator += arg
    head += 1

def nop(arg):
    global head
    head += 1

def jmp(arg):
    global head
    head += arg

func_table = {"acc": acc,
              "nop": nop,
              "jmp": jmp}

#run program
already_run = set()
while head < len(program):
    if head in already_run:
        print(accumulator)
        break
    already_run.add(head)
    func = program[head][0]
    arg = program[head][1]
    func_table[func](arg)