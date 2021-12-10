from statistics import multimode
with open("day03_data2.txt") as data:
    d = [x.strip() for x in data.readlines()]; lw = len(d[0]); get_maj_bit = lambda data, pos: max(multimode([x[pos] for x in data])); g = int("".join([get_maj_bit(d, x) for x in range(lw)]), 2); e = int("".join([str(1 - int(get_maj_bit(d, x))) for x in range(lw)]), 2); print(g*e);o2=d.copy(); co2=d.copy()
for i in range(lw):
    o2 = [x for x in o2 if x[i] == get_maj_bit(o2, i)] if len(o2) > 1 else o2; co2 = [x for x in co2 if x[i] == str(1 - int(get_maj_bit(co2, i)))] if len(co2) > 1 else co2
print(int(o2[0],2))
print(int(co2[0],2))
