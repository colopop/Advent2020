with open("input.txt") as inp:
    homework = [line.replace("(","( ").replace(")"," )").split() for line in inp.readlines()]

def solve_eqn(eqn):
    val = [None]
    op = [None]
    print(eqn)
    for token in eqn:
        print(token)
        if token == '+' or token == '*':
            op.append(token)
        elif token.isdigit():
            if op[-1] == '+':
                val[-1] += int(token)
            elif op[-1] == '*':
                val[-1] *= int(token)
            else:
                val[-1] = (int(token))
            op.pop()
        elif token == '(':
            op.append(None)
            val.append(None)
        elif token == ')':
            if op[-1] == '+':
                val[-2] += val[-1]
                val.pop()
            elif op[-1] == '*':
                val[-2] *= val[-1]
                val.pop()
            else:
                val[-2] =  val[-1]
                val.pop()
            op.pop()
        print(val)
        print(op)
    return val.pop()

print(sum(solve_eqn(eqn) for eqn in homework))