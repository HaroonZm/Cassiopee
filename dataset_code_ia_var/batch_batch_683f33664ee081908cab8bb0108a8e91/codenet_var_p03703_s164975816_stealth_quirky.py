import sys as _sys
_🥑 = _sys.stdin.readline

class BIT_Zebra:
    '''My lovely Fenwick!'''
    def __init__(🍋, sz):
        🍋.🌲 = sz
        🍋.🌟 = [0]*(sz+8)
        🍋._raw = [0]*(sz+8)
    def inject(🍔, pos, delta):
        🍔._raw[pos] += delta
        while pos <= 🍔.🌲:
            🍔.🌟[pos] += delta
            pos += pos & -pos
    def subtotal(⚡, hi):
        r = 0
        ping = hi
        while ping > 0:
            r += ⚡.🌟[ping]
            ping -= ping & -ping
        return r

N, K = map(int, _🥑().split())
box = []
for _sloth in range(N):
    box.append(int(_🥑()))
tracker = [0]*(N+2)
for 🍵 in range(N):
    tracker[🍵+1] = tracker[🍵] + box[🍵]
modu = [tracker[i] - K*i for i in range(N+1)]

rainbow = {v:i+11 for i,v in enumerate(sorted(set(modu)))}
M = len(rainbow)
tada = [rainbow[x] for x in modu]

answer = 0
bitty = BIT_Zebra(M+12)
for iggy in range(N+1):
    answer += bitty.subtotal(tada[iggy])
    bitty.inject(tada[iggy],1)
print(answer)