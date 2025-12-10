f = open("input/i10.txt")

states = []
list_of_buttons = []
joltages = []
for l in f.readlines():
    parts = l.split(" ")

    state = tuple([0 if c == "." else 1 for c in parts[0][1:-1]])
    states.append(state)

    buttons = [tuple([int(y) for y in x[1:-1].split(",")]) for x in parts[1:-1]]
    list_of_buttons.append(buttons)

    joltage = tuple([int(n) for n in parts[-1][1:-2].split(",")])
    joltages.append(joltage)
    
print(state)
print(buttons)
print(joltage)

def change_state(state,button):
    state = list(state)
    for b in button:
        state[b] = (state[b] + 1) % 2
    return tuple(state)

def change_joltage(joltage,button):
    joltage = list(joltage)
    for b in button:
        joltage[b] = (joltage[b] + 1)
    return tuple(joltage)

def solve_state(state,buttons):
    presses = 0
    oldstate = {tuple([0 for n in s])}
    newstates = {tuple([0 for n in s])}
    while state not in newstates:
        presses += 1
        newstates2 = set()
        for b in buttons:
            for nstate in newstates:
                calculated_state = change_state(nstate,b)
                if calculated_state not in oldstate:
                    newstates2.add(calculated_state)
        oldstate.update(newstates)
        newstates = newstates2
    return presses


counter = 0
for i, s in enumerate(states):
    counter += solve_state(s,list_of_buttons[i])

print(counter)
    # grundidee:
    # oldstate = []
    # newstates = [originalstate]
    # jeden button pressen für jeden newstate
    # oldste.update(newstate)
    # gucken ob neue states entstanden sind
    # maximale länge von states sind 10, also 2^10 möglichkeiten maximal