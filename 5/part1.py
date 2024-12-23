data = open('5/ex input.txt','r')
rules,content = data.read().split("\n\n")

for line in content:
    for rule in rules.splitlines():
        X,Y = line.split("|")