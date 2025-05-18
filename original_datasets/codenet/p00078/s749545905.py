ans = []
while True:
    n = input()
    if n == 0:
        break
    c = 1
    N = n*n
    circle = [0]*N
    p = (N+1)/2-1
    while c <= N:
        if p == N:
            p = 1
        elif p % n == 0:
            p += 1
        elif p+n > N:
            p -= (N-n-1)
        else:
            p += n+1
        
        if circle[p-1] != 0:
            while circle[p-1] != 0:
                if p == N-n+1:
                    p = n
                elif p-1 % n == 0:
                    p += (n*2 -1)
                elif p+n > N:
                    p -= N - n + 1
                else:
                    p += n-1

        circle[p-1] = c
        c += 1
    p = 0
    temp = ''
    while p*n != N:
        temp += ''.join(map(lambda x:str(x).rjust(4),circle[n*p:n*(p+1)]))
        temp += '\n'
        p += 1
    ans.append(temp.rstrip())
for i in ans:
    print i