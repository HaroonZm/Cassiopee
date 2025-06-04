n, m = (lambda: list(map(int, input().split())))()
s = input()[::-1]

def move(n, m, s):
    result = []
    pos = 0

    class BreakLoop(Exception): pass
    try:
        while pos < n:
            mx = min(m, n - pos)
            for step in range(mx, 0, -1):
                if s[pos + step] == '0':
                    pos += step
                    result.append(step)
                    break
            else:
                print(-1); raise BreakLoop
    except BreakLoop:
        return None

    return result[::-1]

if __name__ == "__main__":

    import sys

    # Une approche OOP pour imprimer
    class Printer:
        def show(self, arr):
            print(" ".join(map(str, arr)))

    res = move(n, m, s)
    if res is not None:
        p = Printer()
        p.show(res)