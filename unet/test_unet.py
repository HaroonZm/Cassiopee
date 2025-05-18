import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import os
import glob
import argparse
from tqdm import tqdm

# Architecture UNet modifiée pour la détection de code IA
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

def test_directory(model, test_dir, device):
    """
    Teste le modèle sur tous les fichiers .npy d'un répertoire
    """
    # Trouver tous les fichiers .npy dans le répertoire
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

def main():
    # Configurer les arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Test d'un modèle UNet pour la détection de code généré par IA")
    parser.add_argument('--model', type=str, default='best_unet_tile_detector.pth', help='Chemin vers le fichier du modèle (.pth)')
    parser.add_argument('--input', type=str, required=True, help='Chemin vers un fichier .npy ou un répertoire contenant des fichiers .npy')
    parser.add_argument('--device', type=str, default='', help='Device à utiliser (cuda/cpu, vide pour auto-détection)')
    
    args = parser.parse_args()
    
    # Déterminer le device
    if args.device:
        device = torch.device(args.device)
    else:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    print(f"Utilisation de: {device}")
    
    # Vérifier que le modèle existe
    if not os.path.exists(args.model):
        print(f"Erreur: Le fichier modèle '{args.model}' n'existe pas!")
        return
    
    # Charger le modèle
    try:
        model = UNetForCodeDetection()
        model.load_state_dict(torch.load(args.model, map_location=device))
        model.to(device)
        model.eval()
        print(f"Modèle chargé avec succès: {args.model}")
    except Exception as e:
        print(f"Erreur lors du chargement du modèle: {e}")
        return
    
    # Tester le modèle
    if os.path.isdir(args.input):
        # C'est un répertoire
        test_directory(model, args.input, device)
    elif os.path.isfile(args.input) and args.input.endswith('.npy'):
        # C'est un fichier unique
        test_single_file(model, args.input, device)
    else:
        print(f"Erreur: '{args.input}' n'est pas un fichier .npy ou un répertoire valide!")

if __name__ == "__main__":
    main()