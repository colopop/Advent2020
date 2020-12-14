earliest = 1002460
buses = [29,41,601,23,13,17,19,463,37]

min_bus = min(buses, key=lambda x: (x - earliest % x) )
print(min_bus * (min_bus - (earliest % min_bus)))