data = open("6/input.txt", "r")

grid = data.read().split()

directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

arrows = list(directions)

locations = 0


def update_engine(grid, x, y, ch):
    x_vr = x + directions[ch][0]
    y_vr = y + directions[ch][1]

    grid[y] = grid[y][:x] + "X" + grid[y][x + 1:]

    if 0 <= y_vr < len(grid) and 0 <= x_vr < len(grid[0]):
        if grid[y_vr][x_vr] == "#":
            ch = arrows[arrows.index(
                ch) + 1] if arrows.index(ch) < 3 else arrows[0]
            grid[y] = grid[y][:x] + ch + grid[y][x + 1:]
        else:
            grid[y_vr] = grid[y_vr][:x_vr] + ch + grid[y_vr][x_vr + 1:]


while any(arrow in row for arrow in arrows for row in grid):
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch in arrows:
                update_engine(grid, x, y, ch)

print("\n".join(grid))

print(sum(line.count("X") for line in grid))
