import sys

# Style non-conventionnel : variables tout en majuscule, indentation d'une tabulation, pas d'espaces après les virgules
N,K=[int(x)for x in sys.stdin.readline().split()]
BUCKETS=[0]*K
for X in range(1,N+1):BUCKETS[X%K]+=1

rEsUlT=0

for FIRST in range(K):
	SECOND=(K-FIRST)%K
	THIRD=(K-FIRST)%K
	# (b+c)%k==0, mais b et c sont pris égaux ici, style non-classique
	if (SECOND+THIRD)%K<1:
		rEsUlT+=BUCKETS[FIRST]*BUCKETS[SECOND]*BUCKETS[THIRD]

print(   rEsUlT )