def check_word_chain(a: str, b: str, c: str) -> str:
    """
    Vérifie si trois chaînes de caractères forment une "chaîne de mots" spécifique.

    Les règles sont les suivantes :
      - Le dernier caractère de la première chaîne 'a' doit être égal au premier caractère de la deuxième chaîne 'b'.
      - Le dernier caractère de la deuxième chaîne 'b' doit être égal au premier caractère de la troisième chaîne 'c'.

    Args:
        a (str): Le premier mot saisi par l'utilisateur.
        b (str): Le deuxième mot saisi par l'utilisateur.
        c (str): Le troisième mot saisi par l'utilisateur.

    Returns:
        str: "YES" si les mots forment une chaîne valide selon la règle, "NO" sinon.
    """
    # Vérifie la correspondance entre la fin et le début de chaque paire de mots
    if a[-1] == b[0] and b[-1] == c[0]:
        return "YES"
    else:
        return "NO"

def main():
    """
    Fonction principale du programme.

    Demande à l'utilisateur d'entrer trois mots séparés par des espaces,
    puis affiche "YES" si les mots forment une chaîne valide, sinon affiche "NO".
    """
    # Lit les trois mots depuis l'entrée standard, séparés par des espaces
    a, b, c = map(str, input("Entrez trois mots séparés par des espaces : ").split())

    # Vérifie si la condition de la chaîne est respectée et affiche le résultat
    result = check_word_chain(a, b, c)
    print(result)

# Appelle la fonction principale lorsque le script est exécuté
if __name__ == '__main__':
    main()