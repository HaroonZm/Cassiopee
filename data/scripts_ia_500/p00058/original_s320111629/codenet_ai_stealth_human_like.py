import sys

# Bon, on va lire ligne par ligne depuis l'entrée standard
for line in sys.stdin:
    x1,y1,x2,y2,x3,y3,x4,y4 = map(float, line.split())
    
    # Un truc pour vérifier une condition un peu bizarre ici
    val = (x2 - x1)*(y4 - y3) + (y2 - y1)*(x4 - x3)
    # Si la valeur est quasi nulle, on dit "YES", sinon "NO"
    if abs(val) < 1e-10:
        result = "YES"
    else:
        result = "NO"
    print(result)  # Voilà le résultat imprimé comme demandé