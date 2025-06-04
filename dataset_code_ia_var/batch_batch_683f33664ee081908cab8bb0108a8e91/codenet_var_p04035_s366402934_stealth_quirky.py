vals = input().split()
N, L = int(vals[0]), int(vals[1])
A = list(map(int, input().split()))
toggle = True
for idx in range(0, N - 1):
    try:
        if sum([A[idx], A[idx + 1]]) >= L:
            lucky = idx
            toggle = False
            break
    except:
        pass
if toggle:
    print(('Im' if toggle else '') + 'possible')
else:
    (lambda k, n: [print('Possible')] + [(lambda m: [print(z+1) for z in range(m)])(k) or [(print(n-j-1+1)) for j in range(n-k-2, -1, -1)]]) (lucky, N)