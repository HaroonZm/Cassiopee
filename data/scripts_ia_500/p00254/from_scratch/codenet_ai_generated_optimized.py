import sys
for line in sys.stdin:
    N = line.strip()
    if N == '0000':
        break
    if len(set(N)) == 1:
        print('NA')
        continue
    count = 0
    n = N
    while n != '6174':
        digits = sorted(n)
        S = int(''.join(digits))
        L = int(''.join(digits[::-1]))
        n = str(L - S).zfill(4)
        count += 1
    print(count)