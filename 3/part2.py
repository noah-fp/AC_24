import re

data = open('3/input.txt','r')
input = data.read()

def multiply_mul(muls):
    int1,int2,val3,val4 = muls
    product = int(int1)*int(int2)
    total = product
    return total

total = 0
do = True

for find in re.findall(r"mul\((\d+)\,(\d+)\)|(do\(\))|(don't\(\))",input):
    if "do()" in find:
        do = True
    elif "don't()" in find:
        do = False
    else:
        if do:
            total += multiply_mul(find)

print(total)