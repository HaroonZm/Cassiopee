import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# Le problème consiste à maintenir un grand texte de parenthèses équilibré,
# initialement équilibré, et soumis à des flip de parenthèses ponctuels.
# À chaque flip, il faut indiquer la position minimale qu'il faut retourner 
# pour que la chaîne devienne à nouveau équilibrée.

# Analyse du problème et approche :

# Une chaîne est équilibrée si, en parcourant de gauche à droite, la somme
# des +1 pour '(' et -1 pour ')' ne descend jamais en dessous de 0, et la
# somme finale est 0.

# On doit donc maintenir la "balance" : pour une chaîne s, on définit pour
# chaque position i : val[i] = +1 si s[i] == '(', -1 sinon.

# La balance partielle sum(i) = val[0]+...+val[i] ne doit jamais être négative,
# et sum(N-1) == 0.

# Le problème: après chaque flip et "fix" (retour d'un flip qui rétablit l'équilibre),
# on doit indiquer la position minimale à flip (switch) pour recouvrer l'équilibre
# si une autre flip arrive.

# La solution classique: en présence de flips et requêtes rapides sur les sommes partielles
# et minimal prefix sum, segment tree est adapté.

# Pour vérifier si la chaîne est équilibrée, il faut que min prefix sum >=0 et somme finale ==0.

# Lorsqu'une flip est appliquée sur la position p:
# val[p] sera soit +1 (pour '(') soit -1 (pour ')'), donc la valeur de val[p] sera inversée.
# Cela modifie les sommes partielles de p à la fin.

# La donnée clé: après flip, la chaîne devient "déséquilibrée" avec un minimum prefix sum < 0.
# Pour rééquilibrer, on flip un caractère à une position minimale pos tel que
# si on inverte val[pos], la chaîne redevient équilibrée.

# L'approche pour trouver ce pos minimal dans un balanced string altéré par un flip est:
# Elle vient d'une solution classique (référence : solution officielle japonaise).

# On maintient un segment tree sur les gains val[i], capable de donner:
# - sum total sur tout le tableau (avec update ponctuel)
# - minimum prefix sum sur tout le tableau
# Par rapport à val, on stocke dans le segment tree:
#   total sum sur un intervalle
#   minimum prefix sum sur un intervalle
#   (minimum prefix sum = minimum de prefix sums en ce intervalle)

# Quand on flip un caractère en position p:
#   on modifie val[p], val[p] = -val[p]
# On met à jour l'arbre segmentaire.

# Pour trouver la position minimale à flip pour rééquilibrer:
# On cherche la plus petite position pos tel que si on inverse val[pos],
# la chaîne devient équilibrée.

# Cette position est celle qui fixe le "déséquilibre" le plus à gauche.
# On peut la trouver par une recherche dans l'arbre segmentaire:
# Une recherche descendante basée sur le prefix minimum.

# Détails du segment tree:
# pour chaque noeud: on garde (total sum, minimum prefix sum)
# Pour concaténation de deux intervalles [L,R] = [L,M] + [M+1,R]:
# sum_total = sum_left + sum_right
# minimum_prefix = min(min_left, sum_left + min_right)
# ('min_left' et 'min_right' sont minimum prefix sums dans parties gauches et droites)

# Recherche de la position minimale:
# On part de la racine:
# Si le minimum prefix est >= 0 à partir de la racine, la chaîne est équilibrée.
# Sinon, on descend l'arbre en priorisant le fils gauche:
# Si dans le fils gauche le min prefix < 0, descend à gauche.
# Sinon, on va à droite mais en ajustant la valeur du prefix par le sum total du gauche.

# A la feuille:
# La position retournée est la position pour fixer la chaîne.

# Implémentation concrète ci-dessous.

class SegmentTree:
    def __init__(self, n):
        self.n = 1
        while self.n < n:
            self.n <<= 1
        # tree stocke pour chaque noeud (sum, min_prefix)
        self.sum = [0]*(2*self.n)
        self.min_pref = [0]*(2*self.n)
    
    # construit l'arbre à partir d'une liste de valeurs val
    def build(self, val):
        for i in range(len(val)):
            self.sum[self.n+i] = val[i]
            self.min_pref[self.n+i] = min(0, val[i])
        for i in range(self.n-1, 0, -1):
            self.sum[i] = self.sum[i<<1] + self.sum[i<<1|1]
            self.min_pref[i] = min(self.min_pref[i<<1], self.sum[i<<1] + self.min_pref[i<<1|1])
    
    # met à jour la position p avec la nouvelle valeur v
    def update(self, p, v):
        p += self.n
        self.sum[p] = v
        self.min_pref[p] = min(0,v)
        p >>= 1
        while p:
            self.sum[p] = self.sum[p<<1] + self.sum[p<<1|1]
            self.min_pref[p] = min(self.min_pref[p<<1], self.sum[p<<1] + self.min_pref[p<<1|1])
            p >>= 1
    
    # recherche la position minimale qui cause un prefix sum négatif
    # la chaîne est équilibrée si min_pref[1]>=0
    # sinon on cherche la première position où prefix sum devient <0.
    def find_min_pos(self):
        if self.min_pref[1] >= 0:
            # équilibrée => position à retourner = 1 (par convention)
            return 1
        p = 1
        prefix_sum = 0
        while p < self.n:
            left = p << 1
            right = left | 1
            if self.min_pref[left] + prefix_sum < 0:
                # le déséquilibre se trouve dans le fils gauche
                p = left
            else:
                # sinon on doit aller à droite en ajoutant la somme du gauche
                prefix_sum += self.sum[left]
                p = right
        # on est à une feuille, la position correspond à (p - n)
        return p - self.n + 1  # +1 car positions sont 1-indexées

def main():
    N,Q = map(int,input().split())
    s = list(input().rstrip())
    # On code '(' = +1, ')' = -1
    val = [1 if c=='(' else -1 for c in s]

    seg = SegmentTree(N)
    seg.build(val)

    # Chaque flip qi :
    # 1) on flip val[qi-1] = -val[qi-1]
    # 2) on update seg
    # 3) on cherche la position minimale pos à fliper pour que chaine redevienne équilibre
    # 4) on fait ce flip (pour "fixer" la chaine)
    # 5) on update seg avec le flip à pos

    for _ in range(Q):
        qi = int(input())-1
        # flip donné par rayon cosmique
        val[qi] = -val[qi]
        seg.update(qi, val[qi])

        # trouver la position minimale à flip pour recompenser
        pos = seg.find_min_pos()-1

        # flip de correction
        val[pos] = -val[pos]
        seg.update(pos, val[pos])

        print(pos+1)

if __name__ == "__main__":
    main()