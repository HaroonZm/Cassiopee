import math, string, itertools as it, fractions, heapq, collections, re as regex, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)
INF = pow(10, 20)
EPS = 1.0/1e10
MOD = 10**9+7

step4 = [(0,-1),(1,0),(0,1),(-1,0)]
step8 = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_():
    return [eval(s)-1 for s in sys.stdin.readline().split()]
def LF():
    return [float(x) for x in sys.stdin.readline().split()]
def LS():
    return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
S = lambda : input()
def pf(s): print(s, flush=True)

def main():
    result = []

    while True:
        n = I()
        if not n:
            break
        pairs = [LS() for __ in range(n)]
        start = S()
        target = S()
        m = len(target)
        if start == target:
            result.append(0)
            continue

        universe = set()
        queue = set()
        universe.add(start)
        queue.add(start)
        depth = 0
        answer = -1

        while queue:
            depth += 1
            next_queue = set()
            for current in queue:
                for src, dst in pairs:
                    temp = current.replace(src, dst)
                    if len(temp) > m:
                        continue
                    next_queue.add(temp)
            if target in next_queue:
                answer = depth
                break
            queue = next_queue - universe
            universe |= next_queue
        result += [answer]

    return '\n'.join(map(str, result))


if __name__=='__main__':
    print(main())