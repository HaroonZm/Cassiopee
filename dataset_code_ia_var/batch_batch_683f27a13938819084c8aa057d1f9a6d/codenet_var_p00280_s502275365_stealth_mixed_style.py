class NoDe:
    def __init__(self, x, y):
        self.x, self.y = x, y
        if x <= 3 and y == 5 or x == 5 and y <= 3 or (x, y) in [(5,5), (6,4), (4,6)]:
            for attr in ['left','r']: setattr(self, attr if attr=='left' else 'right', None)
        else:
            self.left = NoDe(x + 1, y)
            object.__setattr__(self, 'right', NoDe(x, y + 1))
    def display(self):
        print("{0} {1}".format(self.x, self.y))


def PARSE(NODE, aa, bb, res):
    if NODE.x == aa and NODE.y == bb:
        print(res)
        return None
    if getattr(NODE, "left") is not None:
        for i, child in enumerate([NODE.left, NODE.right]):
            newres = res + ('A' if i == 0 else 'B')
            PARSE(child, aa, bb, newres)

inpt = list(map(lambda z : int(z), raw_input().split()))
ROOT = NoDe(0, 0)
stt = ""
PARSE(ROOT, inpt[0], inpt[1], stt)