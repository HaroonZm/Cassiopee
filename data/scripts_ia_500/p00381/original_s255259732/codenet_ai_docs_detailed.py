from collections import defaultdict

MOD = 1000000007

def main():
    """
    Lit les entrées depuis l'utilisateur, effectue un calcul basé sur les caractères de deux chaînes,
    et affiche un résultat modulo MOD.

    Description détaillée :
    1. Lecture d'un entier n représentant la longueur des chaînes.
    2. Lecture de deux chaînes s et t de longueur n.
    3. Initialisation d'un dictionnaire (dic) comptant le nombre d'occurrences pondérées des caractères,
       avec une valeur initiale pour le premier caractère de s.
    4. Parcours des sous-chaînes intermédiaires (de l'indice 1 à n-2) de s et t en parallèle.
       Pour chaque paire de caractères (cs, ct), on met à jour dic[cs] en y ajoutant dic[ct],
       en prenant soin d'appliquer le modulo MOD pour gérer les grands nombres.
    5. À la fin, affichage de la valeur associée au dernier caractère de t dans dic.

    Cette logique semble compter, d'une certaine manière, des occurrences pondérées ou des chemins liés aux caractères,
    selon les correspondances entre s et t sur les positions intermédiaires.
    """
    # Lecture de la taille des chaînes
    n = int(input())

    # Lecture des deux chaînes de caractères
    s = input()
    t = input()

    # Utilisation d'un dictionnaire à valeurs entières, initialisé à 0 par défaut
    dic = defaultdict(int)

    # Initialisation du dictionnaire avec la première lettre de s à 1
    dic[s[0]] = 1

    # Parcours des caractères des chaînes s et t de l'indice 1 à n-2
    # zip(s[1:n-1], t[1:n-1]) crée des paires (cs, ct) à chaque étape
    for cs, ct in zip(s[1:n-1], t[1:n-1]):
        # Mise à jour de la valeur associée à cs en y ajoutant la valeur associée à ct
        dic[cs] += dic[ct]

        # Application du modulo pour éviter les dépassements de capacité d'entiers
        dic[cs] %= MOD

    # Affichage de la valeur associée au dernier caractère de t
    print(dic[t[-1]])

if __name__ == "__main__":
    main()