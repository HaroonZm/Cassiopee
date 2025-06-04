def validate_string():
    """
    Fonction principale qui lit une chaîne à partir de l'entrée standard et vérifie si elle suit un motif précis.
    Règles de validation :
    1. Le premier caractère doit être 'A'.
    2. Il doit y avoir exactement un 'C' dans la sous-chaîne S[2:-1].
    3. Après suppression du premier 'A' et du seul 'C', les caractères restants doivent tous être en minuscules.
    Affiche "AC" si la chaîne satisfait toutes les conditions, sinon affiche "WA".
    """
    # Lire la chaîne d'entrée et la convertir en liste de caractères pour faciliter les modifications
    S = [i for i in input()]
    
    # Vérifier si le premier caractère est "A" et s'il y a exactement un "C" dans la sous-liste S[2:-1]
    if S[0] == "A" and S[2:-1].count("C") == 1:
        # Supprimer la première occurrence de "A" (en position 0) de la liste
        S.remove("A")
        # Supprimer la première occurrence de "C" dans la liste restante
        S.remove("C")
        # Après suppressions, vérifier si les caractères restants sont tous des minuscules alphabétiques
        if "".join(S).islower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")

# Appel de la fonction principale si ce script est exécuté
if __name__ == "__main__":
    validate_string()