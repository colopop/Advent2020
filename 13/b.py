with open("input.txt") as inp:
    earliest = int(inp.readline())
    buses = [b for b in inp.readline().split(',')]

#to calculate the inverse of x modulo n
def mod_inverse(x, n):
    def ext_euclid(a, b, p0, p1, n):
        q = a // b
        r = a % b
        if r == 0:
            if b != 1:
                raise ValueError("Value is not invertible.")
            return p1
        else:
            p_next = (p0 - p1*q) % n
            return ext_euclid(b, r, p1, p_next, n)

    if x > n:
        x = x % n
    return ext_euclid(n, x, 0, 1, n)

#solve an instance of the Chinese Remainder Theorem
#constraints must be of the form [(residue1, mod1), (residue2, mod2), ...]
def solve_CRT(constraints):
    if len(constraints) == 0:
        return 0
    elif len(constraints) == 1:
        return constraints[0][0] % constraints[0][1]
    else:
        mod_prod = 1
        for c in constraints:
            mod_prod *= c[1]

        return sum(residue * (mod_prod//mod) * mod_inverse(mod_prod//mod, mod) for residue,mod in constraints) % mod_prod

#what we want is t such that
#t % 29 == 0
#(t+19) % 41 == 0
#(t+29) % 601 == 0
#(t+37) % 23 == 0
#(t+42) % 13 == 0
#(t+46) % 17 == 0
#(t+48) % 19 == 0
#(t+60) % 463 == 0
#(t+97) % 37 == 0
#or
#t % 29 == 0
#t % 41 == -19
#t % 601 == -29
#t % 23 == -37
#t % 13 == -42
#t % 17 == -46
#t % 19 == -48
#t % 463 == -60
#t % 37 == -97
#a.k.a. Chinese remainder theorem
print(solve_CRT([(-1*index, int(bus_val)) for index,bus_val in enumerate(buses) if bus_val.isdigit()]))
