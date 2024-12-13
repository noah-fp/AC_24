import re

def boundary(y,x):
    #row and colummn indexes cannot exceed 9 or be less than 0
    limit = True
    if y > 9 or y < 0 or x > 9 or x < 0:
        limit = False
    return limit

data = open('4/ex input.txt','r')
directions = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(1,-1),(1,0),(1,1)]
next_letter = ["M","A","S"]

for y_index,row in enumerate(data):
    for x_index,character in enumerate(row):
        if character == "X":
            for y_var,x_var in enumerate(directions):
                course = (y_index + y_var,x_index + x_var)
                if boundary(course[0],course[1]):
                    next_chara = 

print(course," - ",limit)