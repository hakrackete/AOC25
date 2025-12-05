import re
import math

banks = []
f = open("input/i3.txt","r")
for l in f.readlines():
    banks.append([int(x) for x in l.strip()])


counter = 0
for b in banks:
    first= max(b[:-1])
    i = b.index(first)
    second = max(b[i+1:])
    num = 10*first + second
    counter += num
print(counter)


counter = 0
for b in banks:
    joltage = 0
    index = 0
    for bat_num in range(11,-1,-1):
        # print(index)
        # print(bat_num)
        # print(b[index:-bat_num])
        if bat_num == 0:
            first= max(b[index:])
            index = b[index:].index(first) + index + 1
        else:
            first= max(b[index:-bat_num])
            index = b[index:-bat_num].index(first) + index + 1
        
        joltage = joltage*10 + first
    # print(joltage)
    counter += joltage
print(counter)

