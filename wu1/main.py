### Tokenizer
# Not really needed as this version goes character-by-character
input_str = input()
i = 0
sym = None

# initialize sym
while i < len(input_str):
    sym = input_str[i]
    if not sym.isspace():
        break
    i += 1

def get_next():
    global i
    global sym
    i += 1
    while i < len(input_str) and input_str[i].isspace():
        i += 1

    if i < len(input_str):
        sym = input_str[i]
    else:
        sym = None


### Parser
def digit():
    if sym.isdigit():
        res = int(sym)
        get_next()
        return res
    return None

def number():
    res = digit()
    next_digit = digit()
    while next_digit:
        res = res * 10 + next_digit
        next_digit = digit()
    
    return res

def factor():
    if sym == '(':
        get_next()
        res = expression()
        if sym == ')':
            get_next()
            return res
        else:
            raise SyntaxError
    else:
        return number()

def term():
    res = factor()
    if sym == '*':
        get_next() # consume 
        next_factor = factor()
        return res * next_factor
    
    elif sym == '/':
        get_next()
        next_factor = factor()
        return res // next_factor

    return res
    
def expression():
    res = term()
    if sym == '+':
        get_next()
        next_term = term()
        return res + next_term
    elif sym == '-':
        get_next()
        next_term = term()
        return res - next_term
    
    return res

def computation():
    res = expression()

    if sym == '.':
        get_next()
        print(res)
    else:
        raise SyntaxError

if __name__ == "__main__":
    while sym:
        computation()