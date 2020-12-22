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

def play_game(deck1, deck2):
    rounds = set([])
    while len(deck1) > 0 and len(deck2) > 0:

        if (tuple(deck1), tuple(deck2)) in rounds:
            return (0,deck1)
        else:
            rounds.add((tuple(deck1), tuple(deck2)))

        c1 = deck1.pop(0)
        c2 = deck2.pop(0)

        if c1 <= len(deck1) and c2 <= len(deck2):
            winner, deck = play_game(deck1[:c1], deck2[:c2])
            if winner == 0:
                deck1.append(c1)
                deck1.append(c2)
            else:
                deck2.append(c2)
                deck2.append(c1)
        else:
            if c1 > c2:
                deck1.append(c1)
                deck1.append(c2)
            else:
                deck2.append(c2)
                deck2.append(c1)

    return (0 if len(deck2) == 0 else 1, deck1 if len(deck2) == 0 else deck2)

def score(deck):
    ans = 0
    for i,card in enumerate(deck):
        ans += card * (len(deck) - i)
    return ans

print(score(play_game(deck1, deck2)[1]))