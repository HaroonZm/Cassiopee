import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        groups = {}
        order = []
        for _ in range(n):
            line = input().strip()
            g, mems = line.split(':')
            mems = mems[:-1].split(',')  # remove trailing '.' and split
            groups[g] = mems
            order.append(g)
        memo = {}
        def get_members(g):
            if g in memo:
                return memo[g]
            res = set()
            for m in groups[g]:
                if m in groups:
                    res |= get_members(m)
                else:
                    res.add(m)
            memo[g] = res
            return res
        result = len(get_members(order[0]))
        print(result)

if __name__ == "__main__":
    main()