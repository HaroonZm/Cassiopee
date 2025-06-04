from collections import defaultdict

# Définition d'une constante maximale représentant une limite supérieure pour les index utilisés.
MAX = 3652425

def main():
    """
    Programme principal qui lit les entrées, applique des opérations en fonction des instructions
    fournies, et répond à des requêtes de simulation d'un système basé sur l'accumulation temporelle
    avec différentes opérations par type.
    
    Entrée:
        n q          : n = nombre d'opérations, q = nombre de requêtes
        n lignes suivantes : w t x
            w = seuil temporel,
            t = type d'opération (0, 1, 2)
            x = durée de l'opération
        q lignes suivantes: y
            y = point de requête (temporalité pour restauration)
    
    Sortie:
        Pour chaque opération de type n, soit l'index de son insertion, soit "Many years later"
        Pour chaque requête, la valeur restor[y]
    """
    # Lecture des paramètres n (nombre d'opérations) et q (nombre de requêtes)
    n, q = map(int, input().split())

    # Lecture des opérations à effectuer : chaque opération est un triplet (w, t, x)
    lst = [tuple(map(int, input().split())) for _ in range(n)]

    # Initialisation des vecteurs de traitements temporels et de leur mémoire tampon
    # restaur: table de progression de la temporalité "restored"
    restor = [0] * (MAX + 10010)    
    # t0s: incréments cumulés pour les opérations de type 0
    t0s = [0] * (MAX + 10010)
    # t1s: incréments cumulés pour les opérations de type 1
    t1s = [0] * (MAX + 10010)
    # t2s: incréments cumulés pour les opérations de type 2 (effet secondaire du type 2)
    t2s = [0] * (MAX + 10010)
    # t3s: incréments cumulés intermédiaires pour le type 2 pour manipuler l'effet quadratique
    t3s = [0] * (MAX + 10010)

    # Tableaux pour suivre combien il faudra retirer des incréments à échéance pour type 1 et type 2
    t1_cnt_save = defaultdict(int)
    t3_cnt_save = defaultdict(int)

    # Compteurs pour le nombre courant d'opérations type 1 et type 2 actives
    t1_cnt = 0
    t3_cnt = 0
    index = 0  # Index temporel courant

    # Traitement de chaque opération de la liste lst
    for i, line in enumerate(lst):
        w, t, x = line

        # Propage l'effet accumulé jusqu'au point où restaur[index] atteint ou dépasse w
        while index < MAX and w > restor[index]:
            # Propagation des incréments de chaque type à l'instant temporel suivant
            t0s[index + 1] += t0s[index]
            t1_cnt -= t1_cnt_save[index + 1]
            t1s[index + 1] += t1s[index] + t1_cnt
            t3_cnt -= t3_cnt_save[index + 1]
            t3s[index + 1] += t3s[index] + 2 * t3_cnt
            t2s[index + 1] += t2s[index] + t3s[index + 1]
            # Actualisation de la valeur restaur à l'instant suivant
            restor[index + 1] = restor[index] + 1 + t0s[index] + t1s[index] + t2s[index]
            index += 1
        
        # Vérifie si l'opération peut être appliquée (selon si w <= restaur[index])
        if w <= restor[index]:
            print(index)
            if t == 0:
                # Opération de type 0 : effet simple sur t0s pendant x tours
                t0s[index] += 1
                t0s[index + x] -= 1
            elif t == 1:
                # Opération de type 1 : effet linéaire croissant pendant x tours
                t1_cnt += 1
                t1_cnt_save[index + x] += 1
                t1s[index] += 1
                t1s[index + x] -= x
            elif t == 2:
                # Opération de type 2 : effet quadratique croissant pendant x tours
                t3_cnt += 1
                t3_cnt_save[index + x] += 1
                t3s[index] += 1
                t3s[index + x] -= x * 2 - 1
                t2s[index] += 1
                t2s[index + x] -= x ** 2
        else:
            print("Many years later")

    # Traitement de chaque requête
    for _ in range(q):
        y = int(input())
        # Propage l'effet jusqu'à l'instant y (si ce n'est pas déjà fait)
        while index < y:
            t0s[index + 1] += t0s[index]
            t1_cnt -= t1_cnt_save[index + 1]
            t1s[index + 1] += t1s[index] + t1_cnt
            t3_cnt -= t3_cnt_save[index + 1]
            t3s[index + 1] += t3s[index] + 2 * t3_cnt
            t2s[index + 1] += t2s[index] + t3s[index + 1]
            restor[index + 1] = restor[index] + 1 + t0s[index] + t1s[index] + t2s[index]
            index += 1
        # Affiche le résultat demandé
        print(restor[y])

if __name__ == "__main__":
    main()