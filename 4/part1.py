data = open('4/input.txt','r')
grid = data.read().split()
directions = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
next_letter = ["M","A","S"]
count = 0

def boundary(y,x):
    # row and colummn indexes cannot exceed 9 or be less than 0
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

for y_index,row in enumerate(grid):
    for x_index,character in enumerate(row):
        if character == "X":
            for y_var,x_var in directions:
                course = (y_index,x_index)
                for letter in next_letter:
                    course = (course[0] + y_var,course[1] + x_var)
                    if not boundary(course[0],course[1]):
                        break
                    if not grid[course[0]][course[1]] == letter:
                        break
                    if letter == "S":
                        count += 1
print(count)