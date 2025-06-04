def get_integer_list(prompt, length):
    """
    Demande à l'utilisateur de saisir une liste de nombres entiers.

    Args:
        prompt (str): Le message à afficher lors de la saisie.
        length (int): Le nombre d'entiers à lire.

    Returns:
        list: Une liste d'entiers de taille 'length' saisis par l'utilisateur.
    """
    integers = []
    for _ in range(length):
        value = int(input(prompt))
        integers.append(value)
    return integers

def count_special_numbers(a, l, r):
    """
    Compte les entiers x dans l'intervalle [l, r] satisfaisant des conditions spécifiques
    par rapport au tableau a selon l'algorithme donné.

    Pour chaque entier x dans [l, r] inclus :
      - Cherche s'il existe un élément dans a qui divise x.
      - Si c'est le cas et l'indice (i+1) du premier a[i] qui divise x est impair,
        incrémente le compteur.
      - Si aucun a[i] ne divise x et len(a) est pair, incrémente aussi le compteur.

    Args:
        a (list): Liste des diviseurs potentiels.
        l (int): Borne inférieure de l'intervalle.
        r (int): Borne supérieure de l'intervalle.

    Returns:
        int: Le nombre d'entiers x ayant passé les conditions.
    """
    cnt = 0  # Compteur pour les entiers satisfaisant les conditions
    n = len(a)
    for x in range(l, r + 1):  # Parcourir chaque entier de l à r inclus
        flag = False  # Indique si x est divisible par un des éléments de a
        for i in range(n):
            if x % a[i] == 0:
                flag = True
                break  # S'arrêter au premier diviseur trouvé
        if flag:
            # (i+1) car les indices Python commencent à 0
            if (i + 1) % 2 == 1:
                cnt += 1
        else:
            if n % 2 == 0:
                cnt += 1
    return cnt

def main():
    """
    Fonction principale qui gère la boucle d'entrée des cas de test, la récupération
    des paramètres et des tableaux, et qui affiche la sortie requise pour chaque cas.
    """
    while True:
        # Récupère n, l, r et détecte la condition d'arrêt
        try:
            n, l, r = map(int, input().split())
        except Exception:
            # Gère les erreurs d'entrée inattendues
            print("Erreur dans la saisie. Veuillez entrer trois entiers séparés par des espaces.")
            continue

        # Condition pour arrêter la boucle principale
        if n == 0 and l == 0 and r == 0:
            break

        # Lecture du tableau a de taille n
        a = []
        for idx in range(n):
            try:
                aa = int(input())
            except Exception:
                print(f"Erreur dans la saisie du {idx+1}-ème entier du tableau. Veuillez réessayer.")
                aa = int(input())
            a.append(aa)

        # Appliquer le traitement et afficher le résultat
        cnt = count_special_numbers(a, l, r)
        print(cnt)

if __name__ == "__main__":
    main()