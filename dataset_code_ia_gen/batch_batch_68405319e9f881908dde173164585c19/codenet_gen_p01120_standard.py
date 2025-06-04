def main():
    import sys
    input = sys.stdin.readline
    while True:
        n,m = map(int,input().split())
        if n == 0 and m == 0:
            break
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        diff = [(b[i]-a[i])%m for i in range(n)]
        ops = 0
        i = 0
        while i < n:
            if diff[i] == 0:
                i += 1
                continue
            val = diff[i]
            ops += val
            while i < n and diff[i] == val:
                i += 1
        print(ops)
main()