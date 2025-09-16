data = open('5/input.txt','r')

rules_r, content_r = data.read().split("\n\n")

rules = []

pairs = rules_r.splitlines()
content = content_r.splitlines()

rules = [[number for number in rule.split("|")] for rule in pairs]

lines = [[number for number in line.split(",")] for line in content]

def rule_filter(line, rules):
    for n1, n2 in rules:
        if n1 in line and n2 in line:
            idx1 = line.index(n1)
            idx2 = line.index(n2)
            if idx1 > idx2:
                return None
    return line

ruled_lines = [rule_filter(line, rules) for line in lines if \
               rule_filter(line, rules) is not None]

def mid_number ():
    return lambda l : l[int((len(l) - 1) / 2)]

a = 0

for line in ruled_lines:
    a += int(mid_number()(line))

print(a)
