class Exp:
    def __init__(self):
        pass
class BinExp (Exp):
    def __init__(self, left, op, right):
        self.op = op
        self.left = left
        self.right = right
    def eval(self):
        if self.op == '+':
            return self.left.eval() + self.right.eval()
        elif self.op == '-':
            return self.left.eval() - self.right.eval()
        elif self.op == '*':
            return self.left.eval() * self.right.eval()
        return self.left.eval() / self.right.eval()
class UnExp (Exp):
    def __init__(self, op, val):
        self.op = op
        self.val = val
    def eval(self):
        if self.op == '-':
            return - self.val.eval()
        return self.val.eval()
class IntLit (Exp):
    def __init__(self, val):
        self.val = val
    def eval(self):
        return self.val
class FloatLit (Exp):
    def __init__(self, val):
        self.val = val
    def eval(self):
        return self.val