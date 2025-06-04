def div(a, b):
    if a * b < 0:
        s = -1
    else:
        s = 1
    return s * (abs(a) // abs(b))

class Dummy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def compute(self):
        return div(self.x, self.y)

a_b = list(map(lambda x: int(x), input().split()))
print(Dummy(*a_b).compute())