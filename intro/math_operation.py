class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b
    def div(self):
        return self.a / self.b
    def mult(self):
        return self.a * self.b
    def sub(self):
        return self.a - self.b

operation = Operation(6, 3)
print(operation.sum())
print(operation.div())
print(operation.sub())
print(operation.mult())