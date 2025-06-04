import sys

# Augmente la limite de récursion pour éviter des erreurs dans le cas de récursions profondes.
sys.setrecursionlimit(10 ** 6)

def MI():
    """
    Lit une ligne depuis l'entrée standard, sépare les valeurs par des espaces
    et les convertit en entiers.
    
    Retourne :
        map : un itérable de valeurs entières obtenues à partir de la ligne lue.
    """
    return map(int, sys.stdin.readline().split())

def main():
    """
    Lit les entrées nécessaires depuis l'utilisateur, effectue un calcul selon une
    formule spécifique, puis affiche le résultat.
    
    Les valeurs lues sont :
        a, b : deux entiers sur la première ligne
        p, q, r : trois entiers sur la deuxième ligne
    
    Calcule et affiche :
        (p*b + a*q + r*b) / (q + r)
    """
    # Lecture de deux entiers pour 'a' et 'b'
    a, b = MI()
    # Lecture de trois entiers pour 'p', 'q', et 'r'
    p, q, r = MI()
    # Application de la formule demandée et affichage du résultat
    print((p * b + a * q + r * b) / (q + r))

# Appel de la fonction principale lorsque le script est exécuté
main()