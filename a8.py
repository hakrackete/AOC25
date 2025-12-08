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

sortiert = sorted(distances_list, key=lambda x: x[2])
sortiert2 = sorted(sortiert[0:1000],key=lambda x: x[0])
print(len(sortiert))

cliques = []
for b1,b2,_ in sortiert2:
    cliques.append(set({b1,b2}))


def merge_clic2(clic):
    new_clic = []
    for i,c1 in enumerate(clic):
        for j, c2 in enumerate(clic,i):
            if not(c1.isdisjoint(c2)):
                c1.update(c2)
        if c1 not in new_clic:
            new_clic.append(c1)
    return new_clic

def solve1(cliques):
    prev_len = 0
    current_len = len(cliques)
    while prev_len != current_len:
        prev_len = current_len
        cliques = merge_clic2(cliques)
        current_len = len(cliques)
        print(current_len)

    # print(cliques)

    sorted_c = sorted(cliques,key = lambda x : len(x))
    # print(sorted_c)
    solution = len(sorted_c[-1]) * len(sorted_c[-2])* len(sorted_c[-3])
    print(f"solution part 1: {solution}")


solve1(cliques)
# print(circuits)

def solve2(circuits,sortiert):
    for a,b, _ in sortiert:
        # print(f"a: {a} b: {b}")
        # print(len(circuits))
        ca, cb = None,None
        for i, c in enumerate(circuits):
            # print(f"c: {c}")
            if a in c:
                ca = c
                break
        for c in circuits:
            # print(f"c: {c}")
            if b in c:
                cb = c
                break
        if cb == ca:
            continue
        ca.update(cb)
        circuits[i] = ca
        circuits.remove(cb)
        if len(circuits) == 1:
            solution = boxes[a][0] * boxes[b][0]
            print(f"solution part 2: {solution} ")
            break

def solve1_alternative(circuits,sortiert):
    for a,b, _ in sortiert[0:1000]:
        # print(f"a: {a} b: {b}")
        # print(len(circuits))
        ca, cb = None,None
        for i, c in enumerate(circuits):
            # print(f"c: {c}")
            if a in c:
                ca = c
                break
        for c in circuits:
            # print(f"c: {c}")
            if b in c:
                cb = c
                break
        if cb == ca:
            continue
        ca.update(cb)
        circuits[i] = ca
        circuits.remove(cb)
    sorted_c = sorted(circuits,key = lambda x : len(x))
    # print(sorted_c)
    solution = len(sorted_c[-1]) * len(sorted_c[-2])* len(sorted_c[-3])
    print(f"solution part 1 alternative: {solution}")

circuits = [set({x}) for x in range(0,1000)]
solve2(circuits,sortiert)

circuits = [set({x}) for x in range(0,1000)]
solve1_alternative(circuits,sortiert)