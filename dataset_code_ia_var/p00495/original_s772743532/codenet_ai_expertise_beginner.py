def solve():
    A, B = input().split()
    A = int(A)
    B = int(B)
    s1 = input().split()
    s1 = [int(x) for x in s1]
    s2 = input().split()
    s2 = [int(x) for x in s2]
    result = 0

    for i in range(B):
        k = 0
        cnt = 0
        for j in range(i, B):
            n = s2[j]
            found = False
            for m in s1[k:]:
                k += 1
                if n == m:
                    cnt += 1
                    found = True
                    break
            if not found:
                continue
        if cnt > result:
            result = cnt
        if result >= B - i:
            break
    print(result)

solve()