def solve(N):
    k = 0
    rng = 0
    for i in range(54):
        if cl[i] < N <= cl[i+1]:
            k = i + 2
            rng2 = cl[i]
            rng = cl[i+1] - cl[i]
    # print(k)
    posrng = (N-rng2)%(rng//9)
    perrng = (N-rng2)//(rng//9)+1
    if posrng == 0:
        posrng = rng//9
        perrng -= 1
    ans = [perrng]
    for i in range(k-1):
        if i == k-2:
            tmp = [0 if j == perrng else 1 for j in range(10)]
        else:
            tmp = [(cl[k-i-2]-cl[k-i-3])//9 if j == perrng else 2**(k-i-2) for j in range(10)]
        if posrng <= tmp[0]:
            ans.append(0)
            # posrng = posrng
        for j in range(1, 10):
            tmp[j] += tmp[j-1]
            if tmp[j-1] < posrng <=tmp[j]:
                ans.append(j)
                posrng -= tmp[j-1]
        if max(ans) != min(ans):
            break
    for i in range(k-len(ans), 0, -1):
        if posrng <= 2**(i-1):
            ans.append(min(ans))
        else:
            ans.append(max(ans))
            posrng -= 2**(i-1)
    print(''.join(map(str, ans)))

cl = [sum([9*2**j for j in range(i)])*9 for i in range(55)]
for i in range(1, 55):
    cl[i] += cl[i-1]
while True:
    N = int(input())
    if N == 0:
        break
    solve(N)