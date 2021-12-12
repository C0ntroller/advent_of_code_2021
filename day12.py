from copy import deepcopy
map_dict = {}
with open("day12_data.txt") as data:
    d = [x.strip().split("-") for x in data.readlines()]
    for p in d:
        map_dict[p[0]] = map_dict.get(p[0], []) + [p[1]]
        map_dict[p[1]] = map_dict.get(p[1], []) + [p[0]]

# print(map_dict)

count1 = 0
def explore_edge1(start_node, curr_map):
    global count1
    if start_node == "end": 
        count1 += 1
        return

    curr_map = deepcopy(curr_map)
    nbs = curr_map[start_node]
    if start_node.islower():
        for nb in nbs: 
            curr_map[nb].remove(start_node)
    
    for nb in nbs:
        explore_edge1(nb, curr_map)

explore_edge1("start", map_dict)
print(count1)

count2 = 0
def explore_edge2(start_node, curr_map, double, db_visit = False, db_db = False):
    global count2
    if start_node == "end":
        count2 += int(db_db)
        return

    curr_map = deepcopy(curr_map)
    nbs = curr_map[start_node]
    if start_node.islower():
        if start_node != double or db_visit:
            for nb in nbs: 
                curr_map[nb].remove(start_node)
        if start_node == double:
            db_db = db_db or db_visit
            db_visit = True
    
    for nb in nbs:
        explore_edge2(nb, curr_map, double, db_visit, db_db)

[explore_edge2("start", map_dict, d) for d in filter(lambda x: x.islower() and x != "start" and x != "end", map_dict.keys())]
print(count2)
print(count1 + count2)