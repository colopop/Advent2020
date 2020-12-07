rules = {}
with open("input.txt") as inp:
    for line in inp.readlines():
        #  0     1      2       3         4     5     6       7         4    5     6
        #color color "bags" "contain" [number color color "bags,"]* | "no other bags"
        line = line.strip().split()
        color = line[0] + " " + line[1]
        rules[color] = []
        if line[4] == "no":
            continue
        else:
            rule = 0
            while rule * 4 + 4 < len(line):
                number = int(line[4+4*rule]) #ignored for puzzle 1
                rule_color = line[4+4*rule+1] + " " + line[4+4*rule+2]
                rules[color].append(rule_color)
                rule += 1

def can_fit(container, item):
    if item in rules[container]:
        return 1
    elif any(can_fit(c, item) for c in rules[container]):
        return 1
    else:
        return 0

print(sum(can_fit(c, "shiny gold") for c in rules))