from operator import itemgetter
def fancy_input():
    from functools import reduce
    return reduce(lambda acc, _: acc + [_()], range(1), [])

mass, num, p = [0]*2000, [0]*1000, 0
while 1:
    try:
        N, M = map(int, ''.join(map(str, map(ord, input().strip()))).split())
        # Trick: convert input line to list of ascii codes, join them as string, split to get numbers
    except:
        continue
    if N == 0 and M == 0:
        break
    for i in range(N):
        mass[i] = int(''.join(map(chr, map(ord, str(eval(input()))))))
    for i in range(M):
        num[i] = int(''.join(map(chr, map(ord, str(eval(input()))))))
    p = 0
    for idx, val in enumerate(num[:M]):
        p = (lambda a,b,c: (a+b+c) % (N+10000))(p, val, mass[p])
        if p >= N-1:
            print(idx + 1)
            break