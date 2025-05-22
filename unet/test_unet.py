#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import glob
import argparse
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import traceback
from tqdm import tqdm
import subprocess

# Architecture UNet pour la détection de code IA
class UNetForCodeDetection(nn.Module):
    def __init__(self):
        super(UNetForCodeDetection, self).__init__()
        # Encoder
        self.enc1 = self.conv_block(1, 64)
        self.enc2 = self.conv_block(64, 128)
        self.enc3 = self.conv_block(128, 256)
        self.enc4 = self.conv_block(256, 512)
        
        # Decoder
        self.upconv3 = nn.ConvTranspose2d(512, 256, kernel_size=2, stride=2)
        self.dec3 = self.conv_block(512, 256)
        
        self.upconv2 = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        self.dec2 = self.conv_block(256, 128)
        
        self.upconv1 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.dec1 = self.conv_block(128, 64)
        
        # Classification head
        self.final_conv = nn.Conv2d(64, 32, kernel_size=1)
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )
        
        # Max pooling
        self.pool = nn.MaxPool2d(2)
        
    def conv_block(self, in_ch, out_ch):
        return nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True)
        )
    
    def forward(self, x):
        # Encoder
        e1 = self.enc1(x)
        p1 = self.pool(e1)
        
        e2 = self.enc2(p1)
        p2 = self.pool(e2)
        
        e3 = self.enc3(p2)
        p3 = self.pool(e3)
        
        # Bottleneck
        e4 = self.enc4(p3)
        
        # Decoder avec gestion des dimensions
        d3 = self.upconv3(e4)
        # Vérifier et ajuster les dimensions si nécessaire
        if d3.size() != e3.size():
            d3 = F.interpolate(d3, size=e3.size()[2:], mode='bilinear', align_corners=True)
        d3 = torch.cat([d3, e3], dim=1)
        d3 = self.dec3(d3)
        
        d2 = self.upconv2(d3)
        # Vérifier et ajuster les dimensions si nécessaire
        if d2.size() != e2.size():
            d2 = F.interpolate(d2, size=e2.size()[2:], mode='bilinear', align_corners=True)
        d2 = torch.cat([d2, e2], dim=1)
        d2 = self.dec2(d2)
        
        d1 = self.upconv1(d2)
        # Vérifier et ajuster les dimensions si nécessaire
        if d1.size() != e1.size():
            d1 = F.interpolate(d1, size=e1.size()[2:], mode='bilinear', align_corners=True)
        d1 = torch.cat([d1, e1], dim=1)
        d1 = self.dec1(d1)
        
        # Classification
        x = self.final_conv(d1)
        output = self.classifier(x)
        return output

def preprocess_matrix(matrix):
    """
    Prétraite une matrice de la même manière que pendant l'entraînement
    """
    # Remplacer les valeurs -inf ou NaN par une valeur numérique
    matrix = np.nan_to_num(matrix, neginf=-100.0)
    
    # Normalisation min-max pour ramener entre 0 et 1
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    if max_val > min_val:  # Éviter la division par zéro
        matrix = (matrix - min_val) / (max_val - min_val)
    
    return matrix

def determine_true_class(filename):
    """
    Détermine la classe réelle à partir du nom de fichier
    """
    filename = filename.lower()
    if "var" in filename or "gen" in filename or "ia" in filename:
        return "IA"
    elif "human" in filename:
        return "Humain"
    else:
        return "Inconnu"

def test_single_file(model, file_path, device):
    """
    Teste le modèle sur un seul fichier
    """
    try:
        # Charger et prétraiter la matrice
        matrix = np.load(file_path)
        matrix = preprocess_matrix(matrix)
        
        # Vérifier la taille de la matrice
        print(f"Taille de la matrice originale: {matrix.shape}")
        
        # Si la matrice est trop petite, la redimensionner
        # La taille minimale requise dépend de l'architecture UNet
        # Pour un modèle avec 4 couches de downsample, la taille minimale est 16x16
        min_size = 16
        if matrix.shape[0] < min_size or matrix.shape[1] < min_size:
            print(f"Matrice redimensionnée de {matrix.shape} à au moins {min_size}x{min_size}")
            # Créer une nouvelle matrice de taille minimale, remplie de zéros
            new_matrix = np.zeros((max(min_size, matrix.shape[0]), max(min_size, matrix.shape[1])))
            # Copier les valeurs de la matrice originale
            new_matrix[:matrix.shape[0], :matrix.shape[1]] = matrix
            matrix = new_matrix
            print(f"Nouvelle taille de matrice: {matrix.shape}")
        
        # Conversion en tenseur
        matrix_tensor = torch.tensor(matrix, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
        matrix_tensor = matrix_tensor.to(device)
        
        # Prédiction
        with torch.no_grad():
            output = model(matrix_tensor).squeeze().item()
        
        # Déterminer la classe prédite
        predicted_class = "IA" if output > 0.5 else "Humain"
        confidence = output if output > 0.5 else 1 - output
        
        # Déterminer la classe réelle
        filename = os.path.basename(file_path)
        true_class = determine_true_class(filename)
        
        result = {
            'file': filename,
            'true_class': true_class,
            'predicted_class': predicted_class,
            'score': output,
            'confidence': confidence,
            'correct': predicted_class == true_class if true_class != "Inconnu" else None
        }
        
        print("\n" + "="*60)
        print(f"Résultat pour: {filename}")
        print("-"*60)
        print(f"Classe réelle: {true_class}")
        print(f"Prédiction: {predicted_class}")
        print(f"Score brut: {output:.4f}")
        print(f"Confiance: {confidence*100:.2f}%")
        if true_class != "Inconnu":
            print(f"Correct: {'✓' if predicted_class == true_class else '✗'}")
        print("="*60)
        
        return result
        
    except Exception as e:
        print(f"Erreur lors du test de {file_path}: {e}")
        traceback.print_exc()  # Afficher la trace complète de l'erreur
        return None

def test_directory(model, test_dir, device, recursive=False):
    """
    Teste le modèle sur tous les fichiers .npy d'un répertoire
    
    Args:
        model: Le modèle UNet chargé
        test_dir: Le répertoire contenant les fichiers .npy à tester
        device: Le périphérique de calcul (CPU/GPU)
        recursive: Si True, recherche également dans les sous-dossiers
    """
    # Trouver tous les fichiers .npy dans le répertoire
    if recursive:
        test_files = glob.glob(os.path.join(test_dir, "**/*.npy"), recursive=True)
    else:
        test_files = glob.glob(os.path.join(test_dir, "*.npy"))
    
    print(f"Trouvé {len(test_files)} fichiers à tester dans {test_dir}")
    
    if len(test_files) == 0:
        print("Aucun fichier .npy trouvé dans le répertoire spécifié!")
        return []
    
    results = []
    for file_path in tqdm(test_files, desc="Test des fichiers"):
        result = test_single_file(model, file_path, device)
        if result:
            results.append(result)
    
    # Calculer les statistiques
    correct_count = sum(1 for r in results if r['correct'] == True)
    total_known = sum(1 for r in results if r['correct'] is not None)
    
    print("\n" + "="*60)
    print("RÉSULTATS GLOBAUX")
    print("-"*60)
    
    if total_known > 0:
        accuracy = correct_count / total_known
        print(f"Précision globale: {accuracy*100:.2f}% ({correct_count}/{total_known})")
        
        # Statistiques par classe
        ia_total = sum(1 for r in results if r['true_class'] == "IA")
        ia_correct = sum(1 for r in results if r['true_class'] == "IA" and r['correct'])
        
        human_total = sum(1 for r in results if r['true_class'] == "Humain")
        human_correct = sum(1 for r in results if r['true_class'] == "Humain" and r['correct'])
        
        if ia_total > 0:
            print(f"Précision sur code IA: {(ia_correct/ia_total)*100:.2f}% ({ia_correct}/{ia_total})")
        
        if human_total > 0:
            print(f"Précision sur code Humain: {(human_correct/human_total)*100:.2f}% ({human_correct}/{human_total})")
    else:
        print("Aucun fichier avec une classe connue n'a été testé.")
    
    print("="*60)
    
    return results

def generate_matrix_and_tiles_from_python(py_file, output_dir=None, token_model="gpt-4o-mini", pred_model="gpt-4o-mini", tiles_size=(16, 16)):
    """
    Convertit un fichier Python en représentation matricielle puis en tuiles pour l'analyse
    en appelant matrix_generator_no_batch.py puis matrix_tiling.py.
    
    Args:
        py_file: Chemin vers le fichier Python
        output_dir: Répertoire de sortie pour la matrice et les tuiles
        token_model: Modèle à utiliser pour la tokenisation
        pred_model: Modèle à utiliser pour la prédiction
        tiles_size: Taille des tuiles (lignes, colonnes)
    
    Returns:
        Chemin vers le dossier contenant les tuiles générées
    """
    import subprocess
    import tempfile
    import time
    import glob
    
    try:
        # Créer un répertoire temporaire si aucun n'est spécifié
        if not output_dir:
            output_dir = tempfile.mkdtemp(prefix="matrix_temp_")
        else:
            os.makedirs(output_dir, exist_ok=True)
        
        # Nom de base du fichier
        base_name = os.path.basename(py_file).replace('.py', '')
        
        # 1. Générer la matrice avec matrix_generator_no_batch.py
        matrix_cmd = [
            "python", 
            "matrix_generation/matrix_generator_no_batch.py",
            "--file", py_file,
            "--token-model", token_model,
            "--pred-model", pred_model,
            "--output-dir", output_dir
        ]
        
        print(f"Étape 1: Génération de la matrice...")
        print(f"Exécution de la commande: {' '.join(matrix_cmd)}")
        
        # Exécuter la commande pour générer la matrice
        process = subprocess.Popen(
            matrix_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Lire et afficher la sortie
        matrix_path = None
        for line in process.stdout:
            print(line.strip())
            # Chercher le chemin de la matrice générée dans la sortie
            if "Matrice sauvegardée dans:" in line:
                matrix_path = line.split("Matrice sauvegardée dans:")[1].strip()
            elif "Matrice sauvegardée dans" in line:
                parts = line.split("Matrice sauvegardée dans")
                if len(parts) > 1:
                    matrix_path = parts[1].strip()
        
        # Attendre la fin du processus
        exit_code = process.wait()
        
        if exit_code != 0:
            print(f"Erreur lors de la génération de la matrice, code de sortie: {exit_code}")
            return None
        
        # Si nous n'avons pas trouvé le chemin dans la sortie, chercher la matrice
        if not matrix_path:
            # Recherche par motif de nom
            possible_paths = [
                os.path.join(output_dir, f"matrix_{base_name}.npy"),
                os.path.join(output_dir, "matrixes", f"matrix_{base_name}.npy"),
                os.path.join(output_dir, "matrices", f"matrix_{base_name}.npy")
            ]
            
            for path in possible_paths:
                if os.path.exists(path):
                    matrix_path = path
                    print(f"Matrice trouvée par motif de nom: {matrix_path}")
                    break
        
        # Si nous n'avons toujours pas trouvé la matrice, chercher tous les fichiers .npy
        if not matrix_path:
            npy_files = []
            for root, dirs, files in os.walk(output_dir):
                for file in files:
                    if file.endswith('.npy'):
                        full_path = os.path.join(root, file)
                        npy_files.append(full_path)
                        print(f"Matrice potentielle trouvée: {full_path}")
            
            # Si un seul fichier .npy a été trouvé, supposons que c'est notre matrice
            if len(npy_files) == 1:
                matrix_path = npy_files[0]
                print(f"Une seule matrice trouvée: {matrix_path}")
            elif len(npy_files) > 1:
                # Chercher le fichier avec le nom le plus proche
                for npy_file in npy_files:
                    if base_name.lower() in os.path.basename(npy_file).lower():
                        matrix_path = npy_file
                        print(f"Meilleure correspondance parmi plusieurs fichiers: {matrix_path}")
                        break
                
                # Si nous n'avons toujours pas trouvé de correspondance, prendre le plus récent
                if not matrix_path:
                    matrix_path = max(npy_files, key=os.path.getmtime)
                    print(f"Fichier le plus récent parmi plusieurs: {matrix_path}")
        
        if not matrix_path or not os.path.exists(matrix_path):
            print(f"Erreur: Aucune matrice générée trouvée")
            return None
        
        # 2. Convertir la matrice en tuiles avec matrix_tiling.py
        # Créer les dossiers pour les tuiles
        matrices_dir = os.path.dirname(matrix_path)
        tiles_dir = os.path.join(output_dir, "tiles")
        os.makedirs(tiles_dir, exist_ok=True)
        
        tiling_cmd = [
            "python",
            "matrix_generation/matrix_tiling.py",
            matrices_dir,
            tiles_dir,
            os.path.join(output_dir, "archive"),  # Dossier d'archive requis
            "--taille_tuile",
            str(tiles_size[0]),
            str(tiles_size[1])
        ]
        
        print(f"\nÉtape 2: Génération des tuiles...")
        print(f"Exécution de la commande: {' '.join(tiling_cmd)}")
        
        # Exécuter la commande pour générer les tuiles
        process = subprocess.Popen(
            tiling_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Lire et afficher la sortie
        for line in process.stdout:
            print(line.strip())
        
        # Attendre la fin du processus
        exit_code = process.wait()
        
        if exit_code != 0:
            print(f"Erreur lors de la génération des tuiles, code de sortie: {exit_code}")
            return None
        
        # Vérifier si des tuiles ont été générées
        tile_files = []
        for root, dirs, files in os.walk(tiles_dir):
            for file in files:
                if file.endswith('.npy'):
                    tile_files.append(os.path.join(root, file))
        
        if not tile_files:
            print(f"Aucune tuile générée dans {tiles_dir}")
            return None
        
        print(f"Génération réussie ! {len(tile_files)} tuiles ont été créées dans {tiles_dir}")
        return tiles_dir
    
    except Exception as e:
        print(f"Erreur lors de la génération de tuiles pour {py_file}: {str(e)}")
        traceback.print_exc()
        return None

def analyze_tiles_directory(model, tiles_dir, device):
    """
    Analyse toutes les tuiles dans un répertoire et retourne une prédiction globale
    
    Args:
        model: Le modèle UNet chargé
        tiles_dir: Chemin vers le répertoire contenant les tuiles
        device: Device à utiliser (cuda/cpu)
    
    Returns:
        Un dictionnaire avec le résultat de l'analyse
    """
    # Vérifier que le répertoire existe
    if not os.path.isdir(tiles_dir):
        print(f"Erreur: {tiles_dir} n'est pas un répertoire valide")
        return None
    
    # Trouver toutes les tuiles dans le répertoire
    tile_files = []
    for root, dirs, files in os.walk(tiles_dir):
        for file in files:
            if file.endswith('.npy'):
                tile_files.append(os.path.join(root, file))
    
    if not tile_files:
        print(f"Aucune tuile trouvée dans {tiles_dir}")
        return None
    
    print(f"Analyse de {len(tile_files)} tuiles...")
    
    # Analyser chaque tuile
    ia_scores = []
    success_count = 0
    
    for tile_file in tqdm(tile_files, desc="Analyse des tuiles"):
        try:
            # Charger et prétraiter la tuile
            tile = np.load(tile_file)
            tile = preprocess_matrix(tile)
            
            # Conversion en tenseur
            tile_tensor = torch.tensor(tile, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
            tile_tensor = tile_tensor.to(device)
            
            # Prédiction
            with torch.no_grad():
                output = model(tile_tensor).squeeze().item()
            
            # Ajouter le score à la liste
            ia_scores.append(output)
            success_count += 1
            
        except Exception as e:
            print(f"Erreur lors de l'analyse de la tuile {tile_file}: {e}")
            traceback.print_exc()
    
    if success_count == 0:
        print("Aucune tuile n'a pu être analysée correctement")
        return None
    
    # Calculer le score moyen et la classe prédite
    avg_score = sum(ia_scores) / len(ia_scores)
    predicted_class = "IA" if avg_score > 0.5 else "Humain"
    confidence = avg_score if avg_score > 0.5 else 1 - avg_score
    
    # Récupérer le nom de base du répertoire de tuiles
    directory_path = os.path.dirname(tiles_dir)
    base_name = os.path.basename(directory_path)
    if not base_name or base_name == "temp_matrices":
        # Utiliser le nom du répertoire tiles lui-même
        base_name = os.path.basename(tiles_dir)
    
    # Déterminer la classe réelle
    true_class = determine_true_class(base_name)
    
    # Créer le résultat
    result = {
        'file': base_name,
        'true_class': true_class,
        'predicted_class': predicted_class,
        'score': avg_score,
        'confidence': confidence,
        'tile_scores': ia_scores,
        'tiles_analyzed': success_count,
        'total_tiles': len(tile_files),
        'correct': predicted_class == true_class if true_class != "Inconnu" else None
    }
    
    # Afficher le résultat
    print("\n" + "="*60)
    print(f"Résultat global pour: {base_name}")
    print("-"*60)
    print(f"Classe réelle: {true_class}")
    print(f"Prédiction: {predicted_class}")
    print(f"Score moyen: {avg_score:.4f}")
    print(f"Confiance: {confidence*100:.2f}%")
    print(f"Tuiles analysées: {success_count}/{len(tile_files)}")
    if true_class != "Inconnu":
        print(f"Correct: {'✓' if predicted_class == true_class else '✗'}")
    print("="*60)
    
    return result

def analyze_python_file(model_path, python_file, device=None):
    """
    Analyse un fichier Python pour déterminer s'il est généré par IA
    
    Args:
        model_path: Chemin vers le modèle UNet entraîné
        python_file: Chemin vers le fichier Python à analyser
        device: Périphérique de calcul (None pour auto-détection)
    
    Returns:
        Dictionnaire contenant les résultats d'analyse
    """
    # Déterminer le device
    if device is None:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    print(f"Utilisation de: {device}")
    
    # Vérifier que le modèle existe
    if not os.path.exists(model_path):
        print(f"Erreur: Le fichier modèle '{model_path}' n'existe pas!")
        return None
    
    # Charger le modèle
    try:
        model = UNetForCodeDetection()
        model.load_state_dict(torch.load(model_path, map_location=device))
        model.to(device)
        model.eval()
        print(f"Modèle chargé avec succès: {model_path}")
    except Exception as e:
        print(f"Erreur lors du chargement du modèle: {e}")
        return None
    
    # Si le fichier est déjà une matrice .npy, l'utiliser directement
    if python_file.endswith('.npy'):
        matrix_file = python_file
    else:
        # Convertir le fichier Python en matrice
        temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp_matrices")
        matrix_file = generate_matrix_and_tiles_from_python(python_file, temp_dir)
    
    if matrix_file:
        # Vérifier si le chemin est un répertoire ou un fichier
        if os.path.isdir(matrix_file):
            # Si c'est un répertoire (contenant des tuiles), utiliser analyze_tiles_directory
            result = analyze_tiles_directory(model, matrix_file, device)
        else:
            # Si c'est un fichier unique, utiliser test_single_file
            result = test_single_file(model, matrix_file, device)
        
        # Ajouter le nom du fichier Python d'origine si c'est un .py
        if python_file.endswith('.py') and result:
            result['python_file'] = python_file
        
        return result
    else:
        return None

def analyze_python_directory(model_path, directory, recursive=False, device=None):
    """
    Analyse tous les fichiers Python et NPY dans un répertoire
    
    Args:
        model_path: Chemin vers le modèle UNet entraîné
        directory: Répertoire contenant les fichiers Python
        recursive: Si True, recherche également dans les sous-dossiers
        device: Périphérique de calcul (None pour auto-détection)
    
    Returns:
        Liste de dictionnaires contenant les résultats d'analyse
    """
    # Déterminer le device
    if device is None:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    print(f"Utilisation de: {device}")
    
    # Vérifier que le modèle existe
    if not os.path.exists(model_path):
        print(f"Erreur: Le fichier modèle '{model_path}' n'existe pas!")
        return []
    
    # Charger le modèle
    try:
        model = UNetForCodeDetection()
        model.load_state_dict(torch.load(model_path, map_location=device))
        model.to(device)
        model.eval()
        print(f"Modèle chargé avec succès: {model_path}")
    except Exception as e:
        print(f"Erreur lors du chargement du modèle: {e}")
        return []
    
    # Trouver tous les fichiers Python et NPY dans le répertoire
    py_files = []
    npy_files = []
    
    if recursive:
        py_files = glob.glob(os.path.join(directory, "**/*.py"), recursive=True)
        npy_files = glob.glob(os.path.join(directory, "**/*.npy"), recursive=True)
    else:
        py_files = glob.glob(os.path.join(directory, "*.py"))
        npy_files = glob.glob(os.path.join(directory, "*.npy"))
    
    print(f"Trouvé {len(py_files)} fichiers Python et {len(npy_files)} fichiers NPY dans {directory}")
    
    if len(py_files) == 0 and len(npy_files) == 0:
        print("Aucun fichier Python ou NPY trouvé dans le répertoire spécifié!")
        return []
    
    # Créer un répertoire temporaire pour les matrices générées à partir des fichiers Python
    temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp_matrices")
    os.makedirs(temp_dir, exist_ok=True)
    
    # Traiter d'abord les fichiers .npy qui sont déjà des matrices
    results = []
    if npy_files:
        print("Analyse des matrices .npy existantes...")
        for npy_file in tqdm(npy_files, desc="Analyse des matrices existantes"):
            result = test_single_file(model, npy_file, device)
            if result:
                results.append(result)
    
    # Générer les matrices pour les fichiers Python et les analyser
    if py_files:
        print("Génération des matrices à partir des fichiers Python...")
        for py_file in tqdm(py_files, desc="Génération et analyse des fichiers Python"):
            # Note: Ici nous utilisons generate_matrix_and_tiles_from_python, pas generate_matrix_from_python
            matrix_file = generate_matrix_and_tiles_from_python(py_file, temp_dir)
            if matrix_file:
                # Vérifier si le chemin est un répertoire ou un fichier
                if os.path.isdir(matrix_file):
                    result = analyze_tiles_directory(model, matrix_file, device)
                else:
                    result = test_single_file(model, matrix_file, device)
                
                if result:
                    result['python_file'] = py_file
                    results.append(result)
    
    # Afficher les statistiques globales
    correct_count = sum(1 for r in results if r.get('correct') == True)
    total_known = sum(1 for r in results if r.get('correct') is not None)
    
    print("\n" + "="*60)
    print("RÉSULTATS GLOBAUX")
    print("-"*60)
    
    print(f"Total des fichiers analysés: {len(results)}")
    
    if total_known > 0:
        accuracy = correct_count / total_known
        print(f"Précision globale: {accuracy*100:.2f}% ({correct_count}/{total_known})")
        
        # Statistiques par classe
        ia_total = sum(1 for r in results if r.get('true_class') == "IA")
        ia_correct = sum(1 for r in results if r.get('true_class') == "IA" and r.get('correct'))
        
        human_total = sum(1 for r in results if r.get('true_class') == "Humain")
        human_correct = sum(1 for r in results if r.get('true_class') == "Humain" and r.get('correct'))
        
        if ia_total > 0:
            print(f"Précision sur code IA: {(ia_correct/ia_total)*100:.2f}% ({ia_correct}/{ia_total})")
        
        if human_total > 0:
            print(f"Précision sur code Humain: {(human_correct/human_total)*100:.2f}% ({human_correct}/{human_total})")
    else:
        print("Aucun fichier avec une classe connue n'a été testé.")
    
    print("="*60)
    
    return results

def main():
    # Configurer les arguments en ligne de commande
    parser = argparse.ArgumentParser(description='Test du modèle UNet sur des fichiers Python')
    parser.add_argument('--model', required=True, help='Chemin vers le modèle UNet')
    parser.add_argument('--input', required=True, help='Chemin vers le fichier ou dossier à analyser')
    parser.add_argument('--recursive', action='store_true', help='Rechercher récursivement dans les sous-dossiers')
    parser.add_argument('--device', default='auto', help='Device à utiliser (auto, cuda, cpu)')
    parser.add_argument('--token-model', default='gpt-4o-mini', help='Modèle de tokenisation à utiliser')
    parser.add_argument('--pred-model', default='gpt-4o-mini', help='Modèle de prédiction à utiliser')
    parser.add_argument('--visualize-tiles', action='store_true', help='Visualiser les tuiles générées')
    parser.add_argument('--visualize-activations', action='store_true', help='Visualiser les activations du modèle')
    parser.add_argument('--viz-output', help='Dossier de sortie pour les visualisations')
    
    args = parser.parse_args()
    
    # Déterminer le device
    if args.device == 'auto':
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    else:
        device = torch.device(args.device)
    
    print(f"Utilisation du device: {device}")
    
    # Charger le modèle
    model = UNetForCodeDetection()
    model.load_state_dict(torch.load(args.model, map_location=device))
    model.to(device)
    model.eval()
    
    # Créer le dossier de sortie pour les visualisations si nécessaire
    if args.viz_output:
        os.makedirs(args.viz_output, exist_ok=True)
    
    # Analyser le fichier ou le dossier
    if os.path.isfile(args.input):
        if args.input.endswith('.py'):
            # Analyser un fichier Python
            results = analyze_python_file(args.model, args.input, device)
            
            # Générer les visualisations si demandé
            if args.visualize_tiles or args.visualize_activations:
                # Créer un dossier temporaire pour les tuiles
                temp_dir = os.path.join(os.path.dirname(args.input), 'temp_tiles')
                os.makedirs(temp_dir, exist_ok=True)
                
                # Générer les tuiles
                matrix, tiles = generate_matrix_and_tiles_from_python(
                    args.input, 
                    output_dir=temp_dir,
                    token_model=args.token_model,
                    pred_model=args.pred_model
                )
                
                # Visualiser les tuiles
                if args.visualize_tiles:
                    output_dir = args.viz_output or os.path.dirname(args.input)
                    cmd = ['python', 'visualization/visualize_tilespy.py', 
                          '--dossier_tuiles', temp_dir]
                    if output_dir:
                        cmd.extend(['--dossier_sortie', output_dir])
                    subprocess.run(cmd, check=True)
                
                # Visualiser les activations
                if args.visualize_activations:
                    output_dir = args.viz_output or os.path.join(os.path.dirname(args.input), 'activations')
                    cmd = ['python', 'visualization/visualize_activation.py',
                          '--model', args.model,
                          '--input', temp_dir,
                          '--output', output_dir]
                    if args.device != 'auto':
                        cmd.extend(['--device', args.device])
                    subprocess.run(cmd, check=True)
                
                # Nettoyer le dossier temporaire
                import shutil
                shutil.rmtree(temp_dir)
                
        else:
            # Analyser une matrice ou un dossier de tuiles
            results = test_single_file(model, args.input, device)
    else:
        # Analyser un dossier
        if args.recursive:
            results = analyze_python_directory(args.model, args.input, recursive=True, device=device)
        else:
            results = analyze_python_directory(args.model, args.input, device=device)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())