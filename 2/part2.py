data = open('2/input.txt','r')
lines = data.readlines()
floor_safety = []

def difference_check(numbers):
        line_diff = []
        for i in range(len(numbers)-1):
            diff = abs(numbers[i] - numbers[i+1])
            line_diff.append(diff)
        return line_diff
            
def sequence_check(numbers):
    increasing = 1
    decreasing = 1
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i + 1]:
            increasing = 0
        if numbers[i] < numbers[i + 1]:
            decreasing = 0
        con_change = increasing + decreasing
    return con_change

def safety_check(line_diff, con_change):
    if min(line_diff) > 0 and max(line_diff) < 4 and con_change:
        return 1
    else:
        return 0

for line in lines:
    numbers = list(map(int,line.split()))
    total_line_saf = []
    
    for i in range(len(numbers)):
        listpt1 = numbers[:i]
        listpt2 = numbers[i+1:]
        alt_list = listpt1+listpt2
        alt_line_diff = difference_check(alt_list)
        alt_line_seq = sequence_check(alt_list)
        alt_line_safety = safety_check(alt_line_diff,alt_line_seq)
        
        total_line_saf.append(alt_line_safety)
    if sum(total_line_saf) == 0:
        line_safety = 0
    else:
        line_safety = 1
    floor_safety.append(line_safety)
print(sum(floor_safety))