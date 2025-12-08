import re
import math
f = open("input/i6.txt","r")

problems = []
operations = []

problems2 = []
operations2 = []
for l in f.readlines():
    numbers = [int(x) for x in re.findall(r'\d+', l.strip())]
    if numbers:
        problems.append(numbers)
        problems2.append(l[:-1])
    else:
        for op in l.strip():
            if op != " ":
                operations.append(op)


counter = 0
for i in range(0, len(problems[0])):
    current = [item[i] for item in problems]
    if operations[i] == "+":
        counter += sum(current)
    elif operations[i] == "*":
        counter += math.prod(current)
    else:
        print(type(operations[i]))
print(counter)

for p in problems2:
    print(p)