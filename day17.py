from random import randrange
with open("day17_data.txt") as data:
    r = [x.split("=")[1].split("..") for x in data.readline().strip().split(",")]
    x_range = range(int(r[0][0]), int(r[0][1])+1)
    y_range = range(int(r[1][0]), int(r[1][1])+1)

def sign(x):
    return (x>0) - (x<0)

def step(coords, velocities):
    coords = (coords[0] + velocities[0], coords[1] + velocities[1])
    xv = velocities[0]
    xv -= sign(xv)
    velocities = (xv, velocities[1] - 1)

    xd = min(map(lambda x: abs(x-coords[0]), x_range))
    yd = min(map(lambda y: abs(y-coords[1]), y_range))
    distance = xd**2 + yd**2

    return coords, velocities, distance

def test(vels):
    distance_old = float('inf')
    distance_new = float('inf')
    heights = []
    
    start = (0, 0)
    while not (distance_new > distance_old and vels[1] < 0):
        heights.append(start[1])
        if distance_old == 0: break
        distance_old = distance_new
        start, vels, distance_new = step(start, vels)
        #print(distance_new)
    return distance_old, max(heights)

def main():
    heights = []
    for i in range(1, 77):
        for j in range(-250, 230):
            result = (test((i, j)))
            if result[0] == 0: heights.append(((i,j), result[1]))
    print(max(heights, key=lambda h: h[1]))
    print(len(heights))

#print(test((6, 9)))
main()