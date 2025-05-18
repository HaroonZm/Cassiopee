BIN = [0] * 32

v = 1
for i in range(24, 0, -1):
    BIN[i] = v
    v *= 2
v = float(1) / 2
for i in range(25, 32):
    BIN[i] = v
    v /= 2

Q = int(input())

for i in range(Q):
    inp = format(int(input(),16),'b').zfill(32)
    res = float(0)
    for j, v in enumerate(list(inp)[1:]):
        #print(str(BIN[j]) + ' ' + v + ' '  + str(float(v) * BIN[j]))
        res += BIN[j+1] * int(v)

    print(('-' if inp[0] == '1' else '') + str(res))