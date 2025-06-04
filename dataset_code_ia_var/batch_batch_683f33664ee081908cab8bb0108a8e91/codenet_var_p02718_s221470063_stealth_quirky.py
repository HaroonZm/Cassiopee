gimme = lambda : [int(x) for x in input().split()]
N, M = gimme()
A = gimme()

TOTAL = sum(A)

decision = lambda sc: sc * 4 * M >= TOTAL

vote = sum(decision(a) for a in A)

print(['No', 'Yes'][vote >= M])