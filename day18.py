import re, math

def reduce_term(term):
    need_more = True
    while need_more:
        term, need_more = search_explosion(term)
        #print(term)
        if need_more: continue
        term, need_more = search_split(term)

    #print(term)
    return term

def search_explosion(term: str):
    open = 0
    left = None
    right = None
    i = 0
    while i < len(term):
        if term[i] == "[": open += 1
        elif term[i] == "]": open -= 1
        elif term[i] == ",": pass
        else:
            # Number
            n_str = ""
            start = i
            while term[i].isdigit():
                n_str += term[i]
                i += 1
            number = int(n_str)
            left = (number, (start, i))
            i -= 1
        
        if open == 5:
            # Explosion found
            bracket_open_idx = i
            # Find left number
            i += 1
            n_str = ""
            while term[i].isdigit():
                n_str += term[i]
                i += 1
            left_number = int(n_str)
            
            i += 1
            n_str = ""
            while term[i].isdigit():
                n_str += term[i]
                i += 1
            right_number = int(n_str)

            bracket_close_idx = i

            right_search = re.search(r"\d+", term[bracket_close_idx:])
            if right_search: right = (int(right_search.group()), (right_search.span()[0] + bracket_close_idx, right_search.span()[1] + bracket_close_idx))

            if left: 
                term = replace_into_str(term, left_number + left[0], left[1])
                idx_diff = len(str(left_number + left[0])) - len(str(left[0]))
                if idx_diff:
                    bracket_open_idx += idx_diff
                    bracket_close_idx += idx_diff
                    if right: right = (right[0], (right[1][0] + idx_diff, right[1][1] + idx_diff))
            if right: term = replace_into_str(term, right_number + right[0], right[1])
            term = replace_into_str(term, 0, (bracket_open_idx, bracket_close_idx + 1))
            #print(term)
            return term, True
        
        i += 1
        
    return term, False

def search_split(term:str):
    find = re.search(r"\d{2,}", term)
    if find:
        find_res = (int(find.group()), find.span())
        replace = f"[{math.floor(find_res[0]/2)},{math.ceil(find_res[0]/2)}]"
        return replace_into_str(term, replace, find_res[1]), True
    return term, False


def replace_into_str(string, insert_string, span):
    return string[:span[0]] + str(insert_string) + string[span[1]:]


def calc_magnitude(term):
    if isinstance(term[0], list): left_val = calc_magnitude(term[0])
    else: left_val = term[0]
    if isinstance(term[1], list): right_val = calc_magnitude(term[1])
    else: right_val = term[1]
    return 3*left_val + 2*right_val

with open("day18_data.txt") as data:
    old_term = data.readline().strip()
    lines = [old_term]
    line = data.readline().strip()
    while line:
        lines.append(line)
        old_term = reduce_term(f"[{old_term},{line}]")
        line = data.readline().strip()
    print(old_term)
    print(calc_magnitude(eval(old_term)))

    max_score = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j: continue
            max_score = max(max_score, calc_magnitude(eval(reduce_term(f"[{lines[i]},{lines[j]}]"))))
    print(max_score)