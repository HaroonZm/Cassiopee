from collections import defaultdict

def gen(N, S, W):
    """
    Génère une séquence pseudo-aléatoire de chiffres décimaux basée sur les paramètres donnés.

    Args:
        N (int): Longueur de la séquence à générer.
        S (int): Graine initiale pour la séquence.
        W (int): Valeur utilisée dans la fonction de transformation xor.

    Yields:
        int: Prochain chiffre (entre 0 et 9) de la séquence générée.
    """
    g = S  # Valeur initiale de la graine
    for i in range(N):
        # Génère un chiffre en prenant la partie entière de la division par 7,
        # puis en prenant le chiffre des unités (modulo 10)
        yield (g // 7) % 10
        if g % 2 == 0:
            # Si g est pair, le diviser par 2
            g //= 2
        else:
            # Si g est impair, diviser par 2 (entièreté), puis appliquer xor avec W
            g = (g // 2) ^ W

def solve():
    """
    Lit les entrées, génère une séquence et compte, selon les règles décrites,
    le nombre de sous-chaînes non nulles dont la valeur numérique est multiple de Q.

    Entrée: Une ligne avec quatre entiers N, S, W, Q.
    Sortie: Affiche la réponse correspondant à la séquence générée.
    Retourne:
        bool: True si une nouvelle itération doit être réalisée (N != 0), sinon False (fin du programme).
    """
    # Lecture des paramètres depuis l'entrée standard
    N, S, W, Q = map(int, input().split())
    # Si N vaut 0, arrêter la boucle (aucune séquence à traiter)
    if N == 0:
        return False

    # Génération de la séquence de chiffres à partir de la graine et de la transformation
    bs = list(gen(N, S, W))
    ans = 0  # Initialise la réponse

    # Cas trivial : si Q vaut 2 ou 5, vérifie la divisibilité à chaque chiffre
    # (car un nombre décimal est multiple de 2/5 uniquement selon son dernier chiffre)
    if Q == 2 or Q == 5:
        cnt = 0  # Compte le nombre de chiffres non nuls rencontrés jusqu'ici
        for i in range(N):
            b = bs[i]  # Récupère le i-ème chiffre
            if b != 0:
                cnt += 1  # Incrémente le compteur pour les chiffres significatifs (non zéros)
            if b % Q == 0:
                # Si ce chiffre est divisible par Q, ajoute cnt à la réponse
                ans += cnt
    else:
        # Cas général pour Q différent de 2 ou 5 (donc premier avec 10)
        # Calcul de l'inverse de 10^(Q-2) mod Q pour faciliter le calcul des positions
        rev10 = pow(10, Q - 2, Q)
        D = defaultdict(int)  # Pour compter les occurrences de chaque reste modulo Q
        D[0] = 1  # Initialisation: le reste 0 a déjà été vu une fois
        s = 0     # Somme courante modulo Q
        v = 1     # Puissance courante de rev10 modulo Q (pour gérer les positions)
        first = 1 # Indique si on traite les premiers zéros non significatifs

        for i in range(N):
            b = bs[i]  # Récupère le chiffre actuel

            # Ignore les zéros non significatifs initiaux
            if first and b == 0:
                continue

            # Met à jour la somme modulo Q en tenant compte de la position
            s = (s + v * b) % Q
            # Met à jour la puissance de 10 à la position suivante
            v = (v * rev10) % Q

            # Ajoute au résultat le nombre de préfixes ayant déjà eu le même reste
            ans += D[s]

            # Met à jour le compteur du reste courant si prochain chiffre n'est pas un zéro
            if i < N - 1 and bs[i + 1] != 0:
                D[s] += 1

            # On a franchi les éventuels zéros de tête
            first = 0

    # Affiche la réponse finale
    print(ans)
    return True

# Boucle principale: exécute solve jusqu'à ce qu'il retourne False (fin des entrées)
while solve():
    ...