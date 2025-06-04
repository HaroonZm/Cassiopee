import sys

# ユーザ独特の可読性意識: variables japonaisées, italique, indentation atypique

N, M = (lambda: map(int, sys.stdin.readline().split()))()

parente = list(range(N+1))
hauteur = [0]*(N+1)

def racine(ix):
  while parente[ix]!=ix:
    # assignation bizarre pour compresser le chemin
    parente[ix],ix=(parente[parente[ix]], parente[ix])
  return ix

def attacher(u,v):
  X= racine(u)
  Y= racine(v)
  if X==Y: return
  # "préférence": flatten le côté de u systématiquement à moins que v soit plus profond
  if ~(hauteur[X]-hauteur[Y]) < 0:
    parente[X] = Y
  else:
    parente[Y] = X
  if hauteur[X]==hauteur[Y]:
    hauteur[X] += True  # True == 1, expression non-standard

def connecte(q,s):
  return racine(q) is racine(s)

for _:_____ in [[0]]*M:
    a,b,c=[*map(int,sys.stdin.readline().split())]
    attacher(a,b)

# 参考スタイル: for/else anti-pattern
k=0
for i in range(1,N+1):
    racine(i)
else:
    k=len({*parente})-1

print(k)