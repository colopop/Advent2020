with open("input.txt") as inp:
    cups = [int(i) for i in inp.readline().strip()]

offset = 0
for move in range(100):
    current_index = (move+offset) % len(cups)
    current_cup = cups[current_index]
    print(cups, move+1, current_index, current_cup, offset)
    picked_up = []
    picked_up.append(cups[(current_index+1)%len(cups)])
    picked_up.append(cups[(current_index+2)%len(cups)])
    picked_up.append(cups[(current_index+3)%len(cups)])
    print(picked_up)
    [cups.remove(i) for i in picked_up]
    print(cups)
    target_cup = current_cup-1
    while target_cup not in cups:
        target_cup = (target_cup-1)%(max(cups)+1)
    print(target_cup)

    cups = cups[:cups.index(target_cup)+1] + picked_up + cups[cups.index(target_cup)+1:]
    offset += cups.index(current_cup) - current_index

print("".join([str(i) for i in cups]))