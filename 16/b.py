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

    for i in range(2):
        inp.readline() # discard 2 lines of input

    my_ticket = [int(v) for v in inp.readline().split(',')]
   # print(my_ticket)

    for i in range(2):
        inp.readline() # discard 2 lines of input

    invalid = 0
    all_tickets = [my_ticket]
    for ticket in inp.readlines():
        values = [int(v) for v in ticket.split(',')]
        print(values)
        valid = True
        for v in values:
            if not any(valid_value(v, fields[f]) for f in fields):
                valid = False
                break
        if valid:
            all_tickets.append(values)

field_indices = {f : list(range(len(my_ticket))) for f in fields}

while any(len(field_indices[f]) > 1 for f in field_indices):
    print(field_indices)
    for f in field_indices:
        new_options = []
        for index in field_indices[f]:
            if all(valid_value(ticket[index], fields[f]) for ticket in all_tickets):
                new_options.append(index)
        field_indices[f] = new_options
        if len(new_options) == 1:
            for f2 in field_indices:
                if f == f2: continue
                if new_options[0] in field_indices[f2]:
                    field_indices[f2].remove(new_options[0])


print(my_ticket[field_indices['departure location'][0]]*my_ticket[field_indices['departure station'][0]]*my_ticket[field_indices['departure platform'][0]]*my_ticket[field_indices['departure track'][0]]*my_ticket[field_indices['departure date'][0]]*my_ticket[field_indices['departure time'][0]])