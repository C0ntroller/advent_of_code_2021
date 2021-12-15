with open("day15_data.txt") as data:
    d = [list(map(int, list(x.strip()))) for x in data.readlines()]
    y_dim = len(d)
    x_dim = len(d[0])


def get_neighbors(x, y):
    neightbors = []
    def calc_weight(x, y):
        #return d[y][x]
        return ((d[y % y_dim][x % x_dim] + x // x_dim + y // y_dim) % 10) + 1
    #if x+1 < x_dim: neightbors.append(((x+1,y), calc_weight(x+1, y)))
    if x+1 < x_dim * 5: neightbors.append(((x+1,y), calc_weight(x+1, y)))
    if x > 0: neightbors.append(((x-1,y), calc_weight(x-1, y)))
    #if y+1 < y_dim: neightbors.append(((x,y+1), calc_weight(x, y+1)))
    if y+1 < y_dim * 5: neightbors.append(((x,y+1), calc_weight(x, y+1)))
    if y > 0: neightbors.append(((x,y-1), calc_weight(x, y-1)))
    return neightbors

#end = (x_dim-1, y_dim-1)
end = (x_dim*5-1, y_dim*5-1)

def dijkstra():
    stack = {} 
    stack[(0,0)] = 0
    found = set()
    while True:
        if end in stack: return stack[end]
        current = min(stack, key=stack.get)
        found.add(current)
        for neighbor, n_distance in get_neighbors(current[0], current[1]):
            distance = min(stack[current] + n_distance, stack.get(neighbor, float('inf')))
            if neighbor not in found:
                stack[neighbor] = distance
        del stack[current]

print(dijkstra())
