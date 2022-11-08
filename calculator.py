
class MiniCalculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self, reverse=False):
        if reverse:
            return self.b - self.a
        return self.a - self.b

    def multiply(self):
        pass

    def divide(self):
        pass
