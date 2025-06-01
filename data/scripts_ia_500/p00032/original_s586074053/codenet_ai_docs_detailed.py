# Initialisation des compteurs
r, d = 0, 0

def traiter_triplet(a, b, c):
    """
    Traite un triplet de nombres entiers représentant potentiellement les côtés d'un triangle.

    Args:
        a (int): Longueur du premier côté.
        b (int): Longueur du deuxième côté.
        c (int): Longueur du troisième côté.

    Returns:
        tuple:
            bool: True si le triangle est rectangle (théorème de Pythagore vérifié), False sinon.
            bool: True si le triangle est isocèle (au moins deux côtés égaux), False sinon.
    """
    # Vérifie si le triangle est rectangle : a² + b² == c²
    est_rectangle = (a * a + b * b == c * c)
    # Vérifie si le triangle est isocèle : a == b
    est_isocèle = (a == b)
    return est_rectangle, est_isocèle

while True:
    try:
        # Lecture d'une ligne d'entrée utilisateur, attendue sous la forme "a,b,c"
        # Conversion des valeurs vers des entiers
        (a, b, c) = [int(i) for i in raw_input().split(',')]
    except:
        # Interruption de la boucle si la saisie est invalide ou vide
        break
    # Traitement du triplet
    rectangle, isocèle = traiter_triplet(a, b, c)
    # Mise à jour des compteurs
    if rectangle:
        r += 1
    if isocèle:
        d += 1

# Affichage du nombre de triangles rectangles détectés
print r
# Affichage du nombre de triangles isocèles détectés
print d