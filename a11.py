f = open("input/i11_test.txt")

# idee: DFS:
nodes = {}
for l in f.readlines():
    label = l[0:3]
    neighbors = [c for c in l[5:-1].split(" ")]
    nodes[label] = neighbors

print(len(nodes))


def DFS(visited,current):

    if current == "out":
        return 1
    elif current in visited:
        return 0
    else:
        visited.add(current)
        counter = 0
        for n in nodes[current]:
            counter += DFS(visited,n)
        visited.remove(current)
        return counter
    
def DFS2(visited,current,targets,exclude):
    if current in targets:
        print(visited)
        print(current)
        return 1
    elif current in visited:
        return 0
    elif current in exclude:
        return 0
    else:
        visited.add(current)
        counter = 0
        for n in nodes[current]:
            counter += DFS2(visited,n,targets,exclude)
        visited.remove(current)
        return counter

def solve1():
    vistited_nodes = set()
    result = DFS(vistited_nodes,"you")
    print(f"result: {result}")
# solve1()

vistited_nodes = set()
start = "svr"
targets = set({"fft","dda"})
exclude = set({"out"})
result = DFS2(vistited_nodes,start,targets,exclude)
print(result)

    
