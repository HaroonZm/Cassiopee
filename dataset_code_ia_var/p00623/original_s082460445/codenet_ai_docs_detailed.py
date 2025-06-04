class Node:
    """
    Représente un nœud d'un arbre binaire pour générer toutes les valeurs booléennes possibles
    en utilisant ET, OU, XOR sur des entrées binaires indexées par une expression parenthésée.
    """

    def __init__(self):
        """
        Initialise le nœud avec des attributs left et right.
        Ils sont initialement des listes contenant un entier 0.
        """
        self.left = [0]
        self.right = [0]

    def createleft(self, inp, A):
        """
        Analyse récursivement la sous-expression inp pour générer la partie gauche de l'arbre.
        Si l'expression est une variable, elle récupère sa valeur dans A.
        Si c'est une sous-expression, elle crée récursivement des sous-nœuds.

        Args:
            inp (str): sous-chaîne représentant la sous-expression gauche.
            A (List[int]): liste des entiers binaires correspondants à chaque variable.
        """
        cnt = 0  # Compteur pour suivre le niveau de parenthèses
        for cn in range(len(inp)):
            c = inp[cn]
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            elif cnt == 0:
                # Si on rencontre une variable (chiffre) au niveau de racine
                self.left = [A[int(c) - 1]]
            elif c == ' ' and cnt == 1:
                # Détecte le séparateur principal de la sous-expression
                leftnode = Node()
                inpl = inp[1:cn]  # Sous-expression gauche entre parenthèses
                inpr = inp[cn + 1:len(inp) - 1]  # Sous-expression droite entre parenthèses
                leftnode.createleft(inpl, A)
                leftnode.createright(inpr, A)
                self.left = leftnode  # La partie gauche devient ce nouveau sous-arbre

    def createright(self, inp, A):
        """
        Analyse récursivement la sous-expression inp pour générer la partie droite de l'arbre.
        Fonctionne de la même manière que createleft mais pour la branche droite.

        Args:
            inp (str): sous-chaîne représentant la sous-expression droite.
            A (List[int]): liste des entiers binaires correspondants à chaque variable.
        """
        cnt = 0  # Compteur de niveau de parenthèses
        for cn in range(len(inp)):
            c = inp[cn]
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            elif cnt == 0:
                # Variable de niveau racine
                self.right = [A[int(c) - 1]]
            elif c == ' ' and cnt == 1:
                # Détecte le séparateur principal
                rightnode = Node()
                inpl = inp[1:cn]
                inpr = inp[cn + 1:len(inp) - 1]
                rightnode.createleft(inpl, A)
                rightnode.createright(inpr, A)
                self.right = rightnode  # La partie droite devient ce nouveau sous-arbre

    def possible(self):
        """
        Calcule toutes les valeurs booléennes possibles (ET, OU, XOR) entre
        la partie gauche et la droite du nœud. Si l'une d'elles est un sous-arbre,
        l'appelle récursivement.

        Returns:
            List[int]: toutes les valeurs possibles obtenues en appliquant les opérateurs
            binaires sur les résultats des sous-arbres gauches et droits.
        """
        lp = self.left
        rp = self.right
        # Si la branche gauche est un sous-arbre, calcule les possibilités récursivement
        if isinstance(self.left, Node):
            lp = self.left.possible()
        # Idem pour la droite
        if isinstance(self.right, Node):
            rp = self.right.possible()
        # Combine toutes les possibilités avec &, | et ^ pour chaque paire
        return ([l & r for l in lp for r in rp] +
                [l | r for l in lp for r in rp] +
                [l ^ r for l in lp for r in rp])


# Boucle principale pour traiter plusieurs cas jusqu'à ce que l'entrée soit 'END'
while True:
    inp = raw_input()
    if inp == 'END':
        break  # Arrête si l'utilisateur entre 'END'

    n = int(raw_input())  # Nombre de variables binaires
    A = []  # Liste des nombres binaires des variables
    for i in range(n):
        # Lit un nombre binaire sous forme de chaîne, le convertit en int
        bn = int(''.join(raw_input().split()), 2)
        A.append(bn)

    root = Node()  # Crée le nœud racine de l'arbre
    cnt = 0  # Compteur pour suivre parenthésage de l'expression

    # Création de l'arbre à partir de l'expression parenthésée
    for cn in range(len(inp)):
        c = inp[cn]
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        elif c == ' ' and cnt == 1:
            # Trouve le séparateur principal de la racine, découpe les sous-expressions
            inpl = inp[1:cn]
            inpr = inp[cn + 1:len(inp) - 1]
            root.createleft(inpl, A)
            root.createright(inpr, A)

    # Calcule toutes les valeurs possibles pour l'expression
    poss = root.possible()
    # Compte combien de résultats sont égaux à 15 (soit tous les bits à 1 pour 4 bits)
    ans = poss.count(15)
    print ans