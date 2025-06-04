import sys  # Importe le module sys, qui fournit un accès à certaines variables et fonctions spécifiques de l'interpréteur
import functools  # Importe le module functools, utile pour les fonctions d'ordre supérieur, bien que non utilisé explicitement ici

# Vérifie la version majeure de Python utilisée pour exécuter le script.
# Ceci sert à choisir la bonne fonction pour créer une table de traduction de caractères (maketrans),
# car l'implémentation diffère entre Python 2 et Python 3.
if sys.version_info[0] >= 3:  # Si la version majeure est 3 ou supérieure (Python 3.x)
    maketrans = str.maketrans  # Utilise str.maketrans qui est natif en Python 3 pour créer des tables de traduction
else:
    from string import maketrans  # En Python 2, maketrans se trouve dans le module string

# Définition de fonctions anonymes (lambdas) pour les opérations logiques bit à bit :
O = lambda a: lambda b: a | b  # Fonction pour faire un OU bit-à-bit entre deux valeurs. Retourne une fonction qui attend un deuxième argument.
A = lambda a: lambda b: a & b  # Fonction pour faire un ET bit-à-bit entre deux valeurs. Même principe, mais pour l'opération ET.
X = lambda a: lambda b: a ^ b  # Fonction pour faire un XOR bit-à-bit entre deux valeurs. Même principe, mais pour l'opération XOR.

# Boucle infinie : le programme continuera tant qu'un "break" n'est pas rencontré à l'intérieur
while True:
    # Lit une ligne depuis l'entrée standard (habituellement, le clavier ou un fichier quand redirigé)
    # rstrip() enlève les espaces en fin de ligne, y compris le retour à la ligne
    # La ligne est ensuite transformée via la table de traduction pour remplacer certains caractères :
    # - Les opérateurs '+', '*', '^', '[', et ']' sont changés en 'O', 'A', 'X', '(', ')', respectivement
    s = sys.stdin.readline().rstrip().translate(maketrans('+*^[]', 'OAX()'))
    if s == '.':  # Si la ligne entrée est simplement un point, cela signifie la fin de l'entrée ; on quitte la boucle.
        break
    # Pour chaque lettre 'a', 'b', 'c' et 'd' dans la chaîne,
    # On la remplace par "(a)", "(b)", "(c)", "(d)" respectivement.
    # Cela permet d'encapsuler chaque variable par des parenthèses, facilitant l'évaluation d'expressions complexes.
    for c in 'abcd':
        s = s.replace(c, '(%s)' % c)  # Remplace chaque occurrence de c par (c)

    # s[1:-1] enlève le premier et le dernier caractère de la chaîne,
    # probablement parce que la chaîne est désormais entourée d'une paire de parenthèses inutiles
    s = s[1:-1]

    # Lit une nouvelle ligne depuis l'entrée standard, correspondant à la valeur des variables sous forme entière.
    n = int(sys.stdin.readline())  # Convertit la chaîne obtenue en entier

    # Remplace dans s chaque variable 'a', 'b', 'c', 'd' par un chiffre de l'entier n, formaté sur 4 chiffres,
    # Par exemple si n=5 => '0005', et on remplace a->0, b->0, c->0, d->5
    # Cela permet d'affecter à chaque variable une valeur extraite du nombre entré
    # Ce remplacement est fait via translate et une table de traduction des caractères
    r = eval(s.translate(maketrans('abcd', '%04d' % n)))
    # eval() exécute la chaîne comme du code Python, calculant ainsi le résultat de l'expression booléenne/arithmétique

    # Calcule combien de valeurs entre 0 et 9999 donnent le même résultat r pour l'expression s.
    # Pour cela :
    # - Pour chaque i de 0 à 9999 :
    #   * On remplace 'a','b','c','d' dans s par les chiffres correspondants de i (formaté sur 4 chiffres, avec des zéros initiaux)
    #   * On évalue l'expression obtenue, et on teste si le résultat est égal à r
    # - On compte le nombre de cas où le résultat est égal à r avec sum()
    count = sum(
        r == eval(s.translate(maketrans('abcd', '%04d' % i)))  # Pour chaque i allant de 0 à 9999, compare le résultat à r
        for i in range(10000)  # Boucle sur tous les entiers de 0 à 9999 inclus
    )

    # Affiche (print) le résultat r calculé sur l'entrée, puis le nombre de valeurs parmi toutes les combinaisons possibles
    # pour lesquelles l'expression donne le même résultat, séparés par un espace
    print('%d %d' % (r, count))  # Affichage formaté du résultat