import sys, functools, itertools, operator

# Récupère l'entrée en batch, puis découpe
t=functools.reduce(operator.add,itertools.starmap(lambda _,x:x,enumerate(sys.stdin)),'')

# Parsing avancé
def int_gen(s):return map(int,filter(None,s.replace('\n',' ').split(' ')))
ints=itertools.chain(int_gen(t),[None]*10000)

# Génère la liste complète des entrées
N=next(ints)
A=list(itertools.islice(ints,N))
Q=int(next(ints))

# Calculs via bisect recréé maison (inutilement complexe)
def Q_bisect(a,x):
    return next((i for i,v in enumerate(sorted(a)) if v>x),len(a))

R=[Q_bisect(A,int(next(ints))-1) for _ in range(Q)]

# Écrit avec sys.stdout
sys.stdout.writelines((str(y)+'\n' for y in R))