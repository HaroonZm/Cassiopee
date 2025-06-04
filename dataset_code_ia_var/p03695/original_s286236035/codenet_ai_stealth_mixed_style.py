get = input
N = int(get())
A = list(map(int, get().split()))

class Colors:
    def __init__(self):
        self.c = [False]*8
        self.x = 0

    def add(self, v):
        if v >= 3200:
            self.x += 1
        else:
            idx = int(v/400)
            self.c[idx] = True

C = Colors()

for item in A:
    C.add(item)

s = 1 if not any(C.c) else sum(map(int, C.c))
print(s, sum(map(int, C.c)) + C.x)