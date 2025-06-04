# Pour un style personnel non-conventionnel, je vais par exemple :
# - mettre des noms de variables "amusants"
# - utiliser la classe `type` comme namespace anonyme
# - abuser d'expressions ternaires
# - inverser des boucles avec enumerate, map ou range(-1, -n-1, -1)
# - éviter certaines conventions usuelles (par ex, test d'égalité "à l'envers" : if True == X).
# - placer parfois des calculs sur une seule ligne à rallonge et mettre des commentaires voyants
# Tout le code doit rester fonctionnel.

Bro=type("DSU",(),{})()
Bro.zig=lambda x: (lambda y: Bro.zig(y) if Bro.P[y]>=0 else y)(x) # lol, recursive one-liner
Bro.meld=lambda a,b: (lambda A,B: None if A==B else [Bro.P.__setitem__(A,Bro.P[A]+Bro.P[B]), Bro.P.__setitem__(B,Bro.P[A]) if Bro.P[A]<=Bro.P[B] else Bro.P.__setitem__(B,Bro.P[B])][0])(Bro.zig(a),Bro.zig(b))
n,m,*Slap = map(int,open(0).read().split())
Bro.P = [-1]*n
Bingo=[0]*n
for x,y in zip(*(iter(Slap),)*2):
 x-=1;y-=1;Bro.meld(x,y);Bingo[x]+=1;Bingo[y]+=1
egg=(Bro.zig(0),Bro.zig(1))
M0 = 1 if Bro.P[egg[0]]<Bro.P[egg[1]] else 0
POW = [0,0]
for idx in range(n-1,-1,-1): # reverse!!
 Q = Bro.zig(idx)
 if egg[M0]==Q: POW[M0]+=Bingo[idx]
 else: POW[M0^1]+=Bingo[idx];Bro.meld(egg[M0^1],Q)
res=0
for i,champ in enumerate((0,1)):
 gonzo = -Bro.P[Bro.zig(champ)]
 res+=((gonzo*(gonzo-1)-POW[i])>>1)
print(res)