from sys import setrecursionlimit
setrecursionlimit(10**7)

def solve(AB):
    used = [False]*10
    for v in AB:
        if v != -1:
            used[v] = True

    missing = [i for i, v in enumerate(AB) if v == -1]
    digits = [i for i in range(1,10) if not used[i]]

    count = 0

    def check(a,b,c,d,e,f,g,h,i):
        # a,b,c
        # d,e,f
        # g,h,i
        # conditions reproduce the sum implied by the example (筆算)
        # We consider the sum:
        # A B C
        # + D E F
        # --------
        # G H I

        # So ABC + DEF = GHI
        abc = a*100 + b*10 + c
        def_ = d*100 + e*10 + f
        ghi = g*100 + h*10 + i
        return abc + def_ == ghi

    def backtrack(idx, arr):
        nonlocal count
        if idx == len(missing):
            # all assigned, check condition
            a,b,c,d,e,f,g,h,i = arr
            if check(a,b,c,d,e,f,g,h,i):
                count += 1
            return

        for dig in digits:
            if not used[dig]:
                used[dig] = True
                arr[missing[idx]] = dig
                backtrack(idx+1, arr)
                used[dig] = False
                arr[missing[idx]] = -1

    backtrack(0, AB[:])
    print(count)

AB = list(map(int, input().split()))
solve(AB)