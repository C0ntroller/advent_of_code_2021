map_dict = {}

with open("day05_data.txt") as data:
    line = data.readline().strip()
    while line:
        coords = line.split(' -> ')
        coords = [[int(y) for y in x.split(",")] for x in coords]
        # x same
        if coords[0][0] == coords[1][0]:
            l,h = (coords[0][1], coords[1][1]) if coords[1][1] > coords[0][1] else (coords[1][1], coords[0][1])
            for i in range(l, h+1):
                map_dict[(coords[0][0], i)] = map_dict.get((coords[0][0], i), 0) + 1
        # y same
        elif coords[0][1] == coords[1][1]:
            l,h = (coords[0][0], coords[1][0]) if coords[1][0] > coords[0][0] else (coords[1][0], coords[0][0])
            for i in range(l, h+1):
                map_dict[(i, coords[0][1])] = map_dict.get((i, coords[0][1]), 0) + 1
        # diagonal
        else:
            xs = coords[0][0]
            ys = coords[0][1]
            while True:
                map_dict[(xs, ys)] = map_dict.get((xs, ys), 0) + 1
                if [xs, ys] == coords[1]: break
                xs += 1 if xs < coords[1][0] else -1
                ys += 1 if ys < coords[1][1] else -1
     
        line = data.readline().strip()
    print(sum([1 for x in map_dict.values() if x > 1]))