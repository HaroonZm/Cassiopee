import sys
sys.setrecursionlimit(10**7)

def solve():
    input = sys.stdin.readline
    while True:
        n = input()
        if not n:
            break
        n = int(n)
        if n == 0:
            break
        price = {}
        for _ in range(n):
            s, p = input().split()
            price[s] = int(p)
        m = int(input())
        recipes = {}
        for _ in range(m):
            line = input().split()
            o = line[0]
            k = int(line[1])
            ingredients = line[2:]
            recipes[o] = ingredients
        t = input().strip()
        memo = {}
        def min_cost(item):
            if item in memo:
                return memo[item]
            res = price[item]
            if item in recipes:
                cost = sum(min_cost(i) for i in recipes[item])
                if cost < res:
                    res = cost
            memo[item] = res
            return res
        print(min_cost(t))

if __name__ == "__main__":
    solve()