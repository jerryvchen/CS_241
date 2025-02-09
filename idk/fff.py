class SomeError(Exception):
    pass

def main():
    i = 0
    input_str = input()

    while input_str[i].isspace():
        i += 1
    
    def set_next():
        while input_str[i].isspace():
            i += 1
    
    def peek():
        return input_str[i]
    

    def digit():
        if input_str[i] in '0123456789':
            res = int(input_str[i])
            set_next()
            return res
        return None
    
    def number():
        curr = digit()
        while input_str[i].isdigit():
            curr = curr * 10 + digit()
        return curr
        
    def factor():
        if input_str[i] == '(':
            curr = expression()
            if input_str[i] != ')':
                raise SomeError
            set_next() # consume ')'
        else:
            curr = number()
        
        return curr

    def term():
        curr = factor()
        while input_str[i] in '*/':
            if input_str[i] == '*':
                curr *= factor()
            elif input_str[i] == '/':
                curr //= factor()
        return curr
    
    def expression():
        curr = term()
        while input_str[i] in '+-':
            if input_str[i] == '+':
                curr += term()
            elif input_str[i] == '-':
                curr -= term()
        return curr

    def computation():
        curr = expression()
        if input_str[i] != '.':
            raise SomeError
        set_next() # consume '.'
        print(curr)
    
    while i < len(input_str):
        computation()


if __name__ == "__main__":
    main()