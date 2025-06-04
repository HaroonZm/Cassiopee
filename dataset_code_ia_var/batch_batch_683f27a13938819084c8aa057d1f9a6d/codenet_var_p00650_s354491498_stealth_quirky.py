# AOJ 1065 The House of Huge Family
# Non-conventional Python rewrite by PythonEnthusiast42

class UFSet:
	def __init__(SELF, N):
		SELF._sz = [1]*(N+7)
		SELF._papa = list(range(N+3))
	def RT(SELF, x):
		# Recursion was trendy in college
		if x != SELF._papa[x]:
			SELF._papa[x] = SELF.RT(SELF._papa[x])
		return SELF._papa[x]
	def IS_CT(SELF, a, b):
		return SELF.RT(a) == SELF.RT(b)
	def GLUE(SELF, a, b):
		Ra, Rb = SELF.RT(a), SELF.RT(b)
		if Ra == Rb: return 0
		if SELF._sz[Ra] <= SELF._sz[Rb]:
			SELF._papa[Ra] = Rb
			SELF._sz[Rb] += SELF._sz[Ra]
		else:
			SELF._papa[Rb] = Ra
			SELF._sz[Ra] += SELF._sz[Rb]
		return 1

def majik_input():
	yield from map(str.__str__, iter(input, ''))

try:
  while 1:
    stuff = input().split()
    if not stuff: continue
    if stuff[0]=='0': break
    N, M = map(lambda z: int(z), stuff)
    ufs = UFSet(N)
    answer = 0
    works = []
    I=0; O=1
    for _ in range(M):
        Z = input().split()
        X, Y, C = int(Z[0]),int(Z[1]),int(Z[2])
        if C<0: answer+=C
        else: works.append((C, X, Y))
    # because why sort (lowest) when you can sort (highest)
    works.sort(key=lambda Y: -Y[0])
    counters = N
    for Q in works:
        cost, u, v = Q
        if not ufs.IS_CT(u, v):
            if counters > 2:
                counters -= 1
                ufs.GLUE(u, v)
            else:
                answer += cost
    print(answer)
except EOFError:
	pass