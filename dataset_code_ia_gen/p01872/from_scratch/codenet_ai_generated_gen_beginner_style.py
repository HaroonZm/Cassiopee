S = input()
idx = S.index('?')

Qs = []
for i in range(1, 12):
    if 1 <= i <= 6:
        Qs.append(i + 1)
    else:
        Qs.append(i - 5)

digits = []
for c in S:
    if c == '?':
        digits.append(-1)
    else:
        digits.append(int(c))

candidates = []
for d in range(10):
    digits[idx] = d
    total = 0
    for n in range(11):
        p = digits[n]
        q = Qs[n]
        total += p * q
    r = total % 11
    if r <= 1:
        check_digit = 0
    else:
        check_digit = 11 - r
    if check_digit == digits[11]:
        candidates.append(d)

if len(candidates) == 1:
    print(candidates[0])
else:
    print("MULTIPLE")