import copy

mymap = []
f = open("input/i4.txt","r")
for line in f.readlines():
    mymap.append([x for x in line.strip()])


mm2 = copy.deepcopy(mymap)
positions = (-1,0,1)

def out_of_bouds(m,x,y):
    if x >= len(m[0]) or x < 0:
        return True
    if y >= len(m) or y < 0:
        return True
    return False


def solve1(mymap):
    counter = 0
    for x in range(0,len(mymap[0])):
        for y in range(0,len(mymap)):
            char = mymap[y][x]
            if (char == "."):
                continue

            ats = 0
            for px in positions:
                for py in positions:
                    if px == 0 and py == 0:
                        continue
                    nx = x + px
                    ny = y + py
                    if out_of_bouds(mymap,nx,ny):
                        continue

                    newchar = mymap[ny][nx]
                    if not(newchar == "."):
                        ats += 1
            if ats < 4:
                # print("hi2")
                mymap[y][x] = "X"

    for i in mymap:
        for j in i:
            if j == "X":
                counter+= 1
    return counter




def solve2(mymap):
    counter = 0  
    new_counter = solve1(mymap)
    while new_counter != 0:
        # print(new_counter)
        counter += new_counter
        for k,l in enumerate(mymap):
            l = ["." if x == "X" else x for x in l]
            mymap[k] = l
        new_counter = solve1(mymap)
    return counter

print(solve1(mymap))

print(solve2(mm2))
