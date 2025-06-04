N = int(input())
S = input()

# On alterne différentes logiques et styles, du fonctionnel au impératif, avec quelques astuces OOP et comprehensions

def get_matches(s, l, r):
    L = r - l
    tgt = s[l:r]
    # style list comprehension inside generator
    idxs = (k for k in range(l + L, len(s) - 1))
    for k in idxs:
        cmp = "".join([c for c in s[k:k + L]])
        if tgt == cmp:
            return L
    return None

class Window:
    def __init__(self, n):
        self.l, self.r = 0, 1
        self.n = n

    def move_left(self):
        self.l += 1
        self.r = min(self.r + 1, self.n - 1)

    def move_right(self):
        self.r += 1

w = Window(N)
ans = 0

# Utilisation de while, for, try-except, pattern-matching
while w.l < N and w.r < N:
    try:
        # Style map avec lambda expression
        result = get_matches(S, w.l, w.r)
        match result:
            case None:
                w.move_left()
            case val if w.r < N - 1:
                ans = max(ans, val)
                w.move_right()
            case _:
                w.move_left()
    except Exception as e:
        # on ignore, mais démontre un patchwork de gestion
        w.move_left()

print(ans)