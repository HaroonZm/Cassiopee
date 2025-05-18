import numpy as np
import os
import argparse
import glob

def tuiler_matrice(matrice, taille_tuile_lignes, taille_tuile_colonnes, padding=True, valeur_padding=100):
    """
    Divise une matrice NumPy en tuiles de taille spécifiée.
    
    Arguments:
        matrice (numpy.ndarray): La matrice d'entrée à tuiler
        taille_tuile_lignes (int): Nombre de lignes pour chaque tuile
        taille_tuile_colonnes (int): Nombre de colonnes pour chaque tuile
        padding (bool): Si True, ajoute du padding si nécessaire pour que la matrice soit divisible par la taille des tuiles
        valeur_padding (int/float): Valeur à utiliser pour le padding
        
    Retourne:
        tuple: (tuiles, dimensions_originales)
            - tuiles: numpy.ndarray de tuiles
            - dimensions_originales: tuple (hauteur, largeur) de la matrice originale
    """
    
    # Dimensions de la matrice d'entrée
    hauteur_originale, largeur_originale = matrice.shape
    dimensions_originales = (hauteur_originale, largeur_originale)
    
    # Calcul des dimensions avec padding si nécessaire
    if padding:
        padding_hauteur = (taille_tuile_lignes - hauteur_originale % taille_tuile_lignes) % taille_tuile_lignes
        padding_largeur = (taille_tuile_colonnes - largeur_originale % taille_tuile_colonnes) % taille_tuile_colonnes
        
        # Ajout du padding
        if padding_hauteur > 0 or padding_largeur > 0:
            matrice_paddee = np.full((hauteur_originale + padding_hauteur, largeur_originale + padding_largeur), 
                                     valeur_padding, dtype=matrice.dtype)
            matrice_paddee[:hauteur_originale, :largeur_originale] = matrice
            matrice = matrice_paddee
            
    # Dimensions après padding
    hauteur, largeur = matrice.shape
    
    # Vérification que les dimensions sont divisibles par la taille des tuiles
    if hauteur % taille_tuile_lignes != 0 or largeur % taille_tuile_colonnes != 0:
        raise ValueError("La matrice ne peut pas être tuilée avec les dimensions spécifiées sans padding.")
    
    # Nombre de tuiles dans chaque dimension
    nb_tuiles_lignes = hauteur // taille_tuile_lignes
    nb_tuiles_colonnes = largeur // taille_tuile_colonnes
    
    # Création du tableau de tuiles
    tuiles = np.zeros((nb_tuiles_lignes, nb_tuiles_colonnes, taille_tuile_lignes, taille_tuile_colonnes), 
                      dtype=matrice.dtype)
    
    # Remplissage des tuiles
    for i in range(nb_tuiles_lignes):
        for j in range(nb_tuiles_colonnes):
            debut_ligne = i * taille_tuile_lignes
            fin_ligne = (i + 1) * taille_tuile_lignes
            debut_colonne = j * taille_tuile_colonnes
            fin_colonne = (j + 1) * taille_tuile_colonnes
            
            tuiles[i, j] = matrice[debut_ligne:fin_ligne, debut_colonne:fin_colonne]
    
    return tuiles, dimensions_originales

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

def sauvegarder_tuiles(tuiles, dossier_sortie, dimensions_originales=None):
    """
    Sauvegarde les tuiles dans un répertoire.
    
    Arguments:
        tuiles (numpy.ndarray): Tableau de tuiles
        dossier_sortie (str): Chemin vers le répertoire de sortie
        dimensions_originales (tuple, optional): Dimensions originales de la matrice
    """
    # Création du répertoire de sortie s'il n'existe pas
    os.makedirs(dossier_sortie, exist_ok=True)
    
    # Sauvegarde des métadonnées
    nb_tuiles_lignes, nb_tuiles_colonnes, taille_tuile_lignes, taille_tuile_colonnes = tuiles.shape
    metadonnees = {
        'nb_tuiles_lignes': nb_tuiles_lignes,
        'nb_tuiles_colonnes': nb_tuiles_colonnes,
        'taille_tuile_lignes': taille_tuile_lignes,
        'taille_tuile_colonnes': taille_tuile_colonnes
    }
    
    if dimensions_originales:
        metadonnees['hauteur_originale'] = dimensions_originales[0]
        metadonnees['largeur_originale'] = dimensions_originales[1]
    
    np.savez(os.path.join(dossier_sortie, 'metadonnees.npz'), **metadonnees)
    
    # Sauvegarde de chaque tuile
    for i in range(nb_tuiles_lignes):
        for j in range(nb_tuiles_colonnes):
            nom_fichier = f"tuile_{i}_{j}.npy"
            chemin_fichier = os.path.join(dossier_sortie, nom_fichier)
            np.save(chemin_fichier, tuiles[i, j])
    
    print(f"Les tuiles ont été sauvegardées dans {dossier_sortie}")
    print(f"Nombre total de tuiles: {nb_tuiles_lignes * nb_tuiles_colonnes}")

def afficher_infos_tuiles(tuiles):
    """
    Affiche des informations sur les tuiles créées.
    
    Arguments:
        tuiles (numpy.ndarray): Tableau de tuiles
    """
    nb_tuiles_lignes, nb_tuiles_colonnes, taille_tuile_lignes, taille_tuile_colonnes = tuiles.shape
    
    print("\nInformations sur les tuiles:")
    print(f"Nombre de tuiles: {nb_tuiles_lignes}×{nb_tuiles_colonnes} = {nb_tuiles_lignes * nb_tuiles_colonnes} tuiles")
    print(f"Taille de chaque tuile: {taille_tuile_lignes}×{taille_tuile_colonnes}")
    
    # Afficher les dimensions de quelques tuiles
    print("\nExemples de tuiles:")
    if nb_tuiles_lignes > 0 and nb_tuiles_colonnes > 0:
        print(f"Tuile (0,0):")
        print(tuiles[0, 0])
    
    if nb_tuiles_lignes > 1 and nb_tuiles_colonnes > 1:
        print(f"\nTuile (1,1):")
        print(tuiles[1, 1])
    
    if nb_tuiles_lignes > 0 and nb_tuiles_colonnes > 0:
        print(f"\nDernière tuile ({nb_tuiles_lignes-1},{nb_tuiles_colonnes-1}):")
        print(tuiles[-1, -1])

def sauvegarder_tuiles_direct(tuiles, dossier_sortie, nom_base, dimensions_originales=None):
    """
    Sauvegarde les tuiles directement dans le répertoire de sortie avec le préfixe du nom du fichier original.
    
    Arguments:
        tuiles (numpy.ndarray): Tableau de tuiles
        dossier_sortie (str): Chemin vers le répertoire de sortie
        nom_base (str): Nom de base du fichier original (sans extension)
        dimensions_originales (tuple, optional): Dimensions originales de la matrice
    """
    # Création du répertoire de sortie s'il n'existe pas
    os.makedirs(dossier_sortie, exist_ok=True)
    
    # Sauvegarde des métadonnées
    nb_tuiles_lignes, nb_tuiles_colonnes, taille_tuile_lignes, taille_tuile_colonnes = tuiles.shape
    metadonnees = {
        'nom_base': nom_base,
        'nb_tuiles_lignes': nb_tuiles_lignes,
        'nb_tuiles_colonnes': nb_tuiles_colonnes,
        'taille_tuile_lignes': taille_tuile_lignes,
        'taille_tuile_colonnes': taille_tuile_colonnes
    }
    
    if dimensions_originales:
        metadonnees['hauteur_originale'] = dimensions_originales[0]
        metadonnees['largeur_originale'] = dimensions_originales[1]
    
    np.savez(os.path.join(dossier_sortie, f'{nom_base}_metadonnees.npz'), **metadonnees)
    
    # Sauvegarde de chaque tuile
    for i in range(nb_tuiles_lignes):
        for j in range(nb_tuiles_colonnes):
            nom_fichier = f"{nom_base}_tuile_{i}_{j}.npy"
            chemin_fichier = os.path.join(dossier_sortie, nom_fichier)
            np.save(chemin_fichier, tuiles[i, j])
    
    print(f"Les tuiles ont été sauvegardées dans {dossier_sortie}")
    print(f"Nombre total de tuiles: {nb_tuiles_lignes * nb_tuiles_colonnes}")

def tuiler_fichiers_dossier(dossier_entree, dossier_sortie, taille_tuile_lignes, taille_tuile_colonnes, padding, valeur_padding):
    """
    Traite tous les fichiers de matrices NumPy dans un dossier.
    
    Arguments:
        dossier_entree (str): Chemin vers le dossier contenant les fichiers de matrices
        dossier_sortie (str): Chemin vers le dossier de sortie pour les tuiles
        taille_tuile_lignes (int): Nombre de lignes pour chaque tuile
        taille_tuile_colonnes (int): Nombre de colonnes pour chaque tuile
        padding (bool): Si True, ajoute du padding si nécessaire
        valeur_padding (int/float): Valeur à utiliser pour le padding
    """
    # Création du dossier de sortie s'il n'existe pas
    os.makedirs(dossier_sortie, exist_ok=True)
    
    # Extensions de fichiers supportées
    extensions = ['*.npy', '*.npz', '*.txt', '*.csv']
    
    # Liste pour stocker tous les fichiers trouvés
    fichiers = []
    
    # Recherche des fichiers avec les extensions supportées
    for ext in extensions:
        pattern = os.path.join(dossier_entree, ext)
        fichiers.extend(glob.glob(pattern))
    
    if not fichiers:
        print(f"Aucun fichier compatible trouvé dans {dossier_entree}")
        return
    
    print(f"Nombre de fichiers trouvés: {len(fichiers)}")
    
    # Traitement de chaque fichier
    for chemin_fichier in fichiers:
        try:
            # Extraction du nom du fichier sans extension
            nom_fichier = os.path.basename(chemin_fichier)
            nom_base, _ = os.path.splitext(nom_fichier)
            
            print(f"\nTraitement de {chemin_fichier}...")
            
            # Chargement de la matrice
            matrice = charger_matrice(chemin_fichier)
            print(f"Matrice chargée avec succès. Dimensions: {matrice.shape}")
            
            # Tuilage de la matrice
            print(f"Tuilage de la matrice avec des tuiles de taille {taille_tuile_lignes}×{taille_tuile_colonnes}...")
            tuiles, dimensions_originales = tuiler_matrice(matrice, taille_tuile_lignes, taille_tuile_colonnes, 
                                                          padding, valeur_padding)
            
            # Affichage des informations sur les tuiles
            afficher_infos_tuiles(tuiles)
            
            # Sauvegarde des tuiles directement dans le dossier de sortie
            print(f"Sauvegarde des tuiles dans {dossier_sortie}...")
            sauvegarder_tuiles_direct(tuiles, dossier_sortie, nom_base, dimensions_originales)
            
            print(f"Tuilage de {nom_fichier} terminé avec succès!")
            
        except Exception as e:
            print(f"Erreur lors du traitement de {chemin_fichier}: {e}")
            continue

def main():
    """
    Fonction principale du script.
    """
    # Configuration du parser d'arguments
    parser = argparse.ArgumentParser(description='Tuilage de matrices NumPy')
    parser.add_argument('input_dir', help='Chemin vers le dossier contenant les matrices NumPy (.npy, .npz, .txt, .csv)')
    parser.add_argument('output_dir', help='Chemin vers le répertoire de sortie pour les tuiles')
    parser.add_argument('--taille_tuile', type=int, nargs=2, default=[3, 3], 
                        help='Taille des tuiles en lignes et colonnes (par défaut: 3 3)')
    
    # Parsing des arguments
    args = parser.parse_args()
    
    # Extraction des arguments
    dossier_entree = args.input_dir
    dossier_sortie = args.output_dir
    taille_tuile_lignes, taille_tuile_colonnes = args.taille_tuile
    
    # Valeurs par défaut pour le padding
    padding = True
    valeur_padding = 100
    
    try:
        # Vérification de l'existence du dossier d'entrée
        if not os.path.isdir(dossier_entree):
            raise ValueError(f"Le dossier d'entrée {dossier_entree} n'existe pas ou n'est pas un dossier.")
        
        # Traitement des fichiers dans le dossier
        print(f"Recherche de matrices NumPy dans {dossier_entree}...")
        tuiler_fichiers_dossier(dossier_entree, dossier_sortie, taille_tuile_lignes, taille_tuile_colonnes, 
                               padding, valeur_padding)
        
        print("\nTraitement de tous les fichiers terminé!")
        
    except Exception as e:
        print(f"Erreur: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()