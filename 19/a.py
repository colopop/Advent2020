def ParseRule(string):
    if '"' in string:
        # letter rule
        return string.strip().replace('"','')
    else:
        ans = []
        for term in string.split(' | '):
            ans.append(tuple(int(i) for i in term.split()))
        return ans

def MatchStringToRule(string, rule, lookup):
    """Attempts to match a string to a rule. Returns the number of characters successfully matched."""
    if isinstance(lookup[rule], str):
        if string[0] == lookup[rule]:
            return 1
        else:
            return 0
    else:
        for term in lookup[rule]:
            consumable = string
            valid = True
            for subrule in term:
                match = MatchStringToRule(consumable, subrule, lookup)
                if not match:
                    valid = False
                    break
                else:
                    consumable = consumable[match:]
            if valid:
                return len(string) - len(consumable)
        return 0

rules = {}
messages = []
with open("input.txt") as inp:
    for _ in range(134):
        line = inp.readline()
        rules[int(line.split(": ")[0])] = (ParseRule(line.split(": ")[1]))
    inp.readline()
    for line in inp.readlines():
        messages.append(line.strip())

print(sum(MatchStringToRule(msg, 0, rules) == len(msg) for msg in messages))