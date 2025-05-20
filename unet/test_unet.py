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
from tqdm import tqdm

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

def generate_matrix_from_python(py_file, output_dir=None, token_model="gpt-4o-mini", pred_model="gpt-4o-mini"):
    """
    Convertit un fichier Python en représentation matricielle pour l'analyse
    en appelant matrix_generator.py en mode no-batch.
    
    Args:
        py_file: Chemin vers le fichier Python
        output_dir: Répertoire de sortie pour la matrice
        token_model: Modèle à utiliser pour la tokenisation
        pred_model: Modèle à utiliser pour la prédiction
    
    Returns:
        Chemin vers le fichier .npy contenant la matrice générée
    """
    import subprocess
    import tempfile
    import time
    
    try:
        # Créer un répertoire temporaire si aucun n'est spécifié
        if not output_dir:
            output_dir = tempfile.mkdtemp(prefix="matrix_temp_")
        else:
            os.makedirs(output_dir, exist_ok=True)
        
        # Nom du fichier de sortie
        base_name = os.path.basename(py_file).replace('.py', '')
        matrix_file = os.path.join(output_dir, f"{base_name}.npy")
        
        # Construire la commande pour appeler matrix_generator.py en mode no-batch
        cmd = [
            "python", 
            "matrix_generation/matrix_generator.py",
            "--file", py_file,
            "--no-batch",
            "--token-model", token_model,
            "--pred-model", pred_model,
            "--output-dir", output_dir
        ]
        
        print(f"Exécution de la commande: {' '.join(cmd)}")
        
        # Exécuter la commande
        process = subprocess.Popen(
            cmd,
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
            print(f"Erreur lors de la génération de la matrice, code de sortie: {exit_code}")
            return None
        
        # Vérifier si le fichier a été généré
        if os.path.exists(matrix_file):
            print(f"Matrice générée avec succès: {matrix_file}")
            return matrix_file
        else:
            # Si le fichier spécifique n'existe pas, chercher des fichiers .npy dans le répertoire
            npy_files = glob.glob(os.path.join(output_dir, "*.npy"))
            if npy_files:
                print(f"Matrice trouvée: {npy_files[0]}")
                return npy_files[0]
            else:
                print(f"Aucune matrice générée dans le répertoire: {output_dir}")
                return None
    
    except Exception as e:
        print(f"Erreur lors de la génération de matrice pour {py_file}: {str(e)}")
        return None

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
        matrix_file = generate_matrix_from_python(python_file, temp_dir)
    
    if matrix_file:
        # Analyser la matrice
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
            matrix_file = generate_matrix_from_python(py_file, temp_dir)
            if matrix_file:
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
    parser = argparse.ArgumentParser(description="Test d'un modèle UNet pour la détection de code généré par IA")
    parser.add_argument('--model', type=str, default='best_unet_tile_detector.pth', 
                        help='Chemin vers le fichier du modèle (.pth)')
    parser.add_argument('--input', type=str, required=True, 
                        help='Chemin vers un fichier Python/NPY ou un répertoire contenant des fichiers')
    parser.add_argument('--recursive', action='store_true', 
                        help='Parcourir récursivement les sous-dossiers')
    parser.add_argument('--device', type=str, default='', 
                        help='Device à utiliser (cuda/cpu, vide pour auto-détection)')
    parser.add_argument('--token-model', type=str, default='gpt-4o-mini',
                        help='Modèle à utiliser pour la tokenisation')
    parser.add_argument('--pred-model', type=str, default='gpt-4o-mini',
                        help='Modèle à utiliser pour la prédiction')
    
    args = parser.parse_args()
    
    # Déterminer le device
    if args.device:
        device = torch.device(args.device)
    else:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # Vérifier que le modèle existe
    if not os.path.exists(args.model):
        print(f"Erreur: Le fichier modèle '{args.model}' n'existe pas!")
        return
    
    # Analyser selon le type d'entrée
    if os.path.isfile(args.input):
        if args.input.endswith('.py') or args.input.endswith('.npy'):
            # Fichier Python ou NPY
            result = analyze_python_file(args.model, args.input, device)
            
            # Afficher un résumé
            if result:
                print("\nRÉSUMÉ:")
                print(f"Fichier: {args.input}")
                print(f"Prédiction: {result['predicted_class']}")
                print(f"Confiance: {result['confidence']*100:.2f}%")
        else:
            print(f"Erreur: '{args.input}' n'est pas un fichier Python (.py) ou une matrice (.npy)!")
    elif os.path.isdir(args.input):
        # Répertoire de fichiers
        analyze_python_directory(args.model, args.input, args.recursive, device)
    else:
        print(f"Erreur: '{args.input}' n'est pas un fichier ou un répertoire valide!")

if __name__ == "__main__":
    main()