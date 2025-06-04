def main():
    from sys import stdin
    input = stdin.readline
    executing = True
    while executing:
        try:
            N = int(input())
            if not N:
                break
            W, H = [], []
            W.append(0)
            H.append(0)
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for i in range(1, N):
                entry = input().split()
                if len(entry) < 2:
                    continue
                n, d = map(int, entry)
                x, y = W[n], H[n]
                dx, dy = directions[d]
                W.append(x + dx)
                H.append(y + dy)
            area = [max(W) - min(W) + 1, max(H) - min(H) + 1]
            print(*area)
        except Exception:
            break

class Runner:
    def __init__(self, callable_main):
        self.func = callable_main
    def run(self):
        self.func()

if __name__ == "__main__":
    runner = Runner(main)
    runner.run()