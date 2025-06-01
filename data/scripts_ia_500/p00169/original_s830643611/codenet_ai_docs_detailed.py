# Définition d'une liste s1 utilisée pour les calculs
# s1 correspond à une plage de nombres de 0 à 10 inclus, complétée par trois 10 supplémentaires
s1 = list(range(11)) + [10]*3

def f(x):
    """
    Fonction récursive qui, à partir d'une liste d'indices x,
    calcule une liste de valeurs selon des règles précises.

    Args:
        x (list of int): liste d'indices utilisés pour accéder à s1.

    Returns:
        list: liste de valeurs calculées filtrées pour être inférieures à 22.
    """
    # Si la liste x est vide, retourner la liste contenant seulement 0 (cas de base)
    if x == []:
        return [0]
    
    # Récupère la valeur dans s1 à l'indice x[0]
    e = s1[x[0]]
    
    # Appel récursif sur le reste de la liste x[1:]
    # Pour chaque valeur e1 retournée, ajoute e et construit la liste A1
    A1 = [e + e1 for e1 in f(x[1:])]
    
    # Initialisation d'une liste vide A2
    A2 = []
    
    # Si e vaut 1, crée une nouvelle liste en ajoutant 10 à chaque élément de A1
    if e == 1:
        A2 = [e_ + 10 for e_ in A1]
    
    # Combine les listes A1 et A2 puis filtre pour garder uniquement les valeurs inférieures à 22
    # La fonction filter retourne un itérateur en Python 3, on convertit donc en liste
    return list(filter(lambda val: val < 22, A1 + A2))

# Boucle infinie pour traiter les entrées utilisateur
while True:
    # Lecture de la ligne de saisie, séparation en valeurs entières
    x = list(map(int, input().split()))
    
    # Condition de terminaison : si le premier élément est 0, on quitte la boucle
    if x[0] == 0:
        break
    
    # Appel de la fonction f avec la liste x
    a = f(x)
    
    # Affiche le maximum des valeurs retournées par f, ou 0 si la liste est vide
    print(max(a) if a else 0)