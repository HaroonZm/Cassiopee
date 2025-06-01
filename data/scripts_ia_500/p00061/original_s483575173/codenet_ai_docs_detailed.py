def read_results():
    """
    Lit les paires (numéro, accepté) depuis l'entrée standard jusqu'à ce que (0, 0) soit rencontré.
    
    Chaque ligne doit être au format 'num,accepted' où num et accepted sont des entiers.
    Retourne un dictionnaire où la clé est 'num' et la valeur est 'accepted'.
    """
    result = {}
    while True:
        line = raw_input()  # Lecture d'une ligne d'entrée au format 'num,accepted'
        num, accepted = map(int, line.split(','))  # Séparation et conversion des deux valeurs en entiers
        if num == 0 and accepted == 0:
            # Condition d'arrêt : lorsque les deux valeurs sont nulles, on interrompt la lecture
            break
        else:
            result[num] = accepted  # Enregistrement du résultat dans le dictionnaire
    return result

def assign_ranks(result):
    """
    Attribue des rangs aux numéros en fonction du nombre d'acceptations.
    
    Le classement est décroissant selon la valeur 'accepted'.
    Les numéros avec le même nombre d'acceptations obtiennent le même rang.
    
    Paramètre:
        result (dict): dictionnaire {num: accepted}
    
    Retour:
        dict: dictionnaire {num: rang} avec le rang attribué pour chaque numéro
    """
    rank = 1
    previous_accepted = 0
    ranked_result = {}
    # On trie les éléments par nombre d'acceptations décroissant
    for num, accepted in sorted(result.items(), key=lambda x: x[1], reverse=True):
        if previous_accepted > accepted:
            rank += 1  # Augmentation du rang si la valeur acceptée est inférieure à la précédente
        ranked_result[num] = rank  # Assignation du rang
        previous_accepted = accepted  # Mise à jour pour la prochaine comparaison
    return ranked_result

def print_ranks(ranked_result):
    """
    Lit des numéros depuis l'entrée standard et affiche leur rang associé.
    
    La lecture s'arrête lorsqu'une erreur de fin de fichier (EOF) est détectée.
    
    Paramètre:
        ranked_result (dict): dictionnaire {num: rang}
    """
    while True:
        try:
            num = int(raw_input())  # Lecture du numéro à interroger
            print ranked_result[num]  # Affichage du rang correspondant
        except EOFError:
            # Fin de l'entrée standard, sortie de la boucle
            break

# Programme principal
results = read_results()
ranked_results = assign_ranks(results)
print_ranks(ranked_results)