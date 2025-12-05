import re
from numpy import argmin
f = open("input/i5.txt","r")

ranges = []
lines = f.readlines()
for i,l in enumerate(lines):
    if l.strip() == "":
        break
    numbers = re.findall(r'\d+', l.strip())
    r = (int(numbers[0]),int(numbers[1]))
    ranges.append(r)

# print(ranges)
ids =  [int(x.strip()) for x in lines[i+1:]]

valid_ids = []
for myid in ids:
    for r in ranges:
        if myid >= r[0] and myid <= r[1]:
            valid_ids.append(myid)
            break
    if myid in valid_ids:
        continue


        
zeiger = 0
in_range = False
up, low = 0,0

counter = 0


remaining = ranges

while remaining:
    print(f"zeiger: {zeiger} counter: {counter}")
    if not(in_range):
        index = argmin([t[0] for t in remaining])
        low = remaining[index][0]
        up = remaining[index][1]

        # print(remaining[index])

        # hier noch extra +1 rechnen, weil:
            # bei up-low wird die momentane ID nicht mitgezählt
        counter += (up-low) +1

        zeiger = remaining[index][1]
        in_range = True
        remaining.pop(index)
    else:
        valids = [t for t in remaining if t[0] >= low and t[0] <= up]
        if valids:
            index = argmin([t[0] for t in valids])
            low = valids[index][0]
            up = valids[index][1]

            counter += (up-zeiger)
            zeiger = valids[index][1]
            in_range = True
            remaining.remove(valids[index])
        else:
            in_range = False
    remaining = [t for t in remaining if t[1] > zeiger]

print(f"solution part 1: {len(valid_ids)} \n p2: {counter}")
