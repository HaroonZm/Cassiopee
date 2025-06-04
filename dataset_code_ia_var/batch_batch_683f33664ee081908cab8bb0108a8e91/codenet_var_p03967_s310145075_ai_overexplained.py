import sys  # Importe le module sys, qui permet de travailler avec l'entrée et la sortie standards, entre autres fonctionnalités système

def slove():
    # Redéfinit la fonction input afin qu'elle lise une ligne depuis l'entrée standard en utilisant sys.stdin.readline
    # Cela peut être plus efficace que la fonction input() intégrée, notamment pour les grandes entrées
    input = sys.stdin.readline

    # Lit une ligne depuis l'entrée standard, supprime le caractère de saut de ligne à la fin, puis la convertit en chaîne de caractères explicitement avec str()
    # Bien que readline() renvoie déjà une chaîne, la conversion str() est superflue ici mais elle est conservée pour suivre l'original
    s = str(input().rstrip('\n'))

    # Initialise deux variables entières g et p à 0
    # g va compter le nombre de caractères 'g' dans la chaîne s
    # p va compter le nombre de caractères autres que 'g' (supposé être 'p' ici) dans la chaîne s
    g = 0
    p = 0

    # Parcourt chaque caractère dans la chaîne s à l'aide d'une boucle for avec l'indice i allant de 0 à len(s)-1 inclus
    for i in range(len(s)):
        # Si le caractère courant s[i] est exactement égal à la lettre 'g'
        if s[i] == "g":
            # Incrémente la variable g de 1, c'est-à-dire stocke le nombre de 'g' rencontrés jusqu'à maintenant
            g += 1
        else:
            # Sinon, incrémente p de 1 ; on suppose que les autres caractères sont 'p'
            p += 1

    # Calcule la moitié entière de la longueur de la chaîne s, en utilisant la division entière '//' pour s'assurer que le résultat soit un entier
    # Cette valeur est stockée dans la variable pp, qui va représenter combien d'opérations sont à faire dans la première moitié de s (selon la logique du programme)
    pp = len(s) // 2

    # Initialise un compteur cnt à 0 ; cette variable va accumuler un certain score selon la logique ci-dessous
    cnt = 0

    # Parcourt à nouveau tous les caractères de la chaîne s, toujours avec l'indice i allant de 0 à len(s)-1
    for i in range(len(s)):
        # Si pp n'est pas égal à zéro, donc il reste une opération à faire dans la première moitié
        if pp != 0:
            # Décrémente pp de 1, ce qui indique qu'une position de plus dans la "moitié" a été visitée
            pp -= 1

            # Vérifie si le caractère courant s[i] est la lettre 'g'
            if s[i] == "g":
                # Si oui, incrémente cnt de 1
                # Cela signifie qu'avoir un 'g' dans la première moitié donne un point
                cnt += 1
        else:
            # Sinon, donc pp est égal à zéro, ce qui signifie qu'on traite maintenant la seconde moitié de la chaîne s
            # On vérifie si le caractère courant s[i] est la lettre 'p'
            if s[i] == "p":
                # Si oui, décrémente cnt de 1
                # Cela signifie qu'avoir un 'p' dans la seconde moitié retire un point
                cnt -= 1
    # Affiche la valeur finale de cnt à la sortie standard
    print(cnt)

# Ce bloc vérifie si ce fichier est exécuté en tant que script principal (par opposition à son importation comme module)
if __name__ == '__main__':
    # Appelle la fonction slove définie ci-dessus
    slove()