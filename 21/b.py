options = {}
with open("input.txt") as inp:
    for line in inp.readlines():
        line = line.split('(')
        ingredients = frozenset(line[0].split())
        allergens = line[1].replace(')','').replace('contains ','').replace(',','').split()
        for allergen in allergens:
            if allergen in options:
                options[allergen] &= ingredients
            else:
                options[allergen] = ingredients

while any(len(options[allergen]) > 1 for allergen in options):
    for allergen in options:
        if len(options[allergen]) == 1:
            for other_allergen in options:
                if allergen == other_allergen: continue
                options[other_allergen] -= options[allergen]

#all ingredients should be isolated
canonical_list = ",".join(list(options[allergen])[0] for allergen in sorted(options))
print(canonical_list)