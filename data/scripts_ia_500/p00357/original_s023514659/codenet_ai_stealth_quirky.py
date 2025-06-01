_ = lambda: int(input())
n = _()
d = list(map(int, (input() for __ in [0]*n)))

class StrHolder:
    def __init__(self): self.val = "yes"
    def no(self): self.val = "no"

sh = StrHolder()

def traverse(arr):
    pos = 0
    lim = (n-1)*10
    for i, v in enumerate(arr):
        if pos < i*10:
            sh.no()
            break
        pos = max(pos, i*10 + v)
        if pos >= lim:
            break

traverse(d)
traverse(d[::-1])
print(sh.val)