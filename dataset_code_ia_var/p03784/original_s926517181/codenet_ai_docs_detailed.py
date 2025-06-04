import sys
from collections import deque

def ask(x, y):
    """
    Affiche une question au format standardisé « ? x y ».
    
    Cette fonction est utilisée pour interroger un système externe,
    et le flush est utilisé pour s'assurer que la sortie est bien transmise.
    
    Args:
        x (int): Indice du premier élément à comparer.
        y (int): Indice du second élément à comparer.
    """
    print('?', x, y, flush=True)

def impossible():
    """
    Affiche 'Impossible' et termine le programme.
    
    Utilisée lorsque la combinaison d'entrée (A, B) ne permet pas
    de poursuivre l'algorithme.
    """
    print('Impossible', flush=True)
    sys.exit()

def main():
    """
    Fonction principale du programme.
    
    Récupère et traite l'entrée utilisateur, puis déroule l'algorithme
    de sélection basé sur les valeurs de A et B.
    """
    # Lecture des valeurs d'entrée A et B depuis stdin
    A, B = map(int, input().split())
    
    # Si le problème est impossible selon la contrainte donnée, arrêter.
    if A <= B:
        impossible()
    
    N = A + B  # Calcul du nombre total d'éléments à traiter

    # Création de la liste des candidats à l'aide d'une deque pour faciliter l'accès à gauche et à droite
    candidates = deque(range(N), N)

    # Réduction de la liste des candidats jusqu'à en conserver deux ou moins
    while len(candidates) > 2:
        x = candidates.pop()      # Retirer le dernier indice
        y = candidates.pop()      # Retirer le nouvel avant-dernier indice
        ask(x, y)                 # Interroger le système externe
        
        # Lecture de la réponse et (selon la réponse) replacer un candidat à gauche
        if input() == 'Y':
            candidates.appendleft(y)
    
    # Le 'dieu' (candidat principal choisi) est le premier restant dans la deque
    god = candidates[0]
    result = []
    # Pour chaque indice de 0 à N-1, on interroge la position par rapport au 'dieu'
    for i in range(N):
        ask(god, i)
        result.append(input() == 'Y')
    
    # Affichage du résultat au format attendu
    print('!', ''.join(str(int(s)) for s in result), flush=True)

if __name__ == "__main__":
    main()