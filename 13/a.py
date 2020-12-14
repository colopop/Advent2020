with open("input.txt") as inp:
    earliest = int(inp.readline())
    buses = [int(b) for b in inp.readline().split(',') if b.isdigit()]

min_bus = min(buses, key=lambda x: (x - earliest % x) )
print(min_bus * (min_bus - (earliest % min_bus)))