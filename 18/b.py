with open("input.txt") as inp:
    homework = [("(" + line + ")").replace("(","( ").replace(")"," )").split() for line in inp.readlines()]

def solve_eqn(eqn):
    val = []
    op = [None]
    print(eqn)
    for token in eqn:
        if token == '+' or token == '*':
            op.append(token)
        elif token.isdigit():
            if op[-1] == '+':
                val[-1] += int(token)
                op.pop()
            else:
                val.append(int(token))
        elif token == '(':
            op.append(None)
        elif token == ')':
            while op[-1] is not None:
                if op[-1] == '*':
                    val[-2] *= val[-1]
                    val.pop()
                elif op[-1] == '+':
                    val[-2] += val[-1]
                    val.pop()
                else:
                    val[-2] =  val[-1]
                    val.pop()
                op.pop()
            op.pop()
            if op[-1] == '+':
                val[-2] += val[-1]
                val.pop()
                op.pop()
    return val.pop()

print(sum(solve_eqn(eqn) for eqn in homework))