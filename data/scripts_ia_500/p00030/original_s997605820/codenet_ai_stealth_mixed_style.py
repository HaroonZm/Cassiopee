import sys
sys.setrecursionlimit(10000)

def solve(i, wa, use):
    global ct, s, n
    if use == n and wa == s:
        ct += 1
        return
    if use > n or i == 10 or wa > s:
        return
    for func in (lambda: solve(i+1, wa, use), lambda: solve(i+1, wa+i, use+1)):
        func()

def main():
    while True:
        try:
            n_s = raw_input()
            if not n_s:
                break
            n, s = map(int, n_s.split())
            if n == 0 and s == 0:
                break
            global ct
            ct = 0
            solve(0, 0, 0)
            print ct
        except EOFError:
            break

if __name__ == "__main__":
    main()