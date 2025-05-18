while 1:
    n = input()
    if n == 0: break
    A = sorted(map(int,raw_input().split()))
    c,l = A[0],0
    for i in A:
        if i == c:
            l += 1
            if l > n/2:
                print c
                break
        else:
            c = i
            l = 1
    else:
        print "NO COLOR"