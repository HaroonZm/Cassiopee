import sys

# Style procédural pour IO
def lire_ligne():
    return sys.stdin.readline()

def ecrire(text):
    sys.stdout.write(text)

# Style OOP pour l'emballage de la logique de parsing
class Parseur:
    def __init__(self):
        self.curseur = 0
        self.lbl = 1
        self.dico_map = {"01": 0}
        self.dico_sp = {"01": {0}}
        self.dico_sv = {"01": (0, 1)}
        self.modele = lambda g,h: f"0{g}{h}1"

    # Style fonctionnelle pour comparaison
    def comparer(self, gauche, droite):
        gc, gb = gauche
        dc, db = droite
        a0, b0 = self.dico_sv[gb]
        a1, b1 = self.dico_sv[db]
        if a1 * b0 != a0 * b1:
            return a1 * b0 - a0 * b1
        if gc is None and dc is None:
            return 0
        gl, gr = gc
        dl, dr = dc
        c1 = self.comparer(gl, dl)
        if c1 != 0:
            return c1
        c2 = self.comparer(gr, dr)
        if c2 != 0:
            return c2
        return 0

    # Style impératif-mixte pour construire l'expression
    def lire_expr(self, chaine):
        S = chaine + "$"
        self.curseur = 0
        def expr():
            if S[self.curseur] == "x":
                self.curseur += 1
                return (None, "01")
            self.curseur += 1
            gauche = expr()
            self.curseur += 1
            droite = expr()
            self.curseur += 1
            gb = gauche[1]
            db = droite[1]
            e_bis = self.modele(gb, db) if gb < db else self.modele(db, gb)
            if e_bis not in self.dico_map:
                self.dico_map[e_bis] = self.lbl
                self.dico_sp[e_bis] = self.dico_sp[gb] | self.dico_sp[db] | {self.lbl}
                self.dico_sv[e_bis] = (len(self.dico_sp[gb] & self.dico_sp[db]), len(self.dico_sp[gb] | self.dico_sp[db]))
                self.lbl += 1
            if self.comparer(gauche, droite) < 0:
                gauche, droite = droite, gauche
            return ((gauche, droite), e_bis)
        return expr()

# Style "scripting" très direct pour DFS
dfs = lambda racine, mode: "x" if racine[0] is None else \
    "({} {})".format(
        dfs(racine[0][mode], 0),
        dfs(racine[0][1-mode], 1)
    )

# Mélange de styles pour la logique principale
def resoudre():
    ligne = lire_ligne().strip()
    if ligne == "0":
        return False
    p = Parseur()
    arbre = p.lire_expr(ligne)
    ecrire(dfs(arbre, 0))
    ecrire("\n")
    return True

while resoudre():
    pass