def main():
    """
    Lit une chaîne de caractères depuis l'entrée standard, puis affiche soit le dernier caractère de la chaîne,
    soit la lettre 'o' en fonction du premier caractère de la chaîne :
      - Si le premier caractère est 'o', affiche 'o'
      - Sinon, affiche le dernier caractère de la chaîne
    """
    # Lecture de la chaîne de caractères saisie par l'utilisateur
    s = input()
    # Vérifie si le premier caractère de la chaîne est 'o' (renvoie True ou False)
    premier_est_o = (s[0] == 'o')
    # Si le premier caractère est 'o', affiche 'o', sinon affiche le dernier caractère de la chaîne
    # [s[-1], 'o'][premier_est_o] utilise la valeur booléenne pour choisir l'élément approprié dans la liste
    print([s[-1], 'o'][premier_est_o])

if __name__ == "__main__":
    main()