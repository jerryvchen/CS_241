class MathInterpreter:
    def __init__(self, line):
        self.line = line
        self.i = 0

    def run(self):
        while self.i < len(self.line):
            self.computation()
    
    def next(self):
        while self.i < len(self.line):
            if self.line[self.i] != ' ':
                self.i += 1
                return self.line[self.i - 1]
            self.i += 1
        return None

    def digit(self):
        res = next()
        if res.isnumeric():
            return res
        

    def number(self):
        self.digit()

    def factor(self):
        self.number()

    def term(self):
        self.factor()

    def expression(self):
        self.term()

    def computation(self):
        self.expression()

if __name__ == "__main__":
    line = input()
    interpreter = MathInterpreter(line)
    interpreter.run()