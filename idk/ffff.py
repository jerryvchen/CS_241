curr_i, next_i = 0, 0
input_str = input()

def get_next():
    global i
    while input_str[i].isspace():
        i += 1
    res = input_str[i]
    i += 1
    return res

def peek():
    return input_str[i]



