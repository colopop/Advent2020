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
    """Attempts to match a string to a rule. There may be multiple valid matches; returns list of characters consumed by each match."""
    if isinstance(lookup[rule], str):
        if len(string) == 0:
            return []
        if string[0] == lookup[rule]:
            #print("match")
            return [1]
        else:
            return []
    else:
        matches = []
        for term in lookup[rule]:
            consumable = [string]
            valid = True
            for subrule in term:
                #print(subrule)
                new_consumable = []
                for c in consumable:
                    match = MatchStringToRule(c,subrule,lookup)
                    for m in match:
                        new_consumable.append(c[m:])
                consumable = new_consumable
            matches.extend([len(string) - len(c) for c in consumable])
        return matches


rules = {}
messages = []
with open("input.txt") as inp:
    for _ in range(134):
        line = inp.readline()
        rules[int(line.split(": ")[0])] = (ParseRule(line.split(": ")[1]))
    inp.readline()
    for line in inp.readlines():
        messages.append(line.strip())

rules[8]  = [(42,), (42,8)]
rules[11] = [(42,31), (42,11,31)]

print(sum(any(m == len(msg) for m in MatchStringToRule(msg,0,rules)) for msg in messages))