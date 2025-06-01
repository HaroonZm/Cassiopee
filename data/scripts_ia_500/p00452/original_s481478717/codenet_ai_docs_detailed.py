def input_score(N):
    """
    Lit N scores depuis l'entrée standard et retourne une liste contenant ces scores,
    avec un zéro ajouté au début qui représente le score lorsque la cible n'est pas touchée.

    Args:
        N (int): Le nombre de scores à lire.

    Returns:
        list[int]: Liste de scores, avec un 0 ajouté en première position.
    """
    score = []  # Liste pour stocker les scores des cibles, incluant un score 0 pour le cas où on ne lance pas
    score.append(0)  # Ajoute 0 comme score par défaut
    for i in range(N):
        score.append(int(input()))  # Lecture de chaque score et ajout dans la liste
    return score

def cal_two_sum_score(score):
    """
    Calcule toutes les sommes possibles obtenues en lançant deux fois, en combinant
    les scores de la liste 'score'. Élimine les doublons et trie la liste résultante.

    Args:
        score (list[int]): Liste des scores possibles en un lancé.

    Returns:
        list[int]: Liste triée des scores possibles en deux lancers, sans doublons.
    """
    two_score = []  # Liste pour stocker toutes les combinaisons de scores en deux lancers
    contain_sum = {}  # Dictionnaire pour vérifier la présence d'une somme déjà calculée

    # Boucle double pour combiner chaque score avec chaque autre score (incluant lui-même)
    for i in range(len(score)):
        for j in range(len(score)):
            now_score = score[i] + score[j]  # Somme de deux scores
            if not contain_sum.get(now_score):
                contain_sum[now_score] = True  # Marquer cette somme comme déjà rencontrée
                two_score.append(now_score)  # Ajouter la somme à la liste

    two_score.sort()  # Trie la liste des sommes pour faciliter la recherche ultérieure
    return two_score

def cal_four_sum_score(two_score, M):
    """
    Trouve la somme maximale de quatre lancers (deux paires de deux scores) qui est
    inférieure ou égale à M, en utilisant la méthode de deux pointeurs sur la liste triée
    'two_score'.

    Args:
        two_score (list[int]): Liste triée des scores possibles en deux lancers.
        M (int): Le score maximal à ne pas dépasser.

    Returns:
        int: La somme maximale possible inférieure ou égale à M.
    """
    left = 0  # Pointeur gauche au début de la liste
    right = len(two_score) - 1  # Pointeur droit à la fin de la liste
    max_score = 0  # Initialisation du score maximum trouvé

    # Parcours des paires avec deux pointeurs
    while left != right:
        now_score = two_score[left] + two_score[right]  # Somme des deux valeurs pointées

        if now_score < M:
            # Somme inférieure à M, mise à jour du max_score si besoin
            max_score = max(max_score, now_score)
            left += 1  # Déplacer le pointeur gauche vers la droite pour augmenter la somme
        elif now_score > M:
            # Somme trop grande, diminuer la somme en déplaçant le pointeur droit vers la gauche
            right -= 1
        else:
            # Somme exactement égale à M, solution optimale trouvée, on sort
            max_score = M
            break

    return max_score

def main():
    """
    Fonction principale qui lit plusieurs cas de test, exécute les calculs de scores possibles
    pour deux et quatre lancers, puis affiche le score maximum ne dépassant pas la limite donnée.
    La lecture s'arrête lorsque N et M sont tous deux égaux à 0.
    """
    while True:
        N, M = map(int, input().split())  # Lecture de N (nombre de scores) et M (score maximal)
        if N == 0 and M == 0:
            break  # Fin des cas de test

        score = input_score(N)  # Lecture des scores des cibles
        two_score = cal_two_sum_score(score)  # Calcul des scores possibles en deux lancers
        max_score = cal_four_sum_score(two_score, M)  # Calcul du score maximal pour quatre lancers
        print(max_score)  # Affichage du résultat

if __name__ == "__main__":
    main()