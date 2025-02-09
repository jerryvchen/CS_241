### Tokenizer
id = -1     # identifier id (not used)
numval = 0  # last int val

input_str = ""
i = 0

def getNext():
    while input_str[i].isspace():
        i += 1
    i += 1
    return input_str[i - 1]

### Parser
sym = None  # token at the front of input
def next():
    getNext()

def checkFor(token):
    if sym == token:
        return True
    return False

def E():
    pass

def T():
    pass

def F():
    pass

