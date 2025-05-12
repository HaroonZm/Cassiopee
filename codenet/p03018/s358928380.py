import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)

def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())

def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())

def main():
    s = [c for c in gete()]
    ans = 0
    a = 0
    cur = 0
    while cur < len(s) - 2:

        if "".join(s[cur:cur + 3]) == "ABC":
            ans += a + 1
            cur += 2
            s[cur] = "A"
        else:
            if s[cur] == "A":
                a += 1
            else:
                a = 0
            cur += 1

    print(ans)

if __name__ == "__main__":
    main()