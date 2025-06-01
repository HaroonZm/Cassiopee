from functools import reduce
class CardGame:
    def __init__(self):
        self._inf_loop_break = False
        self._lmb = lambda f, s: list(map(f, s))
    def comp_map(self, f, s):
        return reduce(lambda acc, x: acc + [f(x)], s, [])
    def get_input(self):
        while True:
            try:
                return int(input())
            except Exception:
                continue
    def play(self):
        while True:
            n = (lambda: self.get_input())()
            if not n:
                break
            c = [1] + list(reduce(lambda acc, x: acc + [0], self.comp_map(int, [input() for _ in range(n)]), [1]* (2*n)))
            m = [n,n]
            t, ba, f = 0, 0, 0
            def find_and_update():
                nonlocal ba, t, m, c, f
                for i in range(ba + 1, 2*n + 1):
                    if t == c[i]:
                        ba = i
                        c[i] = 2
                        m[t] -= 1
                        f = 0
                        return
                    if i == 2*n:
                        ba = 0
                if f:
                    ba = 0
            while all(x > 0 for x in m):
                f = 1
                find_and_update()
                t = 1 - t
            print(m[1], m[0], sep='\n')
CardGame().play()