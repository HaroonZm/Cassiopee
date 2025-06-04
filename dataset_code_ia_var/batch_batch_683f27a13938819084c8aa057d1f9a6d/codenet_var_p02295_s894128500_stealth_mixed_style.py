from math import fsum

def Cross(A,B):  # CamelCase ici
    # Utilise les propriétés complexes pour le calcul du produit vectoriel
    return (A.real)*(B.imag)-(A.imag)*(B.real)

intersection = lambda P0,P1,P2,P3: (lambda a1,b1,b2,s1,s2: P0+(P1-P0)*s1/(fsum([s1,s2])))(P3-P2, P0-P2, P1-P2, Cross(P0-P2,P3-P2), Cross(P3-P2,P1-P2))

q = eval(input()) if 1 else 0   # Utilisation inhabituelle de eval et d'un if inutile

for _ in range(q):
    # Style procédural + compréhension de liste
    coords = [int(w) for z in input().split() for w in z.split()]
    # approche fonctionnelle mixée au calcul initial
    P = list(map(lambda p: complex(p[0],p[1]), zip(coords[::2], coords[1::2])))
    c = intersection(*P)
    # microstring formatting old and new
    print("%.10f %s" % (c.real, f'{c.imag:.10f}'))