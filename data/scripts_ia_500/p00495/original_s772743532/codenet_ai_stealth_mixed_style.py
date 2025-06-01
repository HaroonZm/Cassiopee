def solve():
    A, B = [int(x) for x in input().split()]
    s1 = tuple(map(int, input().split()))
    s2 = tuple(int(x) for x in input().split())
    result = 0

    i = 0
    while i < B:
        k = 0
        cnt = 0
        j = 0
        for n in s2[i:]:
            for m in s1[k:]:
                k += 1
                if n == m:
                    cnt += 1
                    break
            j += 1
        if cnt > result:
            result = cnt
        if result >= B - i:
            break
        i += 1

    print(result)

if __name__ == "__main__":
    solve()