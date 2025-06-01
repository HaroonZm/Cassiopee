# Demander à l'utilisateur d'entrer un nombre initial
# La fonction input() affiche une invite pour que l'utilisateur saisisse des données,
# puis renvoie ces données sous forme de chaîne de caractères (string).
# La fonction int() convertit cette chaîne de caractères en un nombre entier.
# Cette valeur est stockée dans la variable 'ans', qui sera notre accumulateur ou résultat courant.
ans = int(input())

# Démarrer une boucle infinie.
# Une boucle infinie signifie que le code à l'intérieur de ce bloc sera répété indéfiniment jusqu'à ce qu'une instruction d'arrêt (comme 'break' ou 'exit') soit exécutée.
while True:
    # Demander à l'utilisateur d'entrer une opération mathématique sous forme de chaîne de caractères.
    # Les opérations attendues sont '+', '-', '*', '/', ou '='.
    op = input()

    # Vérifier si l'utilisateur a entré le signe '+' correspondant à une addition.
    if op == '+':
        # Demander un autre nombre entier à l'utilisateur, que nous allons additionner à 'ans'.
        m = int(input())
        # Ajouter m à ans et stocker le résultat dans ans.
        ans += m

    # Vérifier si l'utilisateur a entré le signe '-' correspondant à une soustraction.
    elif op == '-':
        # Demander un nombre entier m à soustraire.
        m = int(input())
        # Soustraire m de ans et stocker le résultat dans ans.
        ans -= m

    # Vérifier si l'utilisateur a entré le signe '*' correspondant à une multiplication.
    elif op == '*':
        # Demander un nombre entier m à multiplier.
        m = int(input())
        # Multiplier ans par m et stocker le résultat dans ans.
        ans *= m

    # Vérifier si l'utilisateur a entré le signe '/' correspondant à une division entière.
    elif op == '/':
        # Demander un nombre entier m par lequel on va diviser ans.
        m = int(input())
        # Effectuer la division entière (division sans les décimales) de ans par m et stocker dans ans.
        # L'opérateur '//=' effectue la division entière et met à jour directement la variable ans.
        ans //= m

    # Vérifier si l'utilisateur a entré le signe '=' qui signifie afficher le résultat et arrêter le programme.
    elif op == '=':
        # Afficher la valeur actuelle de ans à l'écran.
        print(ans)
        # Terminer immédiatement le programme.
        # La fonction exit() stoppe l'exécution du script Python.
        exit()