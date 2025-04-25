##### Warm-Up 2 (wu2) Interpreter #####
from enum import Enum

class WU2_Token(Enum):
    COMPUTATION = 0
    VAR = 1

    IDENIFIER = 2
    NUMBER = 3
    ASSIGNMENT_OP = 4 # <-

    OPEN_PARENTHESIS = 5
    CLOSE_PARENTHESIS = 6

    PLUS = 7
    MINUS = 8
    MUL = 9
    DIV = 10

    SEMICOLON = 11
    PERIOD = 12

class WU2_Tokenizer:
    """
    The Tokenizer for the WU2_Interpreter.

    Specifically parses:
    - identifiers
    - numbers
    - special symbols
    """
    def __init__(self, input_str: str) -> None:
        """
        Initializes the Tokenizer

        :param str input_str: 
        """
        self.in_str: list[str] = list(reversed([ch for ch in input_str.strip()]))
        self.curr: str | None = None
        self.next: str | None = None

        # finite state machine (see get_next())
        # 0: start
        # 1: identifier (starts with "letter")
        # 2: number (starts with "digit")
        # 3: assignment op (starts with "<")
        # 4: single ch things (ex: +, -, *, /, ;, .)
        self.state = 0

        self.number = 0
        self.identifier = [] # to be joined when returned

        self.get_next_ch()
        self.get_next_ch()
 
    def get_next_ch(self):
        """
        Sets self.curr and self.next to the next states
        """
        self.curr = self.next
        if self.in_str:
            self.next = self.in_str.pop()
        else:
            self.next = None
            return
        
        while self.curr == ' ' and self.next == self.curr:
            self.next = self.in_str.pop() # remove contiguous spaces
    
    def get_number(self):
        res = self.number
        self.number = 0
        return res

    def get_identifier(self):
        res = "".join(self.identifier)
        self.identifier = []
        return res

    def get_next(self):
        """
        Returns the next token.
        """
        # if on space, just get next ch
        if self.curr == ' ':
            self.get_next_ch()
        
        if self.curr is None:
            return
        
        while self.state != -1:
            match self.state:
                case 0: # start
                    # tranfer to other state
                    if self.curr.isalpha():
                        self.state = 1
                        self.identifier.append(self.curr)

                    elif self.curr.isdigit():
                        self.state = 2
                        self.number = int(self.curr)
                    
                    elif self.curr == '<':
                        self.state = 3
                    
                    else:
                        res = -1
                        if self.curr == '(':
                            res = WU2_Token.OPEN_PARENTHESIS
                        elif self.curr == ')':
                            res = WU2_Token.CLOSE_PARENTHESIS
                        elif self.curr == '+':
                            res = WU2_Token.PLUS
                        elif self.curr == '-':
                            res = WU2_Token.MINUS
                        elif self.curr == '*':
                            res = WU2_Token.MUL
                        elif self.curr == '/':
                            res = WU2_Token.DIV
                        elif self.curr == ';':
                            res = WU2_Token.SEMICOLON
                        elif self.curr == '.':
                            res = WU2_Token.PERIOD
                        else:
                            raise SyntaxError
                        
                        self.get_next_ch()
                        return res

                    self.get_next_ch()
                        
                case 1: # identifier
                    while self.curr.isalpha():
                        self.identifier.append(self.curr)
                        self.get_next_ch()
                    
                    self.state = 0

                    # check to see if it maches computation or var
                    res = "".join(self.identifier)

                    if res == "computation":
                        self.identifier = []
                        return WU2_Token.COMPUTATION
                    
                    if res == "var":
                        self.identifier = []
                        return WU2_Token.VAR


                    return WU2_Token.IDENIFIER

                case 2: # number 
                    while self.curr.isdigit():
                        self.number = self.number * 10 + int(self.curr)
                        self.get_next_ch()
                    
                    self.state = 0
                    return WU2_Token.NUMBER
                
                case 3: # assignment op
                    if self.curr != "-":
                        raise SyntaxError
                    self.state = 0
                    self.get_next_ch()
                    return WU2_Token.ASSIGNMENT_OP
        return


class WU2_Interpreter:
    def __init__(self):
        input_str = input()
        self.tokenizer = WU2_Tokenizer(input_str)
        self.table = dict() # identifier table
                            # could be optimized but get working verions first

        self.curr = self.tokenizer.get_next()
        self.next = self.tokenizer.get_next()

        self.computation()
    
    def get_next(self):
        self.curr = self.next
        self.next = self.tokenizer.get_next()

    def factor(self):
        # set self.curr to AFTER factor
        if self.curr == WU2_Token.IDENIFIER:
            iden = self.tokenizer.get_identifier()
            self.get_next()
            return self.table[iden]
        
        elif self.curr == WU2_Token.NUMBER:
            num = self.tokenizer.get_number()
            self.get_next()
            return num

        elif self.curr == WU2_Token.OPEN_PARENTHESIS:
            self.get_next()
            exp = self.expression()
            if self.curr != WU2_Token.CLOSE_PARENTHESIS:
                raise SyntaxError
            self.get_next() # consume close parenthesis
            return exp
        
        else:
            raise SyntaxError


    def term(self):
        res = self.factor()

        while self.curr == WU2_Token.MUL or self.curr == WU2_Token.DIV:
            if self.curr == WU2_Token.MUL:
                self.get_next()
                res *= self.factor()
            elif self.curr == WU2_Token.DIV:
                self.get_next()
                res //= self.factor()
        
        return res

    def expression(self):
        res = self.term()

        while self.curr == WU2_Token.PLUS or self.curr == WU2_Token.MINUS:
            if self.curr == WU2_Token.PLUS:
                self.get_next()
                res += self.term()
            elif self.curr == WU2_Token.MINUS:
                self.get_next()
                res -= self.term()
        
        return res



    def computation(self):
        if self.curr != WU2_Token.COMPUTATION:
            raise SyntaxError

        self.get_next()

        ### READ IN VAR IDENTIFIERS
        while self.curr == WU2_Token.VAR:
            self.get_next()
            if self.curr != WU2_Token.IDENIFIER:
                raise SyntaxError
            
            iden = self.tokenizer.get_identifier()

            self.get_next()
            if self.curr != WU2_Token.ASSIGNMENT_OP:
                raise SyntaxError
            self.get_next()

            self.table[iden] = self.expression()

            if self.curr != WU2_Token.SEMICOLON:
                raise SyntaxError
            self.get_next()

        ### COMPUTE EXPRESSIONS
        res = self.expression()
        print(res)

        while self.curr == WU2_Token.SEMICOLON:
            self.get_next()
            res = self.expression()
            print(res)
        
        if self.curr != WU2_Token.PERIOD:
            raise SyntaxError
        
        return

if __name__ == "__main__":
    WU2_Interpreter()