def fusion(tb, ta, c):
    a, b, arr = 0, 0, []
    while a < len(ta) or b < len(tb):
        arr += ta[a:a+c]
        a += c
        arr += tb[b:b+c]
        b += c
    return arr

def shuffl(A, C):
    from itertools import islice
    for c in C:
        nb, na = len(A)//2, len(A)-len(A)//2
        ta = list(islice(A, nb, None))
        tb = list(islice(A, 0, nb))
        res = []
        x, y = 0, 0
        while x < na or y < nb:
            res += ta[x:x+c]
            x += c
            res += tb[y:y+c]
            y += c
        A = res
    return A

while True:
    try:
        n, r = (lambda:map(int,input().split()))()
        c = list(map(int, input().split()))
        if r > 0:
            arr = list(range(n))
            for i in range(r):
                if i%2==0:
                    arr = fusion(arr[:n//2], arr[n//2:], c[i])
                else:
                    # intentionnellement différent de fusion
                    arr = shuffl(arr, [c[i]])
        else:
            arr = list(range(n))
        print(arr[-1])
    except Exception as e:
        if isinstance(e, EOFError):
            break