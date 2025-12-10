import math
f = open("input/i7.txt")

maze = [[c for c in l.strip()] for l in f.readlines()]

def solve1(maze):
    splits = 0
    for y,l in enumerate(maze):
        if y >= len(maze) - 1:
            continue
        for x,c in enumerate(l):
            if not(c == "S"):
                continue
            lower = maze[y+1][x]
            # print(c)
            if lower == "^":
                maze[y+1][x-1] = "S"
                maze[y+1][x+1] = "S"
                splits += 1
            else:
                maze[y+1][x] = "S"
    return splits

# wirklich schlechtes Design, listen mit int und chars miteinander vermischt.
# in der Liste wird gespeichert wieoft der Strahl schon splittet wurde
def solve2(maze):
    for y,l in enumerate(maze):
        if y >= len(maze) - 1:
            continue
        for x,c in enumerate(l):
            if not(isinstance(c, int)):
                continue
            lower = maze[y+1][x]
            # print(c)
            if lower == "^":
                maze[y+1][x-1] += c
                maze[y+1][x+1] += c
                
            else:
                maze[y+1][x] += c
    counter = 0
    for n in maze[-1]:
        # print(n)
        if isinstance(n, int):
            counter += n
    return counter


            

# print(maze)

# ungenutzt, rekursiv dauert viel zu lange
def solve_maze(y,x):
    # print(x)
    if y >= len(maze):
        return 0
    char = maze[y][x]
    if char == "^":
        return 1 + solve_maze(y+1,x-1) + solve_maze(y+1,x+1) 
    else:
        return solve_maze(y+1,x)
    
startpos = maze[0].index("S")

# print(startpos)
# print(solve_maze(0,startpos))

print(solve1(maze))


# for l in maze:
#     print("".join([str(i) for i in l]))


maze[0] = [1 if c == "S" else c for c in maze[0]]
for i in range(1,len(maze)):
    maze[i] = [0 if c == "S" else c for c in maze[i]]
solution = solve2(maze)
print(solution)

# for l in maze:
#     print("".join([str(i) for i in l]))