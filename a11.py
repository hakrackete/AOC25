f = open("input/i11.txt")

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

vistited_nodes = set()

result = DFS(vistited_nodes,"svr")
print(f"result: {result}")

    
