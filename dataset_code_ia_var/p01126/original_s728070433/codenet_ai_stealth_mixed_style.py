import sys

INFINITE = float('inf')

def main_loop():
    from collections import deque

    while True:
        try:
            c = sys.stdin.readline()
            if not c:
                break
            s = c.strip().split()
            if len(s) < 3:
                continue
            n, m, a = (int(s[0]), int(s[1]), int(s[2]))
            if not any((n, m, a)):
                return
            arr = []
            for j in range(m):
                t = sys.stdin.readline()
                tup = tuple([int(x) for x in t.strip().split()])
                arr.append(tup)
            arr.sort(key=lambda x: x[0])
            steps = deque(arr)
            while steps:
                h, p, q = steps.pop()
                if a == p:
                    a = q
                    continue
                if a == q:
                    a = p
            print(a)
        except Exception:
            break

def run_prog():
    main_loop()

if __name__ == "__main__":
    run_prog()