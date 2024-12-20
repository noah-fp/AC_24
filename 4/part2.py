import re

data = open('4/ex input.txt','r')
grid = data.read().split()
directions = [(-1,-1),(1,-1)]
count = 0

def boundary(y,x):
    # row and colummn indexes cannot exceed grid dimensions or be less than 0
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

for y_index,row in enumerate(grid):
    for x_index,character in enumerate(row):
        if character == "A":
            for y_var,x_var in directions:
                letter1 = (y_index + y_var,x_index + x_var)
                letter2 = (y_index - y_var,x_index - x_var)
                if not boundary(letter1[0],letter1[1]) or not boundary(letter2[0],letter2[1]):
                    break
                if not set((grid[letter1[0]][letter1[1]],grid[letter2[0]][letter2[1]])) == {"M","S"}:
                    break
            count += 1
print(count)