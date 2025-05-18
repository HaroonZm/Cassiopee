import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os
import argparse
from matplotlib.colors import Normalize
import glob

def charger_matrice(chemin_fichier):
    """
    Charge une matrice NumPy à partir d'un fichier.
    
    Arguments:
        chemin_fichier (str): Chemin vers le fichier contenant la matrice NumPy
        
    Retourne:
        numpy.ndarray: La matrice chargée
    """
    try:
        if chemin_fichier.endswith('.npy'):
            # Charger un fichier .npy
            return np.load(chemin_fichier)
        elif chemin_fichier.endswith('.npz'):
            # Charger un fichier .npz (archive de plusieurs matrices)
            # On prend la première matrice de l'archive
            with np.load(chemin_fichier) as data:
                return data[list(data.keys())[0]]
        elif chemin_fichier.endswith('.txt') or chemin_fichier.endswith('.csv'):
            # Charger un fichier texte
            return np.loadtxt(chemin_fichier)
        else:
            raise ValueError(f"Format de fichier non supporté: {chemin_fichier}")
    except Exception as e:
        raise Exception(f"Erreur lors du chargement de la matrice: {e}")

def charger_tuiles_avec_prefixe(dossier, prefixe):
    """
    Charge les tuiles et les métadonnées depuis un répertoire pour un préfixe spécifique.
    
    Arguments:
        dossier (str): Chemin vers le répertoire contenant les tuiles
        prefixe (str): Préfixe des fichiers de tuiles à charger
        
    Retourne:
        tuple: (tuiles, metadonnees)
            - tuiles: numpy.ndarray contenant toutes les tuiles
            - metadonnees: dict contenant les métadonnées
    """
    # Charger les métadonnées
    chemin_metadonnees = os.path.join(dossier, f'{prefixe}_metadonnees.npz')
    if not os.path.exists(chemin_metadonnees):
        raise FileNotFoundError(f"Fichier de métadonnées non trouvé: {chemin_metadonnees}")
    
    with np.load(chemin_metadonnees) as data:
        metadonnees = {key: data[key] for key in data.keys()}
    
    # Extraire les dimensions des tuiles
    nb_tuiles_lignes = int(metadonnees['nb_tuiles_lignes'])
    nb_tuiles_colonnes = int(metadonnees['nb_tuiles_colonnes'])
    taille_tuile_lignes = int(metadonnees['taille_tuile_lignes'])
    taille_tuile_colonnes = int(metadonnees['taille_tuile_colonnes'])
    
    # Créer le tableau des tuiles
    tuiles = np.zeros((nb_tuiles_lignes, nb_tuiles_colonnes, taille_tuile_lignes, taille_tuile_colonnes))
    
    # Charger chaque tuile
    for i in range(nb_tuiles_lignes):
        for j in range(nb_tuiles_colonnes):
            nom_fichier = f"{prefixe}_tuile_{i}_{j}.npy"
            chemin_fichier = os.path.join(dossier, nom_fichier)
            if not os.path.exists(chemin_fichier):
                raise FileNotFoundError(f"Fichier de tuile non trouvé: {chemin_fichier}")
            
            tuiles[i, j] = np.load(chemin_fichier)
    
    return tuiles, metadonnees

def trouver_matrices_dans_dossier(dossier):
    """
    Trouve toutes les matrices dans le dossier en cherchant les fichiers de métadonnées.
    
    Arguments:
        dossier (str): Chemin vers le répertoire contenant les tuiles
        
    Retourne:
        list: Liste des préfixes de matrices trouvées
    """
    pattern = os.path.join(dossier, '*_metadonnees.npz')
    fichiers_metadonnees = glob.glob(pattern)
    
    prefixes = []
    for fichier in fichiers_metadonnees:
        nom_base = os.path.basename(fichier)
        prefixe = nom_base.replace('_metadonnees.npz', '')
        prefixes.append(prefixe)
    
    return prefixes

def reconstituer_matrice(tuiles, dimensions_originales=None):
    """
    Reconstitue une matrice à partir d'un tableau de tuiles.
    
    Arguments:
        tuiles (numpy.ndarray): Tableau de tuiles
        dimensions_originales (tuple, optional): Dimensions (hauteur, largeur) de la matrice originale
        
    Retourne:
        numpy.ndarray: La matrice reconstituée
    """
    nb_tuiles_lignes, nb_tuiles_colonnes, taille_tuile_lignes, taille_tuile_colonnes = tuiles.shape
    
    # Dimensions de la matrice reconstituée avec padding
    hauteur_paddee = nb_tuiles_lignes * taille_tuile_lignes
    largeur_paddee = nb_tuiles_colonnes * taille_tuile_colonnes
    
    # Création de la matrice reconstituée avec padding
    matrice_paddee = np.zeros((hauteur_paddee, largeur_paddee), dtype=tuiles.dtype)
    
    # Remplissage de la matrice
    for i in range(nb_tuiles_lignes):
        for j in range(nb_tuiles_colonnes):
            debut_ligne = i * taille_tuile_lignes
            fin_ligne = (i + 1) * taille_tuile_lignes
            debut_colonne = j * taille_tuile_colonnes
            fin_colonne = (j + 1) * taille_tuile_colonnes
            
            matrice_paddee[debut_ligne:fin_ligne, debut_colonne:fin_colonne] = tuiles[i, j]
    
    # Si dimensions originales fournies, enlever le padding
    if dimensions_originales:
        hauteur_originale, largeur_originale = dimensions_originales
        matrice = matrice_paddee[:hauteur_originale, :largeur_originale]
        return matrice
    
    return matrice_paddee

def visualiser_matrice_et_tuiles(matrice, tuiles, titre="Matrice", metadonnees=None):
    """
    Visualise la matrice originale et ses tuiles.
    
    Arguments:
        matrice (numpy.ndarray): La matrice originale
        tuiles (numpy.ndarray): Le tableau de tuiles
        titre (str): Titre de la visualisation
        metadonnees (dict, optional): Métadonnées des tuiles
    """
    nb_tuiles_lignes, nb_tuiles_colonnes = tuiles.shape[:2]
    taille_tuile_lignes, taille_tuile_colonnes = tuiles.shape[2:]
    
    # Dimensions originales si disponibles
    dimensions_originales = None
    if metadonnees and 'hauteur_originale' in metadonnees and 'largeur_originale' in metadonnees:
        dimensions_originales = (int(metadonnees['hauteur_originale']), int(metadonnees['largeur_originale']))
    
    # Normalisation des valeurs pour l'affichage
    vmin = np.min(matrice)
    vmax = np.max(matrice)
    norm = Normalize(vmin=vmin, vmax=vmax)
    
    # Création de la figure principale
    fig = plt.figure(figsize=(16, 10))
    fig.suptitle(titre, fontsize=16)
    gs = gridspec.GridSpec(2, 2, width_ratios=[2, 1], height_ratios=[1, 1])
    
    # Matrice originale
    ax1 = plt.subplot(gs[0, 0])
    im1 = ax1.imshow(matrice, cmap='viridis', norm=norm)
    ax1.set_title("Matrice Originale")
    
    # Ajouter les limites des tuiles
    for i in range(1, nb_tuiles_lignes):
        ax1.axhline(y=i*taille_tuile_lignes - 0.5, color='r', linestyle='-', alpha=0.7, linewidth=0.5)
    for j in range(1, nb_tuiles_colonnes):
        ax1.axvline(x=j*taille_tuile_colonnes - 0.5, color='r', linestyle='-', alpha=0.7, linewidth=0.5)
    
    # Matrice reconstituée
    if dimensions_originales:
        matrice_reconstituee = reconstituer_matrice(tuiles, dimensions_originales)
    else:
        matrice_reconstituee = reconstituer_matrice(tuiles)
    
    ax2 = plt.subplot(gs[0, 1])
    im2 = ax2.imshow(matrice_reconstituee, cmap='viridis', norm=norm)
    ax2.set_title("Matrice Reconstituée")
    
    # Grille de tuiles
    ax3 = plt.subplot(gs[1, :])
    # Calculer la taille de la grille
    n_cols = min(nb_tuiles_colonnes, 8)  # Maximum 8 colonnes
    n_rows = (nb_tuiles_lignes * nb_tuiles_colonnes + n_cols - 1) // n_cols
    
    # Créer une sous-grille pour les tuiles
    gs_tuiles = gridspec.GridSpecFromSubplotSpec(n_rows, n_cols, subplot_spec=gs[1, :], wspace=0.1, hspace=0.3)
    
    # Afficher chaque tuile
    for i in range(nb_tuiles_lignes):
        for j in range(nb_tuiles_colonnes):
            idx = i * nb_tuiles_colonnes + j
            row, col = idx // n_cols, idx % n_cols
            
            ax = plt.subplot(gs_tuiles[row, col])
            im = ax.imshow(tuiles[i, j], cmap='viridis', norm=norm)
            ax.set_title(f"Tuile ({i},{j})", fontsize=8)
            ax.set_xticks([])
            ax.set_yticks([])
    
    # Ajouter une barre de couleur
    cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
    fig.colorbar(im1, cax=cbar_ax)
    
    plt.tight_layout(rect=[0, 0, 0.9, 1])
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    
    return fig

def visualiser_tuile_specifique(tuiles, indice_ligne, indice_colonne, titre="Tuile", metadonnees=None):
    """
    Visualise une tuile spécifique.
    
    Arguments:
        tuiles (numpy.ndarray): Le tableau de tuiles
        indice_ligne (int): L'indice de ligne de la tuile à visualiser
        indice_colonne (int): L'indice de colonne de la tuile à visualiser
        titre (str): Titre de la visualisation
        metadonnees (dict, optional): Métadonnées des tuiles
    """
    nb_tuiles_lignes, nb_tuiles_colonnes = tuiles.shape[:2]
    
    if indice_ligne < 0 or indice_ligne >= nb_tuiles_lignes or indice_colonne < 0 or indice_colonne >= nb_tuiles_colonnes:
        raise ValueError(f"Indices de tuile invalides: ({indice_ligne},{indice_colonne}). Plage valide: (0-{nb_tuiles_lignes-1},0-{nb_tuiles_colonnes-1})")
    
    # Créer la figure
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.suptitle(titre, fontsize=14)
    
    # Afficher la tuile
    tuile = tuiles[indice_ligne, indice_colonne]
    im = ax.imshow(tuile, cmap='viridis')
    ax.set_title(f"Tuile ({indice_ligne},{indice_colonne})")
    
    # Ajouter une grille pour visualiser les pixels
    ax.set_xticks(np.arange(-0.5, tuile.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, tuile.shape[0], 1), minor=True)
    ax.grid(which='minor', color='w', linestyle='-', linewidth=0.5)
    
    # Ajouter les valeurs dans chaque cellule
    for i in range(tuile.shape[0]):
        for j in range(tuile.shape[1]):
            text = ax.text(j, i, f"{tuile[i, j]:.1f}", ha="center", va="center", color="w", fontsize=8)
    
    # Ajouter une barre de couleur
    fig.colorbar(im, ax=ax)
    
    plt.tight_layout()
    
    return fig

def visualiser_toutes_matrices(dossier_tuiles, dossier_sortie=None, tuile_specifique=None):
    """
    Visualise toutes les matrices et leurs tuiles trouvées dans le dossier.
    
    Arguments:
        dossier_tuiles (str): Chemin vers le répertoire contenant les tuiles
        dossier_sortie (str, optional): Chemin vers le répertoire pour sauvegarder les visualisations
        tuile_specifique (tuple, optional): Indices (ligne, colonne) de la tuile spécifique à visualiser
    """
    # Trouver toutes les matrices
    prefixes = trouver_matrices_dans_dossier(dossier_tuiles)
    
    if not prefixes:
        print(f"Aucune matrice trouvée dans {dossier_tuiles}")
        return
    
    print(f"Matrices trouvées: {len(prefixes)}")
    
    # Créer le dossier de sortie si nécessaire
    if dossier_sortie:
        os.makedirs(dossier_sortie, exist_ok=True)
    
    # Traiter chaque matrice
    for prefixe in prefixes:
        try:
            print(f"\nTraitement de la matrice: {prefixe}")
            
            # Charger les tuiles
            tuiles, metadonnees = charger_tuiles_avec_prefixe(dossier_tuiles, prefixe)
            print(f"Tuiles chargées avec succès. Nombre de tuiles: {tuiles.shape[0]}×{tuiles.shape[1]}")
            
            # Reconstituer la matrice
            if 'hauteur_originale' in metadonnees and 'largeur_originale' in metadonnees:
                dimensions_originales = (int(metadonnees['hauteur_originale']), int(metadonnees['largeur_originale']))
                matrice = reconstituer_matrice(tuiles, dimensions_originales)
            else:
                matrice = reconstituer_matrice(tuiles)
            
            print(f"Matrice reconstituée. Dimensions: {matrice.shape}")
            
            # Visualiser une tuile spécifique si demandé
            if tuile_specifique:
                indice_ligne, indice_colonne = tuile_specifique
                fig = visualiser_tuile_specifique(tuiles, indice_ligne, indice_colonne, 
                                                 f"{prefixe} - Tuile ({indice_ligne},{indice_colonne})", 
                                                 metadonnees)
                
                if dossier_sortie:
                    chemin_sortie = os.path.join(dossier_sortie, f"{prefixe}_tuile_{indice_ligne}_{indice_colonne}.png")
                    fig.savefig(chemin_sortie, dpi=300, bbox_inches='tight')
                    print(f"Visualisation sauvegardée dans {chemin_sortie}")
            
            # Visualiser la matrice et ses tuiles
            else:
                fig = visualiser_matrice_et_tuiles(matrice, tuiles, f"Matrice: {prefixe}", metadonnees)
                
                if dossier_sortie:
                    chemin_sortie = os.path.join(dossier_sortie, f"{prefixe}_visualisation.png")
                    fig.savefig(chemin_sortie, dpi=300, bbox_inches='tight')
                    print(f"Visualisation sauvegardée dans {chemin_sortie}")
            
            plt.close(fig)  # Fermer la figure pour libérer de la mémoire
            
        except Exception as e:
            print(f"Erreur lors du traitement de {prefixe}: {e}")
            continue

def main():
    """
    Fonction principale du script.
    """
    # Configuration du parser d'arguments
    parser = argparse.ArgumentParser(description='Visualisation de matrices NumPy et leurs tuiles')
    parser.add_argument('--dossier_tuiles', required=True, 
                        help='Chemin vers le répertoire contenant les tuiles')
    parser.add_argument('--dossier_sortie', 
                        help='Chemin vers le répertoire pour sauvegarder les visualisations (optionnel)')
    parser.add_argument('--tuile_specifique', type=int, nargs=2, 
                        help='Indices (ligne, colonne) de la tuile spécifique à visualiser')
    parser.add_argument('--afficher', action='store_true', 
                        help='Afficher les visualisations (par défaut: False)')
    
    # Parsing des arguments
    args = parser.parse_args()
    
    try:
        # Visualiser toutes les matrices
        visualiser_toutes_matrices(args.dossier_tuiles, args.dossier_sortie, args.tuile_specifique)
        
        # Afficher les visualisations si demandé
        if args.afficher:
            plt.show()
        
    except Exception as e:
        print(f"Erreur: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()