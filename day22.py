from itertools import product
with open("day22_data.txt") as data:
    d = [(int(state == "on"),ranges.split(",")) for state, ranges in [line.strip().split()for line in data.readlines()]]

onset = set()
for step in d:
    ranges = [tuple(map(int, x[2:].split(".."))) for x in step[1]]
    if list(filter(lambda x: abs(x[0]) > 50 or abs(x[1]) > 50, ranges)) != []: continue
    if step[0]: onset.update(product(range(ranges[0][0], ranges[0][1]+1), range(ranges[1][0], ranges[1][1]+1), range(ranges[2][0], ranges[2][1]+1)))
    else: onset.difference_update(product(range(ranges[0][0], ranges[0][1]+1), range(ranges[1][0], ranges[1][1]+1), range(ranges[2][0], ranges[2][1]+1)))
    # Better way: Save the ranges and the overlaps, just sum the volumes in the end.

def calc_on():
    pass