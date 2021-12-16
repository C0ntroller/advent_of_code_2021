from math import prod
with open("day16_data.txt") as data:
    bin_str = "".join(map(lambda x: "{:04b}".format(int(x, 16)), list(data.readline().strip())))

version_sum = 0

def parse_pkg(bins):
    global version_sum
    version = int(bins[:3], 2)
    version_sum += version
    type = int(bins[3:6], 2)
    bins = bins[6:]
    if type == 4:
        no_str = ""
        while True:
            no = bins[:5]
            no_str += no[1:]
            bins = bins[5:]
            if no[0] == "0": break
        return (bins, type, int(no_str, 2))
    else:
        length_type = bins[:1]

        if length_type == "0":
            payload_size = int(bins[1:16],2)
            payload_pkgs = []
            bins = bins[16:]
            length_before = len(bins)
            while length_before - len(bins) < payload_size:
                result = parse_pkg(bins)
                bins = result[0]
                payload_pkgs.append((result[1], result[2]))
            return (bins, type, payload_pkgs)
        else:
            payloads = int(bins[1:12],2)
            payload_pkgs = []
            bins = bins[12:]

            for _ in range(payloads):
                result = parse_pkg(bins)
                bins = result[0]
                payload_pkgs.append((result[1], result[2]))
            return (bins, type, payload_pkgs)

def calculate_pkgs(pkg):
    if pkg[0] == 4:
        return pkg[1]
    else:
        operands = list(map(calculate_pkgs, pkg[1]))
        if pkg[0] == 0:
            return sum(operands)
        elif pkg[0] == 1:
            return prod(operands)
        elif pkg[0] == 2:
            return min(operands)
        elif pkg[0] == 3:
            return max(operands)
        elif pkg[0] == 5:
            return int(operands[0] > operands[1])
        elif pkg[0] == 6:
            return int(operands[0] < operands[1])
        elif pkg[0] == 7:
            return int(operands[0] == operands[1])
    

result = parse_pkg(bin_str)
print(result[1], result[2])
print(version_sum)
print(calculate_pkgs((result[1], result[2])))
