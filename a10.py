from pulp import *


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
    oldstate = {tuple([0 for n in state])}
    newstates = {tuple([0 for n in state])}
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

def solve_joltage(state,buttons):
    presses = 0
    oldstate = {tuple([0 for n in state])}
    newstates = {tuple([0 for n in state])}
    while state not in newstates:
        presses += 1
        print(presses)
        newstates2 = set()
        for b in buttons:
            for nstate in newstates:
                calculated_state = change_joltage(nstate,b)
                if calculated_state not in oldstate:
                    newstates2.add(calculated_state)
        oldstate.update(newstates)
        newstates = newstates2
    return presses


def solve1(states,list_of_buttons):
    counter = 0
    for i, s in enumerate(states):
        counter += solve_state(s,list_of_buttons[i])
    print(counter)
    return counter


# this should work, but is exponentioal in the runtime/searchspace, for all joltage levels
# is correct with the example, works in not much tima also
# i should go with a linear equation solver
def solve2_naive(joltages,list_of_buttons):
    counter = 0
    for i, s in enumerate(joltages):
        counter += solve_joltage(s,list_of_buttons[i])
    print(counter)
    return counter

# solve1(states,list_of_buttons)

# counter = 0
# for i, s in enumerate(states):
#     counter += solve_joltage(joltage,list_of_buttons[i])
# print(counter)

# solve_joltage(joltages[0],list_of_buttons[0])
# solve2_naive(joltages,list_of_buttons)
    # grundidee:
    # oldstate = []
    # newstates = [originalstate]
    # jeden button pressen für jeden newstate
    # oldste.update(newstate)
    # gucken ob neue states entstanden sind
    # maximale länge von states sind 10, also 2^10 möglichkeiten maximal
def solve_eq(joltage,mybuttons):
    model = LpProblem("ILP", LpMinimize)

    # Anzahl der Variablen
    n = len(mybuttons)

    # soviele Variablen erstellen, constraint, dass diese INteger sein müssen
    x = LpVariable.dicts("x", range(n), lowBound=0, cat="Integer")

    # Zielfunktion mitteilen, wir wollen die Summe aller variablen minimieren
    model += lpSum(x[i] for i in range(n))

    for i,j in enumerate(joltage):
        A = [1 if i in b else 0 for b in mybuttons]
        model += lpSum(A[i] * x[i] for i in range(n)) == j

    # print(model)

    solver = PULP_CBC_CMD(msg=False, logPath=None)
    status = model.solve(solver)
    # print("Lösung:")
    # for j in range(n):
    #     print(f"x{j} =", x[j].value())
    best = sum(x[j].value() for j in range(len(x)))
    return int(best)
# solution = solve_eq(joltages[0],list_of_buttons[0])
# print(solution)

def solve2(joltages, list_of_buttons):
    counter = 0
    for i,j in enumerate(joltages):
        counter += solve_eq(j,list_of_buttons[i])
    
    return counter

solution2 = solve2(joltages,list_of_buttons)
print(solution2)