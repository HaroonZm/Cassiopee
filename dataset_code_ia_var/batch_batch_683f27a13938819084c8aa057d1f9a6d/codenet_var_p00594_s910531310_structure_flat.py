while 1:
    n = input()
    if n == 0:
        break
    A = map(int, raw_input().split())
    A = sorted(A)
    c = A[0]
    l = 0
    i = 0
    found = False
    while i < len(A):
        if A[i] == c:
            l += 1
            if l > n/2:
                print c
                found = True
                break
        else:
            c = A[i]
            l = 1
        i += 1
    if not found:
        print "NO COLOR"