f = open("input/i10.txt")

states = []
for l in f.readlines():
    parts = l.split(" ")
    state = parts[0]
    states.append(state)
    tuples = parts[1:-1]
    joltage = parts[-1]
    print(tuples)
    
print(len(max(states)))

# grundidee:
# oldstate = []
# newstates = [originalstate]
# jeden button pressen für jeden newstate
# oldste.update(newstate)
# gucken ob neue states entstanden sind
# maximale länge von states sind 10, also 2^10 möglichkeiten maximal