options = {}
food_lists = []
all_ingredients = set([])
with open("input.txt") as inp:
    for line in inp.readlines():
        line = line.split('(')
        ingredients = frozenset(line[0].split())
        food_lists.append(ingredients)
        all_ingredients |= ingredients
        allergens = line[1].replace(')','').replace('contains ','').replace(',','').split()
        for allergen in allergens:
            if allergen in options:
                options[allergen] &= ingredients
            else:
                options[allergen] = ingredients

ans = 0
for ingredient in all_ingredients:
    try:
        for option in options:
            if ingredient in options[option]:
                raise StopIteration
        #this ingredient cannot be an allergen
        appearances = 0
        for food in food_lists:
            if ingredient in food:
                appearances += 1
        ans += appearances
    except StopIteration:
        continue
print(ans)