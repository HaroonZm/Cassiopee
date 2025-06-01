# Initialisation d'une liste vide pour stocker les tuples (nom, a, b)
list = []

for i in range(9):
    # Lecture d'une ligne d'entrée utilisateur, séparée en trois variables : n (str), a (str), b (str)
    n, a, b = input().split()
    
    # Conversion des deux dernières variables en entiers
    a = int(a)
    b = int(b)
    
    # Ajout d'un tuple (nom, a, b) à la liste
    list.append((n, a, b))
    
    # Calcul et affichage des résultats selon les valeurs de a et b
    # Affiche le nom, la somme de a et b, et le calcul pondéré (a*200 + b*300)
    print(n, a + b, a * 200 + b * 300)