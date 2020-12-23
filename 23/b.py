class LLNode(object):
    def __init__(self,value,before=None,after=None):
        self.value = value
        self.before = before
        self.after = after


with open("input.txt") as inp:
    cups = [LLNode(int(i)) for i in inp.readline().strip()]

#link em up
for i,cup in enumerate(cups):
    cup.before = cups[i-1]
    cup.after = cups[(i+1)%len(cups)]
head = cups[0]
tail = cups[-1]

tmp_max = max(c.value for c in cups)

for i in range(tmp_max+1, 1000001):
    new_node = LLNode(i, before=tail, after=head)
    tail.after = new_node
    cups.append(new_node)
    tail = new_node

cups = {c.value : c for c in cups}

MAX = max(cups)
MIN = min(cups)

for _ in range(10000000):

    #determine values to move
    value = head.value
    first = head.after
    second = first.after
    third = second.after

    #"remove" values
    head.after = third.after
    third.after.before = head

    #identify target
    target = (value-1) if value > MIN else MAX
    if target == first.value or target == second.value or target == third.value:
        target = (target-1) if target > 1 else MAX
    if target == first.value or target == second.value or target == third.value:
        target = (target-1) if target > MIN else MAX
    if target == first.value or target == second.value or target == third.value:
        target = (target-1) if target > MIN else MAX
    target_node = cups[target]

    #link up
    target_node.after.before = third
    third.after = target_node.after

    target_node.after = first
    first.before = target_node

    head = head.after

print(cups[1].after.value * cups[1].after.after.value)