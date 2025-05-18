import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import os
import glob
import argparse
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from collections import defaultdict
from skimage.transform import resize

# Architecture UNet modifiée pour accéder aux activations intermédiaires
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
        
        # Pour stocker les activations pour Grad-CAM
        self.gradients = None
        self.activations = None
        
    def activations_hook(self, grad):
        self.gradients = grad
    
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
        
        # Bottleneck - c'est ici que nous capturons les activations pour Grad-CAM
        e4 = self.enc4(p3)
        
        # Enregistrer les activations
        self.activations = e4
        
        # Enregistrer le gradient si en mode d'entraînement
        if self.training or (not self.training and self.gradients is None):
            h = e4.register_hook(self.activations_hook)
        
        # Decoder avec gestion des dimensions
        d3 = self.upconv3(e4)
        if d3.size() != e3.size():
            d3 = F.interpolate(d3, size=e3.size()[2:], mode='bilinear', align_corners=True)
        d3 = torch.cat([d3, e3], dim=1)
        d3 = self.dec3(d3)
        
        d2 = self.upconv2(d3)
        if d2.size() != e2.size():
            d2 = F.interpolate(d2, size=e2.size()[2:], mode='bilinear', align_corners=True)
        d2 = torch.cat([d2, e2], dim=1)
        d2 = self.dec2(d2)
        
        d1 = self.upconv1(d2)
        if d1.size() != e1.size():
            d1 = F.interpolate(d1, size=e1.size()[2:], mode='bilinear', align_corners=True)
        d1 = torch.cat([d1, e1], dim=1)
        d1 = self.dec1(d1)
        
        # Classification
        features = self.final_conv(d1)
        output = self.classifier(features)
        return output
    
    def get_activations_gradient(self):
        return self.gradients
    
    def get_activations(self):
        return self.activations

def preprocess_matrix(matrix, padding_value=100):
    """
    Prétraite une matrice tout en identifiant les zones de padding
    """
    # Créer un masque pour les valeurs de padding
    padding_mask = (matrix == padding_value)
    
    # Remplacer les valeurs -inf ou NaN par une valeur numérique
    matrix = np.nan_to_num(matrix, neginf=-100.0)
    
    # Normalisation min-max pour ramener entre 0 et 1
    # Exclure les valeurs de padding pour la normalisation
    non_padding = ~padding_mask
    if np.any(non_padding):
        min_val = np.min(matrix[non_padding])
        max_val = np.max(matrix[non_padding])
        if max_val > min_val:  # Éviter la division par zéro
            matrix_normalized = np.zeros_like(matrix, dtype=np.float32)
            matrix_normalized[non_padding] = (matrix[non_padding] - min_val) / (max_val - min_val)
            # Les zones de padding restent à 0
        else:
            matrix_normalized = np.zeros_like(matrix, dtype=np.float32)
    else:
        matrix_normalized = np.zeros_like(matrix, dtype=np.float32)
    
    return matrix_normalized, padding_mask

def generate_gradcam(model, input_tensor, padding_mask=None):
    """
    Génère une carte d'activation Grad-CAM pour l'entrée donnée
    """
    # Faire une passe avant avec l'entrée
    model.eval()
    
    # Prédiction
    output = model(input_tensor)
    pred_score = output.squeeze().item()
    
    # Calculer le gradient par rapport à la sortie
    model.zero_grad()
    output.backward()
    
    # Récupérer les gradients et les activations
    gradients = model.get_activations_gradient()
    activations = model.get_activations()
    
    # Calculer les poids des feature maps
    weights = torch.mean(gradients, dim=(2, 3), keepdim=True)
    
    # Créer la carte d'activation pondérée
    activation_map = torch.sum(weights * activations, dim=1).squeeze().detach().cpu().numpy()
    
    # Appliquer ReLU à la carte d'activation
    activation_map = np.maximum(activation_map, 0)
    
    # Normaliser pour la visualisation
    if np.max(activation_map) > 0:
        activation_map = activation_map / np.max(activation_map)
    
    return activation_map, pred_score

def visualize_single_tile(input_matrix, cam_map, pred_score, padding_mask, title, ax1, ax2, ax3):
    """
    Visualise une tuile et sa carte d'activation sur les axes spécifiés
    """
    # Créer une colormap personnalisée pour la carte de chaleur
    colors = [(0, 0, 0.7), (0, 0.7, 0.7), (0, 0.7, 0), (0.7, 0.7, 0), (0.7, 0, 0)]
    custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors, N=100)
    
    # Redimensionner la carte d'activation à la taille de l'entrée
    if cam_map.shape[0] > 0 and cam_map.shape[1] > 0:
        resized_cam = resize(cam_map, input_matrix.shape, order=1, preserve_range=True)
    else:
        resized_cam = np.zeros(input_matrix.shape)
    
    # Masquer les zones de padding dans la carte d'activation
    if padding_mask is not None:
        resized_cam[padding_mask] = 0
    
    # Afficher l'entrée originale (masquée)
    masked_input = np.ma.masked_array(input_matrix, mask=padding_mask)
    im1 = ax1.imshow(masked_input, cmap='viridis')
    ax1.set_title(f"{title}\nMatrice")
    plt.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)
    ax1.axis('off')
    
    # Afficher la carte d'activation
    im2 = ax2.imshow(resized_cam, cmap=custom_cmap)
    ax2.set_title("Carte d'activation")
    plt.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)
    ax2.axis('off')
    
    # Afficher la superposition
    ax3.imshow(masked_input, cmap='gray', alpha=0.7)
    im3 = ax3.imshow(resized_cam, cmap=custom_cmap, alpha=0.5)
    ax3.set_title(f"Superposition (Score: {pred_score:.4f})")
    plt.colorbar(im3, ax=ax3, fraction=0.046, pad=0.04)
    ax3.axis('off')

def find_matrix_tiles(input_path, matrix_id=None):
    """
    Trouve toutes les tuiles d'une matrice source
    
    Args:
        input_path: Chemin vers un fichier tuile ou un dossier
        matrix_id: ID de la matrice source (optionnel)
        
    Returns:
        Liste des chemins de tuiles et ID de la matrice
    """
    if os.path.isfile(input_path):
        # Si c'est un fichier unique, extraire l'ID de la matrice
        filename = os.path.basename(input_path)
        parts = filename.split("tuile_")
        if len(parts) < 2:
            print(f"Format de nom de fichier non reconnu: {filename}")
            return [], None
        
        # La partie avant "tuile_" est l'identifiant de la matrice
        matrix_id = parts[0].rstrip("_")
        
        # Trouver toutes les tuiles de cette matrice
        directory = os.path.dirname(input_path)
        pattern = f"{matrix_id}_tuile_*"
        tile_paths = glob.glob(os.path.join(directory, pattern))
        
        if not tile_paths:
            # Si aucune correspondance, utiliser uniquement le fichier spécifié
            return [input_path], matrix_id
        
        return tile_paths, matrix_id
    
    elif os.path.isdir(input_path):
        if matrix_id is None:
            print("Erreur: ID de matrice requis pour un dossier")
            return [], None
        
        # Chercher toutes les tuiles de cette matrice dans le dossier
        pattern = f"{matrix_id}_tuile_*"
        tile_paths = glob.glob(os.path.join(input_path, pattern))
        
        return tile_paths, matrix_id
    
    else:
        print(f"Chemin invalide: {input_path}")
        return [], None

def sort_tiles_by_position(tile_paths):
    """
    Trie les chemins des tuiles par position (row, col)
    """
    position_dict = {}
    
    for path in tile_paths:
        filename = os.path.basename(path)
        parts = filename.split("tuile_")
        if len(parts) >= 2:
            position_part = parts[1]
            try:
                # Extraire la position de la forme "0_0.npy"
                row_col = position_part.split('.')[0]
                row, col = map(int, row_col.split('_'))
                position_dict[path] = (row, col)
            except:
                position_dict[path] = (999, 999)  # Valeur par défaut élevée
    
    # Trier par row, puis par col
    return sorted(tile_paths, key=lambda p: position_dict.get(p, (999, 999)))

def get_tile_position(tile_path):
    """Extrait la position (row, col) d'une tuile à partir de son nom de fichier"""
    filename = os.path.basename(tile_path)
    parts = filename.split("tuile_")
    if len(parts) < 2:
        return (0, 0)
    
    position_part = parts[1]
    try:
        row_col = position_part.split('.')[0]
        row, col = map(int, row_col.split('_'))
        return (row, col)
    except:
        return (0, 0)

def visualize_matrix_tiles(model, tile_paths, output_dir, device, padding_value=100):
    """
    Visualise les cartes d'activation pour toutes les tuiles d'une matrice
    """
    if not tile_paths:
        print("Aucune tuile à visualiser.")
        return
    
    # Déterminer l'ID de la matrice
    filename = os.path.basename(tile_paths[0])
    parts = filename.split("tuile_")
    matrix_id = parts[0].rstrip("_")
    
    # Trier les tuiles par position
    sorted_tiles = sort_tiles_by_position(tile_paths)
    
    # Déterminer le type de code (IA ou humain)
    if "gen" in matrix_id.lower() or "var" in matrix_id.lower() or "ia" in matrix_id.lower():
        code_type = "IA"
    elif "human" in matrix_id.lower():
        code_type = "Humain"
    else:
        code_type = "Inconnu"
    
    # Collecter les résultats pour chaque tuile
    tile_results = []
    
    print(f"Génération des cartes d'activation pour {len(sorted_tiles)} tuiles...")
    for tile_path in sorted_tiles:
        # Charger et prétraiter la tuile
        matrix = np.load(tile_path)
        matrix_preprocessed, padding_mask = preprocess_matrix(matrix, padding_value)
        
        # Conversion en tenseur
        matrix_tensor = torch.tensor(matrix_preprocessed, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
        matrix_tensor = matrix_tensor.to(device)
        
        # Générer la carte d'activation
        cam_map, pred_score = generate_gradcam(model, matrix_tensor, padding_mask)
        
        # Extraire la position
        position = get_tile_position(tile_path)
        
        # Stocker les résultats
        tile_results.append({
            'path': tile_path,
            'position': position,
            'matrix': matrix_preprocessed,
            'padding_mask': padding_mask,
            'cam_map': cam_map,
            'pred_score': pred_score
        })
    
    # Calculer le score agrégé
    scores = [r['pred_score'] for r in tile_results]
    
    # Plusieurs stratégies d'agrégation
    aggregated_score_mean = np.mean(scores)
    aggregated_score_vote = 1.0 if sum(1 for s in scores if s > 0.5) > len(scores)/2 else 0.0
    
    # Stratégie hybride (adaptée de notre fonction d'agrégation précédente)
    n_tiles = len(scores)
    if n_tiles < 3:
        aggregated_score_hybrid = scores[0]  # Prendre le premier score
    elif n_tiles <= 10:
        aggregated_score_hybrid = aggregated_score_mean
    else:
        # Vote pondéré
        weighted_positive = sum(1 for s in scores if s > 0.5)
        weighted_negative = sum(1 for s in scores if s <= 0.5)
        total_weight = weighted_positive + weighted_negative
        
        if weighted_positive > weighted_negative:
            aggregated_score_hybrid = 0.5 + 0.5 * (weighted_positive / total_weight)
        else:
            aggregated_score_hybrid = 0.5 - 0.5 * (weighted_negative / total_weight)
    
    # Décision finale
    final_prediction = "IA" if aggregated_score_hybrid > 0.5 else "Humain"
    
    # Créer un titre pour la visualisation
    correct_prediction = final_prediction == code_type
    title = f"Matrice: {matrix_id} - Type: {code_type} - Prédiction: {final_prediction} ({'Correct' if correct_prediction else 'Incorrect'})"
    
    # Déterminer la disposition des sous-graphiques
    n_tiles = len(tile_results)
    cols = min(5, n_tiles)  # Maximum 5 colonnes
    rows = (n_tiles + cols - 1) // cols * 3  # 3 lignes par tuile (matrice, cam, superposition)
    
    # Créer la figure
    plt.figure(figsize=(20, max(15, rows * 3)))
    plt.suptitle(title, fontsize=16)
    
    # Ajouter un texte avec le score agrégé
    aggregation_text = (
        f"Scores agrégés:\n"
        f"Moyenne: {aggregated_score_mean:.4f}\n"
        f"Vote: {aggregated_score_vote:.1f}\n"
        f"Hybride: {aggregated_score_hybrid:.4f}"
    )
    plt.figtext(0.02, 0.97, aggregation_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
    
    # Visualiser chaque tuile
    for i, result in enumerate(tile_results):
        # Calculer la position dans la grille
        base_row = (i // cols) * 3
        base_col = i % cols
        
        # Créer les 3 sous-graphiques pour cette tuile
        ax1 = plt.subplot(rows, cols, base_row * cols + base_col + 1)
        ax2 = plt.subplot(rows, cols, (base_row + 1) * cols + base_col + 1)
        ax3 = plt.subplot(rows, cols, (base_row + 2) * cols + base_col + 1)
        
        # Visualiser la tuile
        tile_title = f"Tuile {result['position'][0]}_{result['position'][1]}"
        visualize_single_tile(
            result['matrix'],
            result['cam_map'],
            result['pred_score'],
            result['padding_mask'],
            tile_title,
            ax1, ax2, ax3
        )
    
    # Sauvegarder la figure
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"gradcam_matrix_{matrix_id}.png")
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Ajuster pour le titre
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Visualisation sauvegardée dans: {output_path}")
    plt.close()
    
    return tile_results

def main():
    # Configurer les arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Visualisation des cartes d'activation pour un modèle UNet sur des tuiles")
    parser.add_argument('--model', type=str, required=True, help='Chemin vers le fichier du modèle (.pth)')
    parser.add_argument('--input', type=str, required=True, help='Chemin vers une tuile ou un dossier contenant des tuiles')
    parser.add_argument('--matrix', type=str, default=None, help='ID de la matrice à visualiser (requis si --input est un dossier)')
    parser.add_argument('--output', type=str, default='activation_maps', help='Répertoire de sortie pour les visualisations')
    parser.add_argument('--device', type=str, default='', help='Device à utiliser (cuda/cpu, vide pour auto-détection)')
    parser.add_argument('--padding', type=float, default=100, help='Valeur utilisée pour le padding (par défaut: 100)')
    
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
    
    # Trouver les tuiles à visualiser
    tile_paths, matrix_id = find_matrix_tiles(args.input, args.matrix)
    
    if not tile_paths:
        print(f"Aucune tuile trouvée pour la matrice '{args.matrix if args.matrix else 'spécifiée'}'")
        return
    
    print(f"Trouvé {len(tile_paths)} tuiles pour la matrice {matrix_id}")
    
    # Visualiser les tuiles
    visualize_matrix_tiles(model, tile_paths, args.output, device, args.padding)

if __name__ == "__main__":
    main()