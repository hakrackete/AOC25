import re
import math
f = open("input/i2.txt","r")
rest = re.split(",", f.read())

ranges = []
for i in rest:
    nums = re.split("-",i)
    ranges.append((int(nums[0]),int(nums[1])))
print(ranges)

def invalid(num):
    symbols = int(math.log10(num))+1
    if symbols % 2 == 1:
        return False
    
    # print(symbols)
    first = str(num)[0:(symbols//2)]
    second = str(num)[symbols//2:]
    if first == second:
        return True
    else:
        return False
    # print(f"first: {first} second {second}")


def invalid2(num):
    symbols = int(math.log10(num))+1

    for num_splits in range(2,symbols+1):
        all_equal = False
        if not(symbols % num_splits == 0):
            continue
        split = symbols//num_splits 
        first = str(num)[0:split]
        for i in range(1,num_splits):
            second = str(num)[split*i:split*(i+1)]
            if first != second:
                all_equal = False
                break
            else:
                all_equal = True
        if all_equal:
            return True
    return False
    


counter = 0
for lower, upper in ranges:
    for x in range(lower,upper+1):
        if invalid2(x):
            counter+= x

print(counter)