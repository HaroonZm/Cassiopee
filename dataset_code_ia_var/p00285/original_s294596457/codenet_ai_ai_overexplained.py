def main():
    # Commencer une boucle infinie, qui continuera jusqu'à ce qu'on la brise manuellement
    while True:
        # Lire deux entiers séparés par un espace sur la même ligne.
        # input() lit une ligne d'entrée de l'utilisateur sous forme de chaîne de caractères.
        # .split() découpe cette chaîne en fonction des espaces et retourne une liste de chaînes.
        # map(int, ...) convertit chaque chaîne en un entier.
        # m et w reçoivent les deux entiers extraits.
        m, w = map(int, input().split())
        
        # Si le premier entier 'm' est égal à 0, il s'agit du signal pour arrêter la boucle (fin de l'entrée).
        if m == 0:
            break  # On quitte la boucle while, donc le programme s'arrête ici.
        
        # On vérifie si m est supérieur ou égal à w.
        if m >= w:
            # Dans ce cas, on lit une nouvelle ligne de nombres entiers, autant que le nombre indiqué par m.
            # list(map(int, input().split())) construit une liste d'entiers à partir de l'entrée utilisateur.
            long_lst = list(map(int, input().split()))  # Liste longue, associée au plus grand nombre d'éléments
            short_lst = list(map(int, input().split()))  # Liste courte, associée au plus petit nombre d'éléments
            # 'rest' représente le masque binaire pour toutes les combinaisons possibles des éléments de la longue liste.
            # 2**m donne le nombre total de sous-ensembles possibles pour m éléments (inclus 0), donc on retire 1 pour ignorer le sous-ensemble vide.
            rest = 2 ** m - 1
        else:
            # Même logique que ci-dessus mais inversée si m < w : la liste la plus courte est lue en premier.
            short_lst = list(map(int, input().split()))
            long_lst = list(map(int, input().split()))
            # 'rest' devient alors basé sur w.
            rest = 2 ** w - 1
        
        # Crée une liste 'mem' destinée à stocker les résultats de calculs déjà effectués (mémoïsation), pour éviter de recalculer plusieurs fois les mêmes valeurs.
        # La liste à une taille de 'rest + 1', car on va utiliser chaque index pour représenter une configuration possible du masque binaire.
        # On initialise tout à None pour savoir si cette configuration a déjà été calculée ou non.
        mem = [None] * (rest + 1)
        
        # Définir une fonction interne 'elec' qui calcule une valeur spécifique à partir de deux paramètres :
        # bm : élément provenant de la liste courte
        # bw : élément provenant de la liste longue
        def elec(bm, bw):
            # Calcul de la valeur absolue de la différence entre les deux entiers.
            bd = abs(bm - bw)
            # On applique la formule de coût/score fournie.
            # (bd - 30) ** 2 élève au carré la différence entre bd et 30.
            # On multiplie le résultat par bd pour obtenir la valeur finale.
            return bd * (bd - 30) ** 2
        
        # Définir une fonction interne 'score' utilisant la mémoïsation et une recherche exhaustive des meilleures combinaisons.
        # Elle prend deux arguments : 'rest' (le masque binaire des éléments restants) et 'index' (l'indice actuel dans la liste courte).
        def score(rest, index):
            # Vérifier si ce sous-problème a déjà été calculé (mémoisation).
            # Si mem[rest] n'est pas None, alors on a déjà calculé ce cas, donc on retourne la valeur sauvegardée.
            if mem[rest] != None:
                return mem[rest]
            # Cas de base 1 : s'il ne reste plus de combinaisons possibles ('rest' est 0, donc aucune combinaison active)
            # Cas de base 2 : ou si on est allé en dehors des indices valides (index < 0)
            # Donc on retourne 0, car il n'y a plus d'association possible.
            if rest == 0 or index < 0:
                return 0
            
            # On va itérer sur chaque bit de 'rest' pour trouver quelle position (élément dans la longue liste) est active (c'est-à-dire à 1).
            mask = 1  # Initialiser le masque à 1 (bit de poids faible, c'est-à-dire première position).
            count = 0  # Compteur pour connaître la position (indice) de l'élément dans long_lst.
            ret = 0    # 'ret' va garder la meilleure valeur obtenue parmi toutes les options possibles.
            # On cherche chaque bit à 1 dans le masque binaire 'rest'.
            while mask <= rest:
                # Pour chaque bit actif dans 'rest', c'est-à-dire chaque possibilité d'association avec un élément de long_lst.
                if mask & rest:
                    # On crée un nouveau masque 'new_rest' dans lequel on retire (met à 0) le bit courant (celui qu'on va tester dans cette itération).
                    # Cela permet de continuer la recherche sans cet élément, simulant ainsi l'association entre l'élément courant de short_lst et long_lst[count].
                    new_rest = rest & ~mask
                    # L'appel récursif à la fonction score avec un 'new_rest' (élément considéré comme utilisé) et 'index - 1' (prochain élément de short_lst à attribuer).
                    # On ajoute le score courant (calculé par 'elec' pour l'association actuelle) au score obtenu récursivement sur le sous-problème restant.
                    ret = max(ret, score(new_rest, index - 1) + elec(short_lst[index], long_lst[count]))
                # On décale le masque d'un bit à gauche pour passer à l'élément suivant dans long_lst.
                mask <<= 1
                # Incrémenter le compteur pour avoir l'indice correspondant dans la longue liste.
                count += 1
            
            # Sauvegarder la valeur maximale obtenue pour ce 'rest' dans le tableau de mémoïsation.
            mem[rest] = ret
            # Retourner ce score.
            return ret
        
        # Afficher le score optimal trouvé pour les entrées actuelles.
        # La fonction 'min(m, w) - 1' donne l'indice le plus élevé de la liste courte qui sera utilisé dans la première étape de la récursivité.
        print(score(rest, min(m, w) - 1))
        
# Appeler la fonction principale pour démarrer le programme.
main()