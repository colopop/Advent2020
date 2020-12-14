buses = [29,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',41,'x','x','x','x','x','x','x','x','x',601,'x','x','x','x','x','x','x',23,'x','x','x','x',13,'x','x','x',17,'x',19,'x','x','x','x','x','x','x','x','x','x','x',463,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',37]

#what we want is
#t such that
#t % 29 == 0
#(t+19) % 41 == 0
#(t+29) % 601 == 0
#(t+37) % 23 == 0
#(t+42) % 13 == 0
#(t+46) % 17 == 0
#(t+48) % 19 == 0
#(t+60) % 463 == 0
#(t+97) % 37 == 0
#or
#t % 29 == 0
#t % 41 == -19
#t % 601 == -29
#t % 23 == -37
#t % 13 == -42
#t % 17 == -46
#t % 19 == -48
#t % 463 == -60
#t % 37 == -97
#a.k.a. Chinese remainder theorem

def check_validity(timestamp, buses):
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        else:
            if bus - (timestamp % bus) != i:
                return False
    return True

# timestamp = 0
# for i, bus in enumerate(buses[1:]):
#     if bus == 'x': continue
#     timestamp *= bus
#     timestamp += i
#     if check_validity(timestamp, buses):
#         break

for i,bus in enumerate(buses):
    if bus != 'x':
        print(bus-i,bus)

print(timestamp)
