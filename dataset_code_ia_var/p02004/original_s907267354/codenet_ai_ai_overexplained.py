import sys  # Importe le module sys qui fournit un accès à certaines variables et fonctions utilisées ou maintenues par l'interpréteur Python

# Affecte la fonction readline (lecture d'une ligne depuis l'entrée standard) à une variable pour un accès plus facile/souvent plus rapide
readline = sys.stdin.readline

# Affecte la fonction write (écriture directe vers la sortie standard) à une variable courte pour la même raison
write = sys.stdout.write

# Définit une fonction nommée solve qui ne prend aucun argument
def solve():
    # Lit une ligne en entrée, supprime les caractères de fin de ligne (retours à la ligne, espaces en trop)
    S = readline().strip()
    
    # Initialise la variable ans à 0. Cette variable servira à compter le nombre de motifs complets trouvés
    ans = 0

    # Initialise la variable d à 0. Celle-ci représente la direction courante (0 à 3, modulo 4)
    d = 0
    
    # Initialise cur à 0. Cette variable compte combien de fois on a enchaîné des "R" dans un motif précis
    cur = 0
    
    # Parcourt chaque caractère c de la chaîne S (c'est-à-dire chaque lettre de l'entrée)
    for c in S:
        # Vérifie si le caractère courant c est égal à "R"
        if c == "R":
            # Si la direction actuelle d correspond au compte actuel cur, alors...
            if d == cur:
                # Incrémente cur de 1 car on a trouvé le motif attendu à cette étape
                cur += 1
            # Incrémente la direction d de 1, en prenant le reste après division par 4 pour "boucler" sur 0,1,2,3
            d = (d + 1) % 4
            # Si d est revenu à 0 ET qu'on a réussi à enchaîner 4 "R" dans le "bon" motif...
            if d == 0 and cur == 4:
                # On a trouvé un motif complet : on incrémente ans de 1
                ans += 1
                # On remet cur à 0 pour recommencer à chercher un nouveau motif
                cur = 0
        else:
            # Si le caractère n'est pas "R", alors c'est implicitement le seul autre cas prévu ("L")
            # On décrémente d de 1. Le modulo 4 garantit que cela 'tourne' correctement si on descend sous 0
            d = (d - 1) % 4
            # Si après avoir tourné à gauche on revient à la direction de départ (0)...
            if d == 0:
                # On doit réinitialiser cur, car la séquence potentielle est rompue
                cur = 0
    # Écrit le résultat final (le nombre de motifs trouvés), suivi d'un retour à la ligne, vers la sortie standard
    write("%d\n" % ans)

# Appelle la fonction solve pour exécuter l'algorithme lorsque le script est lancé
solve()