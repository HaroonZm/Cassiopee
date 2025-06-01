def solve():
    A, B = map(int, input().split())
    s1 = tuple(map(int, input().split()))
    s2 = tuple(map(int, input().split()))

    result = 0
    for i in range(B):
        iter_s1 = iter(s1)
        cnt = sum(1 for n in s2[i:] if any(m == n for m in iter_s1))
        if cnt > result:
            result = cnt
        if result >= B - i:
            break
    print(result)

if __name__ == "__main__":
    solve()