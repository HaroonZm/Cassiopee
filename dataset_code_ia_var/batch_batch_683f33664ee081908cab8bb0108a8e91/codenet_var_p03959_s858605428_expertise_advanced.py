from sys import stdin
from functools import reduce

MOD = 10**9 + 7

def main():
    n = int(stdin.readline())
    arr1 = list(map(int, stdin.readline().split()))
    arr2 = list(map(int, stdin.readline().split()))

    a = [-1] * n
    b = [-1] * n

    # Process a (left to right)
    curr = arr1[0]
    a[0] = curr
    for i in range(1, n):
        if arr1[i] == 1:
            a[i] = 1
        elif arr1[i] != curr:
            curr = arr1[i]
            a[i] = curr

    # Process b (right to left)
    curr = arr2[-1]
    b[-1] = curr
    for i in range(n-2, -1, -1):
        if arr2[i] == 1:
            b[i] = 1
        elif arr2[i] != curr:
            curr = arr2[i]
            b[i] = curr

    flag = False
    c = [-1] * n

    for i in range(n):
        ai, bi, ar1, ar2 = a[i], b[i], arr1[i], arr2[i]
        if ai == -1 and bi == -1:
            pass
        elif ai == -1:
            if ar1 < bi:
                flag = True
                break
            c[i] = bi
        elif bi == -1:
            if ar2 < ai:
                flag = True
                break
            c[i] = ai
        else:
            if ai != bi:
                flag = True
                break
            c[i] = ai

    if flag:
        print(0)
        return

    ans = 1
    i = 0
    while i < n:
        if c[i] == -1:
            l = c[i-1] if i > 0 else arr1[0]
            j = i
            while j < n and c[j] == -1:
                j += 1
            r = c[j] if j < n else arr2[-1]
            m = min(l, r)
            ans = (ans * pow(m, j - i, MOD)) % MOD
            i = j
        else:
            i += 1
    print(ans)

if __name__ == "__main__":
    main()