# Part 1
with open("day02_data.txt") as data:
    line = data.readline()
    h = 0
    d = 0
    while line:
        command, steps = line.split(" ")
        steps = int(steps)
        if command == "forward":
            h += steps
        if command == "down":
            d += steps
        if command == "up":
            d -= steps
        line = data.readline()
    print(d*h)

with open("day02_data.txt") as data:
    line = data.readline()
    h = 0
    a = 0
    d = 0
    while line:
        command, steps = line.split(" ")
        steps = int(steps)
        if command == "forward":
            h += steps
            d += a * steps
        if command == "down":
            a += steps
        if command == "up":
            a -= steps
        line = data.readline()
    print(d*h)
