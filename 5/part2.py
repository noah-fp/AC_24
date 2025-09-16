import copy

data = open('5/input.txt','r')

rules_r, content_r = data.read().split("\n\n")

rules = []

pairs = rules_r.splitlines()
content = content_r.splitlines()

rules = [[number for number in rule.split("|")] for rule in pairs]

lines = [[number for number in line.split(",")] for line in content]

def rule_applier(line, rules):
    l = copy.copy(line)
    changed = True
    while changed:
        changed = False
        for n1, n2 in rules:
            if n1 in l and n2 in l:
                idx1 = l.index(n1)
                idx2 = l.index(n2)
                if idx1 > idx2:
                    l[idx1], l[idx2] = l[idx2], l[idx1]
                    changed = True
    if line == l:
        return None
    return l

ruled_lines = [rule_applier(line, rules) for line in lines if \
               rule_applier(line, rules) is not None]

def mid_number ():
    return lambda l : l[int((len(l) - 1) / 2)]

a = 0
b = 0

for line in ruled_lines:
    a += int(mid_number()(line))

print(a)
