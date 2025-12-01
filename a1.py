f = open("input/i1.txt","r")

inputs = []
for line in f.readlines():
    inputs.append((line[0], int(line[1:])))

print(inputs)

counter = 50
counted_zeros = 0

for i in inputs:
    # print(i)

    if i[0] == "R":
        counter = (counter +  i[1]) % 100
    else:
        counter = (counter - i[1]) % 100
    
    if counter == 0:
        counted_zeros += 1
    
    # print(counter)
print(counted_zeros)

counter = 50
counted_zeros = 0
for i in inputs:
    # print(i)
# checken wie oft man über die null läuft, einfach den remainder von //100 
    if i[0] == "R":
        counted_zeros += (counter + i[1]) // 100
        counter = (counter +  i[1]) % 100
    
    else:
        # spezielfall, counter zählt einmal zuviel, wenn man auf der Null startet
        if counter == 0:
            counted_zeros += abs((counter - 100 - i[1])) // 100 - 1
        else:
            counted_zeros += abs((counter - 100 - i[1])) // 100
        counter = (counter - i[1]) % 100
    
    # if counter == 0:
    #     counted_zeros += 1
    # print(f"zeros. {counted_zeros} value {counter}")
    # print(counter)
print(counted_zeros)


