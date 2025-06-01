import math

def process_input():
    """
    Lit l'entrée standard ligne par ligne et traite chaque ligne comme une liste d'entiers.
    
    Chaque ligne est supposée commencer par un entier 'l' suivi d'une séquence d'entiers 'r'.
    Pour chaque ligne, la fonction applique une logique spécifique pour déterminer
    si la sortie doit être "OK" ou "NA" selon des contraintes mathématiques.
    
    La fonction boucle jusqu'à rencontrer une fin de fichier (EOF).
    """
    while True:
        l = 0          # Premier entier de la ligne, utilisé comme une limite ou un seuil
        r = []         # Liste des entiers suivants la limite
        try:
            # Lecture d'une ligne, découpage en entiers
            # raw_input() lit une ligne de l'entrée standard en Python 2
            inp = map(int, raw_input().split())
            # Récupérer le premier entier comme limite 'l'
            l = inp[0]
            # Le reste des entiers constitue la liste 'r'
            r = inp[1:]
        except EOFError:
            # Fin du fichier détectée, sortir de la boucle
            break
        
        n = len(r)  # Nombre d'éléments dans la liste r
        
        # Cas simple: si deux fois la somme des éléments de r est inférieure ou égale à l,
        # afficher "OK" car la condition est satisfaite immédiatement.
        if 2 * sum(r) <= l:
            print "OK"
        else:
            # Sinon, appliquer un algorithme pour organiser les éléments de r
            # afin d'estimer une valeur appelée 'ans' qui sera comparée à l.
            s = []
            
            if n > 1:
                # Tri de la liste r par ordre croissant
                r.sort()
                
                # Construction de la liste s selon une alternance spécifique
                # pour minimiser une certaine expression.
                for i in xrange(n / 2):
                    # On insère l'élément r[i] au début de s,
                    # puis on ajoute la liste s inversée,
                    # puis on ajoute à la fin r[-i-1] (élément symétrique à droite)
                    s = [r[i]] + s[::-1] + [r[-i-1]]
                
                # Gestion du cas où n est impair: ajouter l'élément du milieu r[n/2]
                if n & 1:
                    # Comparer la proximité de r[n/2] par rapport aux extrémités de s
                    if abs(s[0] - r[n / 2]) < abs(s[-1] - r[n / 2]):
                        # Ajouter à la fin si plus proche du début
                        s.append(r[n / 2])
                    else:
                        # Sinon ajouter au début
                        s = [r[n / 2]] + s
            else:
                # Si un seul élément dans r, s est simplement r
                s = r
            
            # Calcul de la valeur 'ans' en fonction des extrémités et d'une formule impliquant des racines carrées
            ans = s[0] + s[-1]
            for i in xrange(n - 1):
                # Ajouter deux fois la racine carrée du produit de paires consécutives
                ans += 2 * math.sqrt(s[i] * s[i + 1])
            
            # Comparer ans à la limite 'l' avec une marge tolérée 1e-9
            # Si ans strictement inférieur à l + 1e-9, afficher "OK", sinon "NA"
            print "OK" if ans < 0.000000001 + l else "NA"

# Appel principal
process_input()