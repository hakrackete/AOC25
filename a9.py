import math
f = open("input/i9.txt")

carpets = []
for l in f.readlines():
    t = tuple([int(i) for i in l.split(",")])
    carpets.append(t)

print(carpets)

max_size = 0
for i, (x1,y1) in enumerate(carpets):
    for j, (x2,y2) in enumerate(carpets,i):
        dx = abs(x1-x2) + 1
        dy = abs(y1-y2) + 1 
        size = dx * dy
        # print(size)
        if size > max_size:
            max_size = size
print(max_size)
