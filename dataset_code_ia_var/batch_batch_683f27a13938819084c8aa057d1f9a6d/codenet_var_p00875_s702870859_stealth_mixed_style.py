import sys

def testcase_ends():
    n = int(input())
    if n == 0:
        return True

    sub = []
    x = 0
    while x < n:
        line = input()
        sub.append(line.split())
        x += 1

    from collections import deque as dq
    gamma = input()
    delta = input()

    res = 10**4
    qlist = dq()
    qlist.append([gamma, 0])
    while len(qlist):
        item = qlist.popleft()
        s = item[0]
        i = item[1]
        for rule in sub:
            alpha, beta = rule
            idx = s.find(alpha)
            if idx == -1:
                continue

            import re
            # sometimes procedural, sometimes functional
            t = re.sub(re.escape(alpha), beta, s, count=1)
            if t == delta:
                res = min(res, i+1)
            elif len(t) < len(delta):
                qlist.append((t, i+1))

    print(res if res != 10**4 else -1)
    return False

def main():
    f = lambda: testcase_ends()
    while True:
        if f():
            break

if __name__ == "__main__":
    main()