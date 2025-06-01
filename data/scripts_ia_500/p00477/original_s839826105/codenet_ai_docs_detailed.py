import sys

def read_integer_from_stdin():
    """
    Lit une ligne depuis l'entrée standard et la convertit en entier.
    
    Returns:
        int: L'entier lu depuis l'entrée standard.
    """
    return int(sys.stdin.readline())

def main():
    """
    Lit quatre entiers depuis l'entrée standard représentant des durées en secondes, 
    calcule la somme de ces durées, puis convertit et affiche la durée totale en minutes et secondes.
    
    Procédé:
    1. Lit quatre valeurs entières (en secondes).
    2. Calcule la somme totale des secondes.
    3. Convertit la somme en minutes et secondes restantes.
    4. Affiche les minutes puis les secondes sur deux lignes distinctes.
    """
    # Lire quatre entiers représentant des durées en secondes
    a = read_integer_from_stdin()
    b = read_integer_from_stdin()
    c = read_integer_from_stdin()
    d = read_integer_from_stdin()
    
    # Calculer la somme des quatre durées en secondes
    sum_4 = a + b + c + d
    
    # Convertir la somme totale en minutes entières
    minutes = sum_4 // 60  # Division entière pour obtenir les minutes
    
    # Calculer les secondes restantes après avoir extrait les minutes
    seconds = sum_4 % 60  # Modulo 60 pour obtenir les secondes restantes
    
    # Afficher le résultat final: minutes puis secondes sur deux lignes
    print(minutes)
    print(seconds)

if __name__ == "__main__":
    main()