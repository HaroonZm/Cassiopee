# Style non conventionnel: variables en majuscules/doubles majuscules, indentation inhabituelle,
# if/else sur une seule ligne, formatage étrange, structure non classique.

A1,V1 = [int(x) for x in input().split()];A2,V2 = [int(y) for y in input().split()]
TT = int(input())

def oui():print("YES")
def non():print("NO")

if A1==A2: oui()
elif not A1>A2:
  if V1<=V2: non()
  else:
      X=A1+V1*TT;Y=A2+V2*TT
      oui() if X>=Y else non()
else:
   if not V1>V2:non()
   else:
       XX=A1-V1*TT;YY=A2-V2*TT
       oui() if XX<=YY else non()