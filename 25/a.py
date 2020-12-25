with open("input.txt") as inp:
    card_key = int(inp.readline())
    door_key = int(inp.readline())

# card_key == 7^x % 20201227
# door_key == 7^y % 20201227

# encryption_key == (7^x)^y % 20201227 == (7^y)^x % 20201227 == 7^(x*y) % 20201227

def transform(subject_number, loop_size):
    val = 1
    for _ in range(loop_size):
        val *= subject_number
        val = val % 20201227
    return val

def handshake(card_loop, door_loop):
    card_key = transform(7, card_loop)
    door_key = transform(7, door_loop)

    encryption_key = transform(card_key, door_loop)
    assert encryption_key == transform(door_key, card_loop)

    return encryption_key

#to calculate the inverse of x modulo n (from day 13)
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

def inverse_transform(public_key):
    exponent = 0
    seven_inverse = mod_inverse(7,20201227)
    reduced_key = public_key
    while reduced_key > 1:
        exponent += 1
        reduced_key *= seven_inverse
        reduced_key = reduced_key % 20201227
    return exponent


if __name__ == "__main__":
    card_loop = inverse_transform(card_key)
    encryption_key = transform(door_key, card_loop)
    print(encryption_key)