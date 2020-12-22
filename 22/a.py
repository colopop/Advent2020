deck1 = []
deck2 = []
with open("input.txt") as inp:
    inp.readline()
    for _ in range(25):
        deck1.append(int(inp.readline()))
    inp.readline()
    inp.readline()
    for _ in range(25):
        deck2.append(int(inp.readline()))

def score(deck):
    ans = 0
    for i,card in enumerate(deck):
        ans += card * (len(deck) - i)
    return ans

while len(deck1) > 0 and len(deck2) > 0:
    c1 = deck1.pop(0)
    c2 = deck2.pop(0)
    if c1 > c2:
        deck1.append(c1)
        deck1.append(c2)
    else:
        deck2.append(c2)
        deck2.append(c1)

print(max([score(deck1), score(deck2)]))