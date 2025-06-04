import sys
import string
from collections import defaultdict

sys.setrecursionlimit(1 << 20)
inf = float('inf')
eps = 1e-10
mod = 10**9 + 7
DIR4 = [(-1,0),(0,1),(1,0),(0,-1)]
DIR8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

input = sys.stdin.readline

def ints(): return list(map(int, input().split()))
def ints0(): return [x-1 for x in map(int, input().split())]
def floats(): return list(map(float, input().split()))
def str_list(): return input().split()
def int1(): return int(input())
def float1(): return float(input())
def str1(): return input().rstrip()
def pf(s): print(s, flush=True)

def main():
    results = []

    while True:
        n = int1()
        if not n:
            break

        words = [str1() for _ in range(n)]
        graph = defaultdict(set)
        graph[''].update(string.ascii_lowercase)

        valid = True
        for i, ai in enumerate(words):
            for aj in words[i+1:]:
                for k, ca in enumerate(ai):
                    if k >= len(aj):
                        valid = False
                        break
                    if ca == aj[k]:
                        continue
                    graph[ca].add(aj[k])
                    break
                else:
                    if len(ai) > len(aj):
                        valid = False
                if not valid:
                    break
            if not valid:
                break

        if not valid:
            results.append('no')
            continue

        state = defaultdict(int)  # 0=unvisited, 1=visiting, 2=visited
        state[''] = 2

        def dfs(u):
            nonlocal state, graph
            if state[u] == 1:
                return False
            if state[u] == 2:
                return True
            state[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False
            state[u] = 2
            return True

        if all(state[c] or dfs(c) for c in list(graph)):
            results.append('yes')
        else:
            results.append('no')

    return '\n'.join(results)

print(main())