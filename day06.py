with open("day06_data.txt") as file:
    a = file.readline(); fish = [len([f for f in [int(x) for x in a.split(",")] if f == i]) for i in range(9)]

def run(days):
    for _ in range(days):
        fish.append(fish.pop(0))
        fish[6] += fish[-1]

run(256)
print(sum(fish))

