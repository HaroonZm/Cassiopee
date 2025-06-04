import sys

ptn00 = [['00', '01', '11', '10'], ['10', '11', '01', '00']]
ptn11 = [['00', '01', '11', '10'], ['10', '00', '01', '11']]
ptnEven = ['01', '10']

N, A, B = map(int, input().split())

binA = bin(A)[2:].zfill(N)
binB = bin(B)[2:].zfill(N)
numDiff = 0
for a, b in zip(binA, binB):
    if a != b:
        numDiff += 1

if numDiff % 2 == 0:
    print('NO')
    sys.exit()

numSame = N - numDiff
maxDigit = 1 + numDiff//2 + numSame//2

ptns = []
stack = []
stack.append((1, '0', 0, False))
stack.append((1, '1', 1, True))
while stack:
    digit, ptnNow, parity, isLast = stack.pop()
    if digit == maxDigit:
        if N % 2:
            ptns.append(ptnNow)
        else:
            ptns.append(ptnNow + ptnEven[parity][0])
            ptns.append(ptnNow + ptnEven[parity][1])
        continue
    if digit <= numDiff//2 and parity and isLast:
        for v, p in enumerate(ptn11[1]):
            stack.append((digit+1, ptnNow+p, v%2, isLast if v == 3 else 0))
    else:
        for v, p in enumerate(ptn00[parity]):
            stack.append((digit+1, ptnNow+p, v%2, isLast if v == 3 else 0))

conv2digitPtns = []
digitDiff = 0
digitSame = numDiff
for i in range(N):
    if binA[i] == binB[i]:
        conv2digitPtns.append(digitSame)
        digitSame += 1
    else:
        conv2digitPtns.append(digitDiff)
        digitDiff += 1

anss = []
for ptn in ptns:
    ans = ''
    for c in conv2digitPtns:
        ans += ptn[c]
    ansN = int(ans, 2) ^ A
    anss.append(ansN)

print('YES')
print(' '.join(map(str, anss)))