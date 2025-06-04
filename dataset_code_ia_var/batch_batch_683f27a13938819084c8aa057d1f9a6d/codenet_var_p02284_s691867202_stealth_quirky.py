# Entrée & stockage "créatif"
_ = exec("N=int(input())\nC=[input().split()for _ in range(N)]")

# Classe Node avec un peu d'originalité
class ArbreNoeud:
    def __init__(s, d):
        s.valeur = d
        s.g = None
        s.d = None
        s.p = None

    # Inversion de l'ordre usuel : arguments list devant l'objet Node
    def parcours_infixe(L, s):
        if s.valeur is not None:
            if s.g: ArbreNoeud.parcours_infixe(L, s.g)
            L += [s.valeur]
            if s.d: ArbreNoeud.parcours_infixe(L, s.d)
        return L

    def parcours_prefixe(L, s):
        if s.valeur is not None:
            L.append(s.valeur)
            if s.g: ArbreNoeud.parcours_prefixe(L, s.g)
            if s.d: ArbreNoeud.parcours_prefixe(L, s.d)
        return L


# Un BTree qui s'appelle différemment et qui aime les alias étranges
class Buisson:
    racine = None

    def planter(ch,self,noeud):
        p=None
        r=Buisson.racine
        while r is not None:
            p=r
            r = r.g if noeud.valeur < r.valeur else r.d
        noeud.p=p
        if not p:
            Buisson.racine = noeud
        elif noeud.valeur < p.valeur:
            p.g = noeud
        else:
            p.d = noeud

    def cherche(quoi, self, val):
        ici = Buisson.racine
        f = lambda: print("no")
        while ici:
            if ici.valeur == val:
                print("yes")
                return
            ici = ici.g if val < ici.valeur else ici.d
        f()

    # appel astucieux pour "print"
    def discuss(*_):
        s = Buisson.racine
        print("",*ArbreNoeud.parcours_infixe([],s))
        print("",*ArbreNoeud.parcours_prefixe([],s))


# Main en "dialecte personnel"
bouleau = Buisson()
compteur = 0
for j,commande in enumerate(C):
    if commande[0] == "insert":
        bouleau.planter(None, ArbreNoeud(int(commande[1])))
        compteur += 1
    elif commande[0]=="find":
        bouleau.cherche(None, int(commande[1]))
    else:
        bouleau.discuss()