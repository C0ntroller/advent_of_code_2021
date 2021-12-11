with open("day11_data2.txt") as data:
    d = [list(map(int, list(x.strip()))) for x in data.readlines()]

def step(data):
    blinks = 0

    for i in range(10):
        for j in range(10):
            data[i][j] += 1
    
    def blink():
        for i in range(10):
            for j in range(10):
                if data[i][j] >= 10:
                    data[i][j] = 0
                    if i-1 >= 0 and j-1 >= 0: data[i-1][j-1] += 1 if data[i-1][j-1] > 0 else 0 # topleft
                    if i-1 >= 0: data[i-1][j] += 1 if data[i-1][j] > 0 else 0 # top
                    if i-1 >= 0 and j+1 < 10: data[i-1][j+1] += 1 if data[i-1][j+1] > 0 else 0 # topright
                    if j+1 < 10: data[i][j+1] += 1 if data[i][j+1] > 0 else 0 # right
                    if i+1 < 10 and j+1 < 10: data[i+1][j+1] += 1 if data[i+1][j+1] > 0 else 0 # bottom right
                    if i+1 < 10: data[i+1][j] += 1 if data[i+1][j] > 0 else 0 # bottom
                    if i+1 < 10 and j-1 >= 0: data[i+1][j-1] += 1 if data[i+1][j-1] > 0 else 0 # bottom left
                    if j-1 >= 0: data[i][j-1] += 1 if data[i][j-1] > 0 else 0 # left
                    return True
        return False

    changed = True
    while changed:
        changed = blink()
        blinks += changed
    
    return blinks

#blinks = 0
#for _ in range(100):
#    blinks += step(d)
#print(blinks)

steps = 0
while sum(map(sum, d)) != 0:
    step(d)
    steps += 1
print(steps)