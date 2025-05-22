import numpy as np
import os
import argparse
import glob
import shutil
from pathlib import Path

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

def sauvegarder_tuiles_direct(tuiles, dossier_sortie, nom_base, chemin_relatif="", dimensions_originales=None):
    """
    Sauvegarde les tuiles directement dans le répertoire de sortie avec le préfixe du nom du fichier original.
    
    Arguments:
        tuiles (numpy.ndarray): Tableau de tuiles
        dossier_sortie (str): Chemin vers le répertoire de sortie
        nom_base (str): Nom de base du fichier original (sans extension)
        chemin_relatif (str): Chemin relatif du sous-dossier pour préserver la structure
        dimensions_originales (tuple, optional): Dimensions originales de la matrice
    """
    # Création du répertoire de sortie complet (y compris le chemin relatif)
    dossier_sortie_complet = os.path.join(dossier_sortie, chemin_relatif)
    os.makedirs(dossier_sortie_complet, exist_ok=True)
    
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
    
    np.savez(os.path.join(dossier_sortie_complet, f'{nom_base}_metadonnees.npz'), **metadonnees)
    
    # Sauvegarde de chaque tuile
    for i in range(nb_tuiles_lignes):
        for j in range(nb_tuiles_colonnes):
            nom_fichier = f"{nom_base}_tuile_{i}_{j}.npy"
            chemin_fichier = os.path.join(dossier_sortie_complet, nom_fichier)
            np.save(chemin_fichier, tuiles[i, j])
    
    print(f"Les tuiles ont été sauvegardées dans {dossier_sortie_complet}")
    print(f"Nombre total de tuiles: {nb_tuiles_lignes * nb_tuiles_colonnes}")

def deplacer_fichier(chemin_source, dossier_destination, chemin_relatif=""):
    """
    Déplace un fichier vers un dossier de destination en préservant la structure des sous-dossiers.
    
    Arguments:
        chemin_source (str): Chemin complet du fichier à déplacer
        dossier_destination (str): Dossier de destination racine
        chemin_relatif (str): Chemin relatif pour préserver la structure
        
    Retourne:
        str: Chemin de destination où le fichier a été déplacé
    """
    # Création du dossier de destination complet
    dossier_destination_complet = os.path.join(dossier_destination, chemin_relatif)
    os.makedirs(dossier_destination_complet, exist_ok=True)
    
    # Chemin de destination complet
    nom_fichier = os.path.basename(chemin_source)
    chemin_destination = os.path.join(dossier_destination_complet, nom_fichier)
    
    # Déplacement du fichier (pas de copie)
    shutil.move(chemin_source, chemin_destination)
    
    print(f"Fichier déplacé: {chemin_source} -> {chemin_destination}")
    return chemin_destination

def traiter_matrices_recursive(dossier_racine, dossier_sortie, dossier_archive, taille_tuile_lignes, taille_tuile_colonnes, padding, valeur_padding):
    """
    Traite récursivement tous les fichiers de matrices NumPy dans un dossier et ses sous-dossiers.
    
    Arguments:
        dossier_racine (str): Chemin vers le dossier racine contenant les matrices NumPy
        dossier_sortie (str): Chemin vers le dossier de sortie pour les tuiles
        dossier_archive (str): Chemin vers le dossier d'archive pour les matrices traitées
        taille_tuile_lignes (int): Nombre de lignes pour chaque tuile
        taille_tuile_colonnes (int): Nombre de colonnes pour chaque tuile
        padding (bool): Si True, ajoute du padding si nécessaire
        valeur_padding (int/float): Valeur à utiliser pour le padding
    """
    # Création des dossiers de sortie et d'archive s'ils n'existent pas
    os.makedirs(dossier_sortie, exist_ok=True)
    os.makedirs(dossier_archive, exist_ok=True)
    
    # Extensions de fichiers supportées
    extensions = ['*.npy', '*.npz', '*.txt', '*.csv']
    
    # Conversion en Path pour faciliter les manipulations
    dossier_racine_p = Path(dossier_racine)
    
    # Liste pour stocker tous les fichiers trouvés
    fichiers_trouves = []
    
    # Recherche des fichiers avec les extensions supportées dans tous les sous-dossiers
    for ext in extensions:
        for fichier in dossier_racine_p.glob(f"**/{ext}"):
            fichiers_trouves.append(fichier)
    
    if not fichiers_trouves:
        print(f"Aucun fichier compatible trouvé dans {dossier_racine} et ses sous-dossiers")
        return
    
    print(f"Nombre de fichiers trouvés: {len(fichiers_trouves)}")
    
    # Traitement de chaque fichier
    for chemin_fichier in fichiers_trouves:
        try:
            # Conversion en chaîne pour compatibilité
            chemin_fichier_str = str(chemin_fichier)
            
            # Extraction du nom du fichier sans extension
            nom_fichier = chemin_fichier.name
            nom_base, _ = os.path.splitext(nom_fichier)
            
            # Calcul du chemin relatif par rapport au dossier racine
            chemin_relatif = str(chemin_fichier.parent.relative_to(dossier_racine_p))
            if chemin_relatif == '.':
                chemin_relatif = ""
            
            print(f"\nTraitement de {chemin_fichier_str}...")
            
            # Chargement de la matrice
            matrice = charger_matrice(chemin_fichier_str)
            print(f"Matrice chargée avec succès. Dimensions: {matrice.shape}")
            
            # Tuilage de la matrice
            print(f"Tuilage de la matrice avec des tuiles de taille {taille_tuile_lignes}×{taille_tuile_colonnes}...")
            tuiles, dimensions_originales = tuiler_matrice(matrice, taille_tuile_lignes, taille_tuile_colonnes, 
                                                          padding, valeur_padding)
            
            # Affichage des informations sur les tuiles
            afficher_infos_tuiles(tuiles)
            
            # Sauvegarde des tuiles en préservant la structure des sous-dossiers
            print(f"Sauvegarde des tuiles...")
            sauvegarder_tuiles_direct(tuiles, dossier_sortie, nom_base, chemin_relatif, dimensions_originales)
            
            # Déplacement du fichier original vers l'archive (pas de copie)
            print(f"Déplacement du fichier original vers l'archive...")
            chemin_destination = deplacer_fichier(chemin_fichier_str, dossier_archive, chemin_relatif)
            print(f"Fichier original déplacé vers: {chemin_destination}")
            
            print(f"Traitement de {nom_fichier} terminé avec succès!")
            
        except Exception as e:
            print(f"Erreur lors du traitement de {chemin_fichier}: {e}")
            continue

def main():
    """
    Fonction principale du script.
    """
    # Configuration du parser d'arguments
    parser = argparse.ArgumentParser(description='Tuilage récursif de matrices NumPy dans un dossier et ses sous-dossiers')
    parser.add_argument('dossier_racine', help='Chemin vers le dossier racine contenant les matrices NumPy (.npy, .npz, .txt, .csv)')
    parser.add_argument('dossier_sortie', help='Chemin vers le répertoire de sortie pour les tuiles')
    parser.add_argument('dossier_archive', help='Chemin vers le répertoire d\'archive pour les matrices traitées')
    parser.add_argument('--taille_tuile', type=int, nargs=2, default=[3, 3], 
                        help='Taille des tuiles en lignes et colonnes (par défaut: 3 3)')
    parser.add_argument('--padding', type=bool, default=True,
                        help='Ajouter du padding si nécessaire (par défaut: True)')
    parser.add_argument('--valeur_padding', type=float, default=100,
                        help='Valeur à utiliser pour le padding (par défaut: 100)')
    
    # Parsing des arguments
    args = parser.parse_args()
    
    # Extraction des arguments
    dossier_racine = args.dossier_racine
    dossier_sortie = args.dossier_sortie
    dossier_archive = args.dossier_archive
    taille_tuile_lignes, taille_tuile_colonnes = args.taille_tuile
    padding = args.padding
    valeur_padding = args.valeur_padding
    
    try:
        # Vérification de l'existence du dossier racine
        if not os.path.isdir(dossier_racine):
            raise ValueError(f"Le dossier racine {dossier_racine} n'existe pas ou n'est pas un dossier.")
        
        # Traitement récursif des fichiers dans le dossier et ses sous-dossiers
        print(f"Recherche et traitement de matrices NumPy dans {dossier_racine} et ses sous-dossiers...")
        traiter_matrices_recursive(dossier_racine, dossier_sortie, dossier_archive, 
                                  taille_tuile_lignes, taille_tuile_colonnes, 
                                  padding, valeur_padding)
        
        print("\nTraitement de tous les fichiers terminé!")
        
    except Exception as e:
        print(f"Erreur: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()