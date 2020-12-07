groups = []
with open("input.txt") as inp:
    group = 0
    groups.append(set([]))
    for line in inp.readlines():
        line = line.strip()
        if line == "":
            group += 1
            groups.append(set([]))
        for char in line:
            groups[group].add(char)

ans = 0
for g in groups:
    ans += len(g)
print(ans)