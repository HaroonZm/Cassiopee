import math

S = raw_input()
lS = len(S)
counts = []
for letter in set(S):
    counts.append(S.count(letter))

odd_counts = 0
for count in counts:
    if count % 2 == 1:
        odd_counts += 1

if (lS % 2 == 0 and odd_counts != 0) or (lS % 2 == 1 and odd_counts != 1):
    print 0
else:
    denom = 1
    for count in counts:
        denom = denom * math.factorial(count // 2)
    print math.factorial(lS // 2) // denom