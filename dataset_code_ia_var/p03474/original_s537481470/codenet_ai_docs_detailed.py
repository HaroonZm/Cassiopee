def main():
    """
    Point d'entrée principal du programme.
    Lis les entiers A et B, puis une chaîne de caractères S, et vérifie si S est 
    au format d'un code postal : A chiffres, un tiret, puis B chiffres.
    Affiche 'Yes' si S correspond au format, sinon 'No'.
    """
    # Lecture des entiers A et B depuis l'entrée standard, séparés par un espace
    A, B = map(int, input().split())
    
    # Lecture de la chaîne S contenant le code à valider
    S = input()
    
    # Création d'une liste de conditions à vérifier pour valider le format de S
    cond = [
        len(S) == A + B + 1,      # S doit avoir exactement A + B + 1 caractères (le +1 pour le tiret)
        S[A] == '-',              # Le caractère à la position A (indice commençant à 0) doit être un tiret '-'
        S[:A].isdigit(),          # Les A premiers caractères doivent être des chiffres
        S[A + 1:].isdigit()       # Les B derniers caractères doivent être des chiffres
    ]
    
    # Affichage du résultat en fonction de la validité du format
    print('Yes' if all(cond) else 'No')

if __name__ == '__main__':
    # Appelle la fonction principale si ce fichier est exécuté comme programme principal
    main()