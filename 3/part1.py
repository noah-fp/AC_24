import re

data = open('3/input.txt','r')
input = data.read()

muls = re.findall(r"mul\((\d+)\,(\d+)\)",input)

def multiply_mul(muls):
    total = 0
    for int1,int2 in muls:
        product = int(int1)*int(int2)
        total += product
    return total

total = multiply_mul(muls)

print(total)