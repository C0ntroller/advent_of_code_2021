with open("day13_data.txt") as data:
    x_dim = 0
    y_dim = 0
    sheet = set()
    line = data.readline().strip()
    while line:
        coords = tuple(map(int, line.split(",")))
        x_dim = coords[0] if coords[0] > x_dim else x_dim
        y_dim = coords[1] if coords[1] > y_dim else y_dim
        sheet.add(coords)
        line = data.readline().strip()
    folds = []
    line = data.readline().strip()
    while line:
        folds.append(line[11:].split("="))
        line = data.readline().strip()

def fold(fold_params):
    global sheet, x_dim, y_dim
    axis = fold_params[0]
    pos = int(fold_params[1])
    if axis == "x": ftr = lambda c: c[0] > pos
    if axis == "y": ftr = lambda c: c[1] > pos
    to_flip = set(filter(ftr, sheet))
    if axis == "x": manipulator = lambda c: (c[0] - 2*(c[0] - pos), c[1])
    if axis == "y": manipulator = lambda c: (c[0], c[1] - 2*(c[1] - pos))
    flipped = map(manipulator, to_flip)
    sheet.difference_update(to_flip)
    sheet.update(flipped)
    if axis == "x": x_dim = pos
    if axis == "y": y_dim = pos

def print_sheet():
    global sheet, x_dim, y_dim
    s_str = [["." for _ in range(x_dim)] for _ in range(y_dim)]
    for p in sheet: s_str[p[1]][p[0]] = "#"
    for x in s_str: print("".join(x))
    

#fold(folds[0])
#print(len(sheet))
for f in folds:
    fold(f)
print_sheet()
