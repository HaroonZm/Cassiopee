def check_string_edges():
    """
    Lit une entrée utilisateur et vérifie si le premier et le dernier caractère
    sont tous deux 'x'. 
    Si c'est le cas, imprime "x", sinon imprime "o".
    """
    # Demande à l'utilisateur de saisir une chaîne de caractères
    a = raw_input()
    
    # Concatène le premier et le dernier caractère de la chaîne entrée
    edges = a[0] + a[-1]
    
    # Vérifie si les deux sont 'x' et affiche le résultat approprié
    if edges == "xx":
        print "x"
    else:
        print "o"

# Appelle la fonction pour exécuter le programme
check_string_edges()