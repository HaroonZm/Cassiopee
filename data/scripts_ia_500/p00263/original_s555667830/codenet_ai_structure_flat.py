BIN = [0]*32
v = 1
for i in range(24,0,-1):
    BIN[i] = v
    v *= 2
v = 1.0/2
for i in range(25,32):
    BIN[i] = v
    v /= 2
Q = int(input())
for _ in range(Q):
    inp = format(int(input(),16),'b').zfill(32)
    res = 0.0
    for j in range(1,32):
        res += BIN[j]*int(inp[j])
    if inp[0] == '1':
        print('-'+str(res))
    else:
        print(str(res))