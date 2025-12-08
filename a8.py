import math
f = open("input/i8.txt")

boxes = []
for l in f.readlines():
    t = tuple([int(i) for i in l.split(",")])
    boxes.append(t)

def box_dist(b1,b2):
    return math.dist(b1,b2)

print(box_dist(boxes[0],boxes[1]))

distances = {}
for i in range(0,len(boxes)-1):
    for j in range(i+1,len(boxes)):
        distances[(i,j)] = box_dist(boxes[i],boxes[j])

print(distances)

