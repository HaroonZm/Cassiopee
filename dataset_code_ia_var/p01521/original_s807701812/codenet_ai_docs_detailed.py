def process_string(s):
    """
    Traite une liste de caractères composée de 'o' et 'x'. 
    À chaque itération, retire les séquences de 'x' ou 'o' situées aux extrémités. 
    Affiche "o" si tous les caractères restants sont des 'o', "x" si ce sont des 'x'.
    
    L'opération alterne entre la suppression des séquences de 'x' puis des séquences de 'o' aux extrémités.
    
    Args:
        s (list): Liste de caractères ('o' ou 'x') à traiter.
        
    Returns:
        None. Affiche le résultat à la sortie standard.
    """
    while True:
        # Si la liste ne contient plus aucun 'o', cela signifie qu'il ne reste que des 'x'
        if "o" not in s:
            print("x")
            break
        
        # Supprimer toutes les occurrences de 'x' à l'extrémité droite
        if s[-1] == "x":
            while s and s[-1] == "x":
                s.pop()
        # Supprimer toutes les occurrences de 'x' à l'extrémité gauche
        elif s[0] == "x":
            while s and s[0] == "x":
                s.pop(0)
        
        # Si la liste ne contient plus aucun 'x', cela signifie qu'il ne reste que des 'o'
        if "x" not in s:
            print("o")
            break
        
        # Supprimer toutes les occurrences de 'o' à l'extrémité droite
        if s[-1] == "o":
            while s and s[-1] == "o":
                s.pop()
        # Supprimer toutes les occurrences de 'o' à l'extrémité gauche
        elif s[0] == "o":
            while s and s[0] == "o":
                s.pop(0)

def main():
    """
    Fonction principale. Récupère l'entrée utilisateur et lance le traitement.
    """
    # Convertir la chaîne d'entrée en liste de caractères pour permettre la modification
    s = list(input())
    process_string(s)

if __name__ == "__main__":
    main()