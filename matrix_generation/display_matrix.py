import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

def charger_matrice(chemin_fichier):
    """
    Charge une matrice à partir d'un fichier .npy
    
    Args:
        chemin_fichier (str): Chemin vers le fichier .npy
        
    Returns:
        numpy.ndarray: La matrice chargée
    """
    try:
        matrice = np.load(chemin_fichier)
        print(f"Matrice chargée depuis {chemin_fichier}")
        print(f"Dimensions: {matrice.shape[0]} lignes x {matrice.shape[1]} colonnes")
        return matrice
    except Exception as e:
        print(f"Erreur lors du chargement de la matrice: {e}")
        exit(1)

def afficher_matrice_console(matrice, afficher_valeurs=True):
    """
    Affiche la matrice dans la console avec formatage
    
    Args:
        matrice (numpy.ndarray): La matrice à afficher
        afficher_valeurs (bool): Si True, affiche les valeurs numériques, sinon des catégories
    """
    print("\nMATRICE DE LOG PROBABILITÉS:")
    print(f"Dimensions: {matrice.shape[0]} lignes x {matrice.shape[1]} colonnes")
    
    # Calculer la largeur maximale pour l'affichage
    max_width = 10 if afficher_valeurs else 8
    
    # Créer une ligne de séparation
    header_sep = "-" * (max_width * matrice.shape[1] + 10)
    print(header_sep)
    
    # Afficher les indices de colonnes
    print("     ", end="")
    for j in range(matrice.shape[1]):
        print(f"{j:^{max_width}}", end="")
    print()  # Nouvelle ligne
    
    # Ligne de séparation après les indices de colonnes
    print("     " + "-" * (max_width * matrice.shape[1]))
    
    # Afficher chaque ligne avec son indice
    for i in range(matrice.shape[0]):
        print(f"{i:3d} |", end="")
        for j in range(matrice.shape[1]):
            val = matrice[i, j]
            if val == 100:
                # Padding
                print(f"{'PAD':^{max_width}}", end="")
            elif val == -50:
                # Anomalie
                print(f"{'ANOM':^{max_width}}", end="")
            elif val == -10:
                # Token d'amorce
                print(f"{'AMORCE':^{max_width}}", end="")
            else:
                # Log probabilité normale
                if afficher_valeurs:
                    print(f"{val:^{max_width}.4f}", end="")
                else:
                    # Catégoriser les log probabilités
                    if val > -2:
                        print(f"{'TRÈS BON':^{max_width}}", end="")
                    elif val > -5:
                        print(f"{'BON':^{max_width}}", end="")
                    elif val > -10:
                        print(f"{'MOYEN':^{max_width}}", end="")
                    else:
                        print(f"{'FAIBLE':^{max_width}}", end="")
        print()  # Nouvelle ligne
    
    # Ligne de séparation finale
    print(header_sep)
    
    # Légende
    print("Légende:")
    print("  - PAD    : Padding (valeur 100)")
    print("  - ANOM   : Anomalie (valeur -50)")
    print("  - AMORCE : Token d'amorce (valeur -10)")
    if not afficher_valeurs:
        print("  - TRÈS BON: Log probabilité > -2")
        print("  - BON     : Log probabilité entre -2 et -5")
        print("  - MOYEN   : Log probabilité entre -5 et -10")
        print("  - FAIBLE  : Log probabilité < -10")
    print(header_sep)

def visualiser_matrice(matrice, mode='heatmap', sauvegarder=False, nom_sortie='visualisation.png'):
    """
    Crée une visualisation graphique de la matrice
    
    Args:
        matrice (numpy.ndarray): La matrice à visualiser
        mode (str): Mode de visualisation ('heatmap' ou 'categorical')
        sauvegarder (bool): Si True, sauvegarde l'image
        nom_sortie (str): Nom du fichier de sortie pour sauvegarder l'image
    """
    # Créer une copie de la matrice pour la visualisation
    matrice_viz = matrice.copy()
    
    # Créer un masque pour les valeurs spéciales
    masque_padding = matrice == 100
    masque_anomalie = matrice == -50
    masque_amorce = matrice == -10
    
    # Appliquer des valeurs spécifiques pour la visualisation
    if mode == 'categorical':
        # Mode catégorique - utiliser des valeurs discrètes pour les catégories
        # 0: padding, 1: anomalie, 2: amorce, 3-6: différentes qualités de log probs
        matrice_viz = np.zeros_like(matrice)
        
        # Définir les catégories
        matrice_viz[masque_padding] = 0
        matrice_viz[masque_anomalie] = 1
        matrice_viz[masque_amorce] = 2
        
        # Catégoriser les log probabilités
        masque_tres_bon = (matrice > -2) & ~(masque_padding | masque_anomalie | masque_amorce)
        masque_bon = (matrice <= -2) & (matrice > -5) & ~(masque_padding | masque_anomalie | masque_amorce)
        masque_moyen = (matrice <= -5) & (matrice > -10) & ~(masque_padding | masque_anomalie | masque_amorce)
        masque_faible = (matrice <= -10) & ~(masque_padding | masque_anomalie | masque_amorce)
        
        matrice_viz[masque_tres_bon] = 3
        matrice_viz[masque_bon] = 4
        matrice_viz[masque_moyen] = 5
        matrice_viz[masque_faible] = 6
        
        # Définir les couleurs pour chaque catégorie
        cmap = plt.cm.colors.ListedColormap(['lightgray', 'red', 'purple', 'darkgreen', 'green', 'orange', 'brown'])
        vmin, vmax = 0, 6
        
    else:  # mode == 'heatmap'
        # Mode heatmap - normaliser les log probabilités
        # Conserver les valeurs spéciales (ne plus remplacer padding par NaN)
        # Les paddings gardent leur valeur 100 pour apparaître sur l'échelle
        matrice_viz[masque_anomalie] = -50
        matrice_viz[masque_amorce] = -10
        
        # Nous ne limitons plus les valeurs comme avant (-20)
        # Nouvelle échelle de -50 à 100
        
        # Utiliser une colormap standard (pas besoin de masque pour NaN)
        cmap = plt.cm.viridis_r
        vmin, vmax = -50, 100  # Nouvelle échelle demandée
    
    # Créer la figure et configurer la taille en fonction des dimensions de la matrice
    fig_width = max(8, matrice.shape[1] * 0.5)
    fig_height = max(6, matrice.shape[0] * 0.5)
    plt.figure(figsize=(fig_width, fig_height))
    
    # Créer la heatmap
    img = plt.imshow(matrice_viz, cmap=cmap, vmin=vmin, vmax=vmax, aspect='auto')
    
    # Configurer les axes et titres
    plt.title("Visualisation de la matrice de log probabilités", fontsize=14)
    plt.xlabel("Position du token dans la ligne", fontsize=12)
    plt.ylabel("Numéro de ligne", fontsize=12)
    
    # Ajouter les ticks pour chaque ligne et colonne si la matrice n'est pas trop grande
    if matrice.shape[0] <= 20:
        plt.yticks(range(matrice.shape[0]))
    if matrice.shape[1] <= 20:
        plt.xticks(range(matrice.shape[1]))
    
    # Ajouter une barre de couleur avec légende
    cbar = plt.colorbar(img)
    
    if mode == 'categorical':
        # Légende pour le mode catégorique
        cbar.set_ticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
        cbar.set_ticklabels(['Padding', 'Anomalie', 'Amorce', 'Très bon', 'Bon', 'Moyen', 'Faible'])
    else:
        # Légende pour le mode heatmap
        cbar.set_label('Log probabilité')
    
    # Ajouter une grille pour mieux voir les cellules
    plt.grid(True, color='gray', linestyle='-', linewidth=0.5, alpha=0.3)
    
    # Ajuster la mise en page
    plt.tight_layout()
    
    # Sauvegarder si demandé
    if sauvegarder:
        plt.savefig(nom_sortie, dpi=300, bbox_inches='tight')
        print(f"Visualisation sauvegardée dans {nom_sortie}")
    
    # Afficher le graphique
    plt.show()

def main():
    """Fonction principale"""
    # Configurer le parseur d'arguments
    parser = argparse.ArgumentParser(description="Visualiser une matrice de log probabilités stockée dans un fichier .npy")
    
    parser.add_argument("fichier", nargs="?", default="matrice_logprob.npy", help="Chemin vers le fichier .npy contenant la matrice (défaut: matrice_logprob.npy)")
    parser.add_argument("--console", "-c", action="store_true", help="Afficher la matrice dans la console")
    parser.add_argument("--values", "-v", action="store_true", help="Afficher les valeurs numériques dans la console (plutôt que des catégories)")
    parser.add_argument("--mode", "-m", choices=["heatmap", "categorical"], default="heatmap", help="Mode de visualisation graphique (défaut: heatmap)")
    parser.add_argument("--save", "-o", action="store_true", help="Sauvegarder la visualisation")
    parser.add_argument("--output", default="visualisation.png", help="Nom du fichier de sortie pour la visualisation (défaut: visualisation.png)")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Vérifier si le fichier existe
    if not os.path.exists(args.fichier):
        print(f"Erreur: Le fichier {args.fichier} n'existe pas.")
        exit(1)
    
    # Charger la matrice
    matrice = charger_matrice(args.fichier)
    
    # Afficher dans la console si demandé
    if args.console:
        afficher_matrice_console(matrice, args.values)
    
    # Toujours faire la visualisation graphique
    visualiser_matrice(matrice, args.mode, args.save, args.output)

if __name__ == "__main__":
    main()