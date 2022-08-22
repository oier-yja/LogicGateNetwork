import random


class Gate:
    def __init__(self):
        self.g = random.randint(0, 15)

    def stimulate(self, a, b):
        if self.g & (1 << (a * 2 + b)) > 0:
            return 1
        else:
            return 0

    def getG(self):
        return self.g
