import math

def compute_gcd_tiled_areas(W, H, C):
    """
    Calcule le nombre de tuiles couvertes avec le motif le plus petit possible qui recouvre un rectangle de taille W x H.
    
    La taille du motif le plus petit est déterminée par le plus grand commun diviseur (gcd) de W et H.
    
    Args:
        W (int): Largeur du rectangle.
        H (int): Hauteur du rectangle.
        C (int): Nombre de couleurs (ou motifs différents à appliquer).
    
    Returns:
        int: Nombre total de tuiles nécessaires pour couvrir le rectangle sans superposition, en tenant compte de C motifs.
    """
    # Calculer le plus grand commun diviseur des dimensions pour déterminer la taille du motif de base.
    g = math.gcd(W, H)
    
    # Calculer combien de motifs de taille g x g tiennent dans la largeur et la hauteur.
    motifs_larg = W // g
    motifs_haut = H // g
    
    # Le nombre total de tuiles est le produit des motifs dans chaque dimension, multiplié par le nombre de couleurs.
    total_tuiles = motifs_larg * motifs_haut * C
    return total_tuiles

def main():
    """
    Fonction principale.
    
    Lit les entrées utilisateur (W, H, C), puis affiche le nombre total de tuiles nécessaires.
    """
    # Lire les entrées W (largeur), H (hauteur) et C (nombre de couleurs/motifs), séparées par des espaces.
    W, H, C = map(int, input().split())
    
    # Appeler la fonction de calcul et afficher le résultat.
    print(compute_gcd_tiled_areas(W, H, C))

# Point d’entrée du programme
if __name__ == "__main__":
    main()