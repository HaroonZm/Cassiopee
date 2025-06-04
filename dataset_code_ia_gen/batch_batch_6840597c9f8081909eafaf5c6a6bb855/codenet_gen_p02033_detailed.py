import sys
import bisect

input = sys.stdin.readline

def main():
    # Lecture des entrées
    N, M = map(int, input().split())
    fans_positions = list(map(int, input().split()))
    Q = int(input())
    losses_allowed = list(map(int, input().split()))

    # fans_positions[i] = m_i : le i-eme souffleur est placé entre x=m_i-1 et x=m_i
    # En pratique, on considère ces positions comme des points entre les entiers.
    # On trie les positions pour garantir l'ordre (même si l'énoncé dit qu'elles sont croissantes)
    fans_positions.sort()

    # Pour un tir de flèche de longueur L (entier > 0),
    # on doit compter le nombre de "pertes" (損失) occasionnées lorsque la pointe est à x=1..N
    # pertes occurent si dans [x-L, x] aucun souffleur n'est inclus.
    # car il faut que la flèche de longueur L (de [x-L, x]) contienne au moins un souffleur.
    # Le critère à vérifier pour chaque x = 1..N est:
    #    y = x - L  => segment [y, x]
    #    on regarde si il y a un m_i dans ]y,x] (note l'usage des m_i entiers - qui représentent des points entre entiers)
    #      car chaque souffleur est entre m_i-1 et m_i, donc entre x=a et x=b, les souffleurs sont à des "demi-positions"
    # Pour simplifier : 
    #   On considère "p = m_i" (position demi-entier)
    #   La flèche couvre l'intervalle [x-L, x] avec x et L entiers.
    #   On veut savoir s'il existe un p dans (x-L, x] (ou [x-L+ϵ, x]) inclus.
    # Donc on cherche :

    # Pour chaque x = 1..N :
    #   perte si aucun m_i dans l'intervalle ]x-L, x]
    # On va pré-calculer, pour chaque position x=1..N et chaque longueur possible L,
    # ceci est impossible car N et L peuvent être jusqu'à 10^5.

    # Solution : On exploite que:
    # pertes = nombre de x in [1..N] tels que aucun souffleur dans (x-L, x]
    # 
    # On interprète ça différemment.
    #
    # Pour un L fixé, pertes = nombre de x où la flèche de longueur L ne couvre aucun souffleur.
    #
    # On veut répondre pour différentes contraintes l (pertes <= l)
    #
    # Soit f(L) = nombre de pertes pour la longueur L.
    # f(L) est décroissante en L (plus la flèche est longue, moins il y a de pertes)
    #
    # Donc on peut chercher L minimal tq f(L) <= l
    #
    # Preprocessing :
    # Il faut pouvoir calculer f(L) rapidement.
    #
    # Méthode pour calculer f(L):
    # On regarde les segments entre souffleurs sur l'axe [0,N]:
    # Les souffleurs sont à des positions mi (demi-unités)
    # On peut considérer les positions entières 1..N comme points où vérifier les pertes
    
    # Passons à une solution efficace décrite ci-dessous :

    # Étape 1 : Ajouter deux position "virtuelles" aux extrémités, 0 et N+1 (car souffleurs entre [0,N])
    fans_positions = [0] + fans_positions + [N + 1]

    # Étape 2 : entre chaque paire de souffleurs consécutifs fans_positions[i] et fans_positions[i+1],
    # Il y a un grand "intervalle vide" (pas de souffleurs dans cette plage)
    # Cet intervalle induira un certain nombre de pertes si la flèche a une longueur <= la taille de cet intervalle - 1

    # Pour un intervalle vide de longueur gap = fans_positions[i+1] - fans_positions[i] - 1 (en entier),
    # le nombre de pertes dues à cet intervalle dépend de L :
    # Si L <= gap, cet intervalle crée (gap - L +1) pertes.
    # Si L > gap, aucune perte de cet intervalle.
    
    # Ex : souffleurs à positions 2 et 5 :
    # intervalle vide entre 2 et 5 est de taille 2 (positions 3 et 4)
    # pour L=1 => pertes = 2 - 1 + 1 = 2
    # pour L=2 => pertes = 2 - 2 + 1 = 1
    # pour L=3 => pertes = 2 - 3 + 1 = 0 (car pas négatif)
    # etc.

    # Étape 3 : on calcule la liste des gaps.
    gaps = []
    for i in range(len(fans_positions) - 1):
        gap = fans_positions[i + 1] - fans_positions[i] - 1
        if gap > 0:
            gaps.append(gap)

    # Tri des gaps
    gaps.sort()

    # Étape 4 : On veut calculer f(L) = sum over gaps of max(0, gap - L +1)
    # = sum over gap >= L of (gap - L + 1)
    #
    # Pour rendre efficient, on fait un préfixe des sommes de gaps
    prefix_sums = [0]
    for g in gaps:
        prefix_sums.append(prefix_sums[-1] + g)

    # Fonction pour calculer f(L) en O(log M)
    def f(L):
        # Trouver l'index i où gaps[i] >= L (borne inférieure)
        idx = bisect.bisect_left(gaps, L)
        if idx == len(gaps):
            return 0
        # nombres de gaps >= L
        count = len(gaps) - idx
        # somme des gaps >=L
        sum_gaps = prefix_sums[-1] - prefix_sums[idx]
        # pertes = sum( gap - L + 1 ) =  sum_gaps - count*(L - 1)
        return sum_gaps - count * (L - 1)

    # Étape 5 : pour répondre aux requêtes l_i (pertes autorisées),
    # on veut le plus petit L tq f(L) <= l_i
    # L doit être un entier > 0

    # Comme N <= 1e5, L ∈ [1..N]
    # Il y a aussi possibilité que la condition ne soit jamais satisfaite => on renvoie -1

    # Préparation de la recherche binaire pour la condition sur L
  
    # Recherche binaire classique sur L in [1..N] pour chaque l_i
    output = []
    for l_i in losses_allowed:
        low, high = 1, N+1  # high = N+1 pour gérer -1 si pas de solution
        ans = -1
        while low < high:
            mid = (low + high) // 2
            if f(mid) <= l_i:
                ans = mid
                high = mid
            else:
                low = mid + 1
        output.append(ans)

    # Affichage résultats
    print('\n'.join(map(str, output)))

if __name__ == '__main__':
    main()