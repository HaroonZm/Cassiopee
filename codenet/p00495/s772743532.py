def solve():
    A, B = map(int, input().split())
    s1 = tuple(map(int, input().split()))
    s2 = tuple(map(int, input().split()))
    result = 0

    for i in range(B):
        k = 0
        cnt = 0
        for j, n in enumerate(s2[i:]):
            for m in s1[k:]:
                k += 1
                if n == m:
                    cnt += 1
                    break
        if cnt > result:
            result = cnt
        if result >= B-i:
            break
    print(result)

if __name__ == "__main__":
    solve()