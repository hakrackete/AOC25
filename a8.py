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
distances_list = []
for i in range(0,len(boxes)-1):
    for j in range(i+1,len(boxes)):
        distances[(i,j)] = box_dist(boxes[i],boxes[j])
        distances_list.append((i,j,box_dist(boxes[i],boxes[j])))

sortiert = sorted(distances_list, key=lambda x: x[2])[0:1000]
sortiert2 = sorted(sortiert,key=lambda x: x[0])
print(len(sortiert))

cliques = []
for b1,b2,_ in sortiert2:
    added = False
    for c in cliques:
        if (b1 in c) or (b2 in c) :
            c.add(b1)
            c.add(b2)
            added = True
            break
    if not(added):
        cliques.append(set({b1,b2}))

def merge_clic(clic):
    new_clic = []
    for i,c1 in enumerate(clic):
        added = False
        for j, c2 in enumerate(clic,i):
            if not(c1.isdisjoint(c2)) and not(c1 <= c2):
                new_clic.append(c1.union(c2))
                added = True
                break
        if not(added):
            new_clic.append(c1)
    return new_clic

for i in range(3):
    print(len(cliques))
    cliques = merge_clic(cliques)

# print(cliques)

            



sorted_c = sorted(cliques,key = lambda x : len(x))
print(len(sorted_c[-1]) * len(sorted_c[-2])* len(sorted_c[-3]))
