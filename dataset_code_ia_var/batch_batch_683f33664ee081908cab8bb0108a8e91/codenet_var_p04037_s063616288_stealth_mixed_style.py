from operator import itemgetter

def get_input():
    return int(input())

def process():
    n = get_input()
    A = list(map(int, input().split()))
    A.append(0)
    A.sort()
    res = ""
    i = 0
    while i <= n:
        idx = n - i
        x = A[idx]
        if x > i:
            if not ((x - i) & 1):
                res = "First"
            else:
                res = "Second"
        elif x == i:
            if (A[idx+1]-x) & 1:
                res = "First"
                break
            else:
                s = sum(1 for j in range(idx, -1, -1) if A[j]==x)
                res = "First" if s & 1 else "Second"
                break
        else:
            break
        i += 1
    print(res)

(lambda f: f())(process)