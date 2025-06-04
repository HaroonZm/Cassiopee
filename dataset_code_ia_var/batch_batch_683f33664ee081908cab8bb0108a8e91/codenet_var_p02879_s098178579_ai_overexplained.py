def solve():
    # Demander à l'utilisateur de saisir une ligne de texte depuis l'entrée standard (clavier).
    # On s'attend à recevoir deux nombres séparés par un espace, par exemple "3 4".
    # La fonction input() lit l'entrée utilisateur sous la forme d'une chaîne de caractères.
    user_input = input()
    
    # La méthode split() divise la chaîne de caractères en une liste de sous-chaînes,
    # en utilisant par défaut l'espace comme séparateur.
    tokens = user_input.split()
    
    # La fonction map applique la fonction int à chaque élément de la liste 'tokens'.
    # Cela convertit chaque sous-chaîne en un entier.
    a, b = map(int, tokens)
    
    # On vérifie maintenant si 'a' et 'b' sont tous les deux compris entre 1 et 9 inclus.
    # L'opérateur <= signifie "inférieur ou égal à",
    # donc 1<=a<=9 vérifie que 'a' n'est pas plus petit que 1 et pas plus grand que 9.
    # Idem pour 'b'.
    if 1 <= a <= 9 and 1 <= b <= 9:
        # Si la condition est vraie, on retourne le produit de 'a' et 'b'.
        # L'opérateur * effectue une multiplication entre deux entiers.
        return a * b
    else:
        # Si au moins une des valeurs 'a' ou 'b' n'est pas dans l'intervalle de 1 à 9,
        # on retourne -1 pour signaler une entrée invalide.
        return -1

# Ce bloc vérifie si ce fichier est exécuté comme programme principal.
# '__name__' est une variable spéciale en Python qui prend comme valeur '__main__'
# lorsque le script est exécuté directement par l'utilisateur.
if __name__ == '__main__':
    # Appeler la fonction 'solve' définie ci-dessus,
    # puis afficher le résultat retourné par cette fonction avec print().
    # print() permet d'afficher quelque chose à l'écran.
    print(solve())