import sys

# Initialisation des compteurs pour deux types de triangles spécifiques
rec = 0   # Compteur pour les triangles rectangles
rhom = 0  # Compteur pour les triangles isocèles dont la somme des deux côtés égaux est supérieure au troisième côté

def analyse_triangles():
    """
    Lit des lignes depuis l'entrée standard où chaque ligne contient trois entiers séparés par des virgules,
    représentant les longueurs des côtés d'un triangle.
    
    Pour chaque triangle, cette fonction vérifie deux propriétés :
    1. Si le triangle est rectangle (le carré du plus grand côté est égal à la somme des carrés des deux autres).
    2. Si le triangle est isocèle (les deux premiers côtés sont égaux) et que la somme des deux côtés égaux
       est strictement supérieure au troisième côté.
       
    La fonction incrémente deux compteurs globaux distincts pour chaque type détecté.
    Enfin, elle affiche les totaux de triangles rectangles et de triangles isocèles correspondants.
    """
    global rec, rhom  # Utilisation des variables globales pour modification
    for s in sys.stdin:
        # Extraction des trois côtés à partir de la ligne d'entrée, en convertissant chaque valeur en entier
        a, b, c = [int(x) for x in s.split(',')]
        
        # Vérification du triangle rectangle via le théorème de Pythagore
        # On teste ici si c² = a² + b²
        if c**2 == b**2 + a**2:
            rec += 1  # Incrémentation du compteur de triangles rectangles
        
        # Vérification d'un triangle isocèle (les deux premiers côtés égaux) et que leur somme > troisième côté
        elif a == b and a + b > c:
            rhom += 1  # Incrémentation du compteur de triangles isocèles répondant à la condition

if __name__ == "__main__":
    analyse_triangles()
    # Affichage des résultats : le nombre de triangles rectangles puis le nombre de triangles isocèles spécifiques
    print(rec)
    print(rhom)