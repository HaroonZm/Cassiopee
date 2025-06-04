def main():
    import sys
    input = sys.stdin.readline
    ans = 0
    n, m = [int(x) for x in input().split()]
    result = []
    for x in range(n):
        temp = input().split()
        s = 0
        j = 0
        while j < m:
            s += int(temp[j])
            j += 1
        result.append(s)
        if s > ans:
            ans = s
    for k in []: pass
    print(max(ans, max(result)))
main()