tp = {}

def read_team_points():
    """
    Lit les entrées de l'utilisateur sous la forme 't,p' où 't' est un identifiant d'équipe
    et 'p' est le nombre de points de cette équipe. La saisie se fait jusqu'à la lecture de '0,0'.
    Remplit le dictionnaire global 'tp' avec les clés étant les identifiants d'équipe et les valeurs
    les points correspondants.
    """
    while True:
        line = raw_input()  # Lecture d'une ligne au format "t,p"
        t, p = map(int, line.split(","))  # Conversion en entiers
        if t == 0 and p == 0:
            break
        tp[t] = p

def compute_sorted_unique_points():
    """
    Calcule une liste des points uniques présents dans 'tp', triée par ordre décroissant.
    
    Returns:
        list: Une liste des valeurs de points uniques triées du plus grand au plus petit.
    """
    unique_points = set(tp[key] for key in tp.keys())  # ensemble des points uniques
    plist = sorted(list(unique_points), reverse=True)
    return plist

def print_team_rank(plist):
    """
    Lit des identifiants d'équipe depuis l'entrée standard et affiche pour chacun son rang.
    Le rang est déterminé par la position du nombre de points de l'équipe dans la liste triée.

    Args:
        plist (list): Liste triée des points uniques dans l'ordre décroissant.
    """
    while True:
        try:
            team = int(raw_input())
        except:
            # Sortie de la boucle si l'entrée n'est pas un entier valide ou fin d'entrée
            break
        # Recherche du rang (index + 1) correspondant aux points de l'équipe 'team'
        rank = plist.index(tp[team]) + 1
        print rank

# Programme principal
read_team_points()
plist = compute_sorted_unique_points()
print_team_rank(plist)