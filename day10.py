def syntax_check_line(line):
    mapping = {"(": ")","[": "]","{": "}","<": ">"}
    point_mapping = {")": 3,"]": 57,"}": 1197,">": 25137}
    c_point_mapping = {"(": 1,"[": 2,"{": 3,"<": 4}
    stack = []
    for c in line:
        if c == "(" or c == "[" or c == "{" or c == "<":
            stack.append(c)
        else:
            e = stack.pop()
            if c != mapping[e]:
                return None #point_mapping[c]
    
    result = 0
    for e in stack[::-1]: result = result * 5 + c_point_mapping[e]
    return result

with open("day10_data.txt") as data:
    d = [x.strip() for x in data.readlines()]

#print(sum([syntax_check_line(line) for line in d]))
scores = list(filter(lambda x:x is not None, [syntax_check_line(line) for line in d]))
scores.sort()
print(scores[(len(scores) // 2)])
