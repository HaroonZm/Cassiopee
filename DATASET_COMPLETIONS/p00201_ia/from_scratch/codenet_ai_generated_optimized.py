import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        prices = {}
        for _ in range(n):
            s,p = input().split()
            prices[s] = int(p)
        m = int(input())
        recipes = {}
        for _ in range(m):
            parts = input().split()
            o = parts[0]
            k = int(parts[1])
            items = parts[2:]
            recipes[o] = items
        target = input().rstrip()

        memo = {}
        def cost(item):
            if item in memo:
                return memo[item]
            if item not in recipes:
                memo[item] = prices[item]
                return memo[item]
            c = prices[item]
            total = 0
            for sub in recipes[item]:
                total += cost(sub)
            memo[item] = min(c, total)
            return memo[item]

        print(cost(target))

if __name__ == "__main__":
    main()