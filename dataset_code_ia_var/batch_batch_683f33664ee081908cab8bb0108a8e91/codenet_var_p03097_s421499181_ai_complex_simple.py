import sys
import itertools
import functools
import operator

PTN00 = list(itertools.starmap(lambda x, y: [x, y], itertools.product(['00', '01', '11', '10'], ['10', '11', '01', '00'])))
PTN11 = list(itertools.starmap(lambda x, y: [x, y], itertools.product(['00', '01', '11', '10'], ['10', '00', '01', '11'])))
PTNEVEN = list(map(lambda i: ''.join(sorted('01', reverse=bool(i))), range(2)))

def parity(n):
    return functools.reduce(operator.xor, map(int, bin(n)[2:]), 0)

def dfs(digit, ptnNow, current_parity, isLast, 
        result_collector, 
        cache={'ptn00':PTN00[0],'ptn11':PTN11[0],'ptnEven':PTNEVEN}):
    if digit == maxDigit:
        if N & 1:
            result_collector.append(ptnNow)
        else:
            result_collector.extend([ptnNow + cache['ptnEven'][current_parity][0], ptnNow + cache['ptnEven'][current_parity][1]])
        return

    cond = digit <= numDiff//2 and current_parity and isLast
    patterns = (enumerate(cache['ptn11'][1]) if cond else enumerate(cache['ptn00'][current_parity]))
    for v, p in patterns:
        dfs(digit+1, ptnNow+p, v & 1, isLast if v == 3 else 0, result_collector, cache)

N, A, B = map(int, next(iter(sys.stdin.readline, input)).split())

binA = '{:0{}b}'.format(A, N)
binB = '{:0{}b}'.format(B, N)
numDiff = sum(map(operator.ne, binA, binB))

if not numDiff & 1:
    print('NO')
    sys.exit()

numSame = N - numDiff
maxDigit = 1 + numDiff // 2 + numSame // 2

ptnCollect = []
dfs(1, '0', 0, False, ptnCollect)
dfs(1, '1', 1, True, ptnCollect)

indexify = lambda seq: functools.reduce(lambda acc, x: acc + [acc[-1]+(seq[acc[-1]]!=seq2[acc[-1]]) if acc else int(seq[0]!=seq2[0])], range(1, len(seq)), [0])
conv2digitPtns = []
digitDiff, digitSame = 0, numDiff
for i, (Ai, Bi) in enumerate(zip(binA, binB)):
    conv2digitPtns.append(digitSame if Ai == Bi else digitDiff)
    if Ai == Bi:
        digitSame += 1
    else:
        digitDiff += 1

def compose_bits(ptn, mapping):
    return functools.reduce(operator.add, (ptn[c] for c in mapping), '')

anss = list(map(lambda p: int(compose_bits(p, conv2digitPtns), 2) ^ A, ptnCollect))

print('YES')
print(' '.join(map(str, anss)))