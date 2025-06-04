import sys
input = sys.stdin.readline

# Pour répondre efficacement aux requêtes RMQ (Range Minimum Query) de type find et update,
# nous utilisons une structure de données Segment Tree (arbre segmenté).
# Cette structure permet d'effectuer les mises à jour et requêtes sur des segments en O(log n).

class SegmentTree:
    def __init__(self, n):
        # Initialisation de l'arbre segmenté à la taille adaptée
        # On considère ici une taille entière puissance de 2 supérieure à n pour simplifier l'implémentation.
        self.n = 1
        while self.n < n:
            self.n <<= 1
        # Initialisation des noeuds avec la valeur maximale possible (2^31 - 1)
        self.tree = [2**31 - 1] * (2 * self.n - 1)

    def update(self, i, x):
        # Met à jour la valeur a_i à x.
        # On modifie la feuille correspondante, puis on remonte les changements vers la racine.
        i += self.n - 1  # indice feuille dans self.tree
        self.tree[i] = x
        while i > 0:
            i = (i - 1) // 2  # parent du noeud i
            # Lancement vers le haut : mettre à jour le noeud parent avec le minimum de ses 2 enfants
            self.tree[i] = min(self.tree[2*i+1], self.tree[2*i+2])
    
    def find(self, s, t):
        # Renvoie le minimum dans l'intervalle [s, t]
        # Utilisation d'une recherche descendante sur l'arbre
        res = 2**31 - 1
        s += self.n - 1
        t += self.n - 1
        while s <= t:
            if (s % 2) == 0:
                # s est un noeud pair, racine du segment
                res = min(res, self.tree[s])
                s += 1
            if (t % 2) == 1:
                # t est un noeud impair, racine du segment
                res = min(res, self.tree[t])
                t -= 1
            s = (s - 1) // 2
            t = (t - 1) // 2
        return res


def main():
    n, q = map(int, input().split())
    seg_tree = SegmentTree(n)
    
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            # update(x, y)
            seg_tree.update(x, y)
        else:
            # find(x, y)
            l, r = x, y
            if l > r:
                l, r = r, l  # s'assurer que l <= r
            print(seg_tree.find(l, r))


if __name__ == "__main__":
    main()