def valid_value(num, ranges):
    #print(num, ranges)
    #print(any(num >= r[0] and num <= r[1] for r in ranges))
    return any(num >= r[0] and num <= r[1] for r in ranges)

fields = {}
with open("input.txt") as inp:
    for i in range(20):
        line = inp.readline()
        rule = line.split(':')
        field = rule[0]
        ranges = [tuple(int(i) for i in rng.split('-')) for rng in rule[1].split(' or ')]
        fields[field] = ranges

    for i in range(5):
        inp.readline() # discard 5 lines of input

    invalid = 0
    for ticket in inp.readlines():
        values = [int(v) for v in ticket.split(',')]
        print(values)
        for v in values:
            if not any(valid_value(v, fields[f]) for f in fields):
                invalid += v
                break

    print(invalid)