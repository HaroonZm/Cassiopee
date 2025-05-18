import sys

ptn00 = [['00', '01', '11', '10'], ['10', '11', '01', '00']]
ptn11 = [['00', '01', '11', '10'], ['10', '00', '01', '11']]
ptnEven = ['01', '10']

# [00…0]（全ての桁が0）から[1…10…0]（先頭のnumDiff桁が1）まで、
# ちょうど1ビットずつ変化するパターン（重複なし）を生成する
def dfs(digit, ptnNow, parity, isLast):
    if digit == maxDigit:
        if N % 2:
            ptns.append(ptnNow)
        else:
            # Nが偶数の場合、長さを調整する
            ptns.append(ptnNow+ptnEven[parity][0])
            ptns.append(ptnNow+ptnEven[parity][1])
        return

    if digit <= numDiff//2 and parity and isLast:
        # [11]になるビットの場合、最後だけ基本パターンから逸脱する
        for v, p in enumerate(ptn11[1]):
            dfs(digit+1, ptnNow+p, v%2, isLast if v == 3 else 0)
    else:
        # [00]になる2ビットの場合
        for v, p in enumerate(ptn00[parity]):
            dfs(digit+1, ptnNow+p, v%2, isLast if v == 3 else 0)

N, A, B = map(int, input().split())

binA, binB = bin(A)[2:].zfill(N), bin(B)[2:].zfill(N)
numDiff = sum([Ai != Bi for Ai, Bi in zip(binA, binB)])

if numDiff % 2 == 0:
    print('NO')
    sys.exit()

numSame = N - numDiff
maxDigit = 1 + numDiff//2 + numSame//2

ptns = []
dfs(1, '0', 0, False)
dfs(1, '1', 1, True)

# A→Bでの変化有無に応じて、各ビットを並べ替える
conv2digitPtns = []
digitDiff, digitSame = 0, numDiff
for i, (Ai, Bi) in enumerate(zip(binA, binB)):
    if Ai == Bi:
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
    ans = int(ans, 2) ^ A
    anss.append(ans)

print('YES')
print(' '.join(map(str, anss)))