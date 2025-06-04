def compute_sequence_value(N, A, B):
    """
    Calcule la paire (A, B) à l'issue d'une série de 12 transformations basées sur des règles spécifiques.
    
    Paramètres :
        N (int): Entier pour déterminer l'indice final dans la séquence cyclique.
        A (int): Première valeur entière servant de base à la suite.
        B (int): Deuxième valeur entière servant de base à la suite.
    
    Retourne :
        tuple: La paire (A, B) résultante à l'indice modulo 12 de la suite générée.
    """
    # Initialisation de la liste pour stocker les paires (A, B) à chaque itération
    sequence_states = [(A, B)]
    
    # Application de 11 transformations successives (pour un total de 12 états, incluant l'initial)
    for i in range(1, 12):
        if i % 2 == 0:
            # Pour les indices pairs, additionner B à A et stocker dans B
            B = A + B
        else:
            # Pour les indices impairs, soustraire B de A et stocker dans A
            A = A - B
        # Ajouter la nouvelle paire (A, B) à la liste de résultats
        sequence_states.append((A, B))
    
    # Retourne la paire située à l'indice (N modulo 12), assurant le caractère cyclique
    return sequence_states[N % 12]

def main():
    """
    Point d'entrée principal du script.
    Récupère les entrées utilisateur, applique l'algorithme et affiche le résultat.
    """
    # Lecture de l'entier N
    N = int(input())
    # Lecture des entiers A et B donnés en une seule ligne séparée par un espace
    A, B = map(int, input().split())
    
    # Calcul de la valeur résultante selon la logique définie
    result = compute_sequence_value(N, A, B)
    
    # Affichage du résultat sous forme de deux valeurs séparées par un espace
    print(*result)

# Exécution du script principal si ce fichier est exécuté directement
if __name__ == "__main__":
    main()