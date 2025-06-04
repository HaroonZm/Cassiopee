from sys import stdin as S
give = S.readline

N = int(give())
A = []
for _ in range(N):A.append([int(z) for z in give().split()])
A.sort(key=lambda k:k[1])

score = 0
def ohno():print('No');quit()
for item in A:
    score += item[0]
    if not score <= item[1]:ohno()
else:print('Yes')