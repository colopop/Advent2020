rules = {}
with open("input.txt") as inp:
    for line in inp.readlines():
        #  0     1      2       3         4     5     6       7         4    5     6
        #color color "bags" "contain" [(number color color "bags,")+ | "no other bags"]
        line = line.strip().split()
        color = line[0] + " " + line[1]
        rules[color] = []
        if line[4] == "no":
            continue
        else:
            rule = 0
            while rule * 4 + 4 < len(line):
                number = int(line[4+4*rule])
                rule_color = line[4+4*rule+1] + " " + line[4+4*rule+2]
                for _ in range(number):
                    rules[color].append(rule_color)
                rule += 1

def num_inside(container):
    return 1 + sum(num_inside(c) for c in rules[container])

print(num_inside("shiny gold") - 1)
