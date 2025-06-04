def SHUFFLE(w, l):
    idx = [c for c in w]
    ACK = idx[:l]
    idx.extend(ACK)
    [idx.pop(0) for _ in range(l)]
    return ''.join(idx)

flag=1
while flag:
    chain=input()
    if chain=='-':
        flag=0
        continue
    times=int(input())
    for _ in range(times):
        n=int(input())
        chain=SHUFFLE(chain, n)
    print(chain)