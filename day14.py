from collections import Counter
with open("day14_data.txt") as data:
    molecule, reactions = data.read().split("\n\n")
    molecule = list(molecule.strip())
    molecule_parts = Counter()
    for i in range(1, len(molecule)):
        molecule_parts.update({"".join(molecule[i-1:i+1]): 1})
    reactions = dict([x.split(" -> ") for x in reactions.split("\n") if x])

def react_step():
    for elements in list(molecule_parts.items()):
        if elements[1] > 0 and elements[0] in reactions:
            molecule_parts.update({elements[0][0] + reactions[elements[0]]: elements[1], reactions[elements[0]] + elements[0][1]: elements[1]})
            molecule_parts.update({elements[0]: -elements[1]})

def count_diff():
    c = Counter()
    for element in molecule_parts.items():
        c.update({element[0][0]: element[1]})
    c.update(molecule[-1])
    return c.most_common()[0][1] - c.most_common()[-1][1]

"""def react_step():
    i = 0
    while i < len(molecule):
        elements = "".join(molecule[i-1:i+1])
        if elements in reactions: 
            molecule.insert(i, reactions[elements])
            i += 2
        else: i += 1"""

for _ in range(40):
    react_step()
print(count_diff())
