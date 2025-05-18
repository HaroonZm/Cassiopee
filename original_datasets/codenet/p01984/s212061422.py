N = int(input())
while N:
    l = 2
    N -= 1
    while N >= ((1<<(l - 1)) - 1)*81:
        N -= ((1<<(l - 1)) - 1)*81
        l += 1
    s = N // (((1<<(l - 1)) - 1)*9) + 1
    N %= ((1<<(l - 1)) - 1)*9
    t = -1
    ans = str(s)
    #print("N = ", N)
    while t < 0:
        for i in range(s):
            if(N >= (1<<(l - 2))):
                N -= (1<<(l - 2))
            else:
                t = i
                break

        if t >= 0:
            continue

        if N >= ((1<<(l - 2)) - 1)*9:
            N -= ((1<<(l - 2)) - 1)*9
            for i in range(s+1, 10):
                if N >= (1<<(l-2)):
                    N -= (1<<(l-2))
                else:
                    t = i
                    break
        else:
            l -= 1
            ans += str(s)
    #print("N = ", N)
    ans += str(t)
    if s > t:
        b = bin(N)[2:]
        ans_ = str(t)*(l - 1 - len(b))
        C = [str(t), str(s)]
    else:
        b = bin(N)[2:]
        ans_ = str(s)*(l - 1 - len(b))
        C = [str(s), str(t)]

    for i in range(len(b)):
        ans_ += C[int(b[i])]
    print(ans+ans_[1:])
    N = int(input())