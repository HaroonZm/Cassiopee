import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import os
import argparse
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

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

def generate_gradcam(model, input_tensor, padding_mask=None, target_class=None):
    """
    Génère une carte d'activation Grad-CAM pour l'entrée donnée
    
    Args:
        model: Le modèle UNet
        input_tensor: Tensor d'entrée au format (1, 1, H, W)
        padding_mask: Masque indiquant les zones de padding (True = padding)
        target_class: Classe cible (0 pour humain, 1 pour IA)
    
    Returns:
        Carte d'activation Grad-CAM et prédiction du modèle
    """
    # Faire une passe avant avec l'entrée
    model.eval()
    
    # Prédiction
    output = model(input_tensor)
    pred_score = output.squeeze().item()
    pred_class = 1 if pred_score > 0.5 else 0
    
    # Si aucune classe cible n'est spécifiée, utiliser la classe prédite
    if target_class is None:
        target_class = pred_class
    
    # Calculer le gradient par rapport à la classe cible
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

def visualize_gradcam(input_matrix, cam_map, pred_score, padding_mask, filename, output_dir='activation_maps'):
    """
    Visualise l'entrée et sa carte d'activation Grad-CAM avec une meilleure gestion du padding
    """
    # Créer le répertoire de sortie si nécessaire
    os.makedirs(output_dir, exist_ok=True)
    
    # Créer une colormap personnalisée pour la carte de chaleur
    colors = [(0, 0, 0.7), (0, 0.7, 0.7), (0, 0.7, 0), (0.7, 0.7, 0), (0.7, 0, 0)]
    cmap_name = 'custom_cmap'
    custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=100)
    
    # Redimensionner la carte d'activation à la taille de l'entrée
    from skimage.transform import resize
    if cam_map.shape[0] > 0 and cam_map.shape[1] > 0:
        resized_cam = resize(cam_map, input_matrix.shape, order=1, preserve_range=True)
    else:
        resized_cam = np.zeros(input_matrix.shape)
    
    # Masquer les zones de padding dans la carte d'activation
    if padding_mask is not None:
        resized_cam[padding_mask] = 0
    
    # Configuration de la figure - avec analyses supplémentaires
    plt.figure(figsize=(20, 15))
    
    # Afficher l'entrée originale (masquée)
    plt.subplot(2, 3, 1)
    plt.title("Matrice d'origine (sans padding)")
    masked_input = np.ma.masked_array(input_matrix, mask=padding_mask)
    plt.imshow(masked_input, cmap='viridis')
    plt.colorbar(label='Valeur normalisée')
    plt.axis('off')
    
    # Afficher la carte d'activation
    plt.subplot(2, 3, 2)
    plt.title("Carte d'activation Grad-CAM")
    plt.imshow(resized_cam, cmap=custom_cmap)
    plt.colorbar(label='Importance pour la classification')
    plt.axis('off')
    
    # Afficher la superposition (masquée)
    plt.subplot(2, 3, 3)
    plt.title(f"Superposition (Prédiction: {'IA' if pred_score > 0.5 else 'Humain'}, Score: {pred_score:.4f})")
    plt.imshow(masked_input, cmap='gray', alpha=0.7)
    plt.imshow(resized_cam, cmap=custom_cmap, alpha=0.5)
    plt.colorbar(label='Importance')
    plt.axis('off')
    
    # Histogramme des valeurs de la matrice (sans padding)
    plt.subplot(2, 3, 4)
    plt.title("Distribution des valeurs (sans padding)")
    if np.any(~padding_mask):
        sns.histplot(input_matrix[~padding_mask].flatten(), bins=50, kde=True)
    else:
        plt.text(0.5, 0.5, "Pas de données hors padding", ha='center', va='center')
    plt.xlabel("Valeur")
    plt.ylabel("Fréquence")
    
    # Carte de chaleur des valeurs d'activation
    plt.subplot(2, 3, 5)
    plt.title("Carte d'activation (seuillée)")
    # Appliquer un seuil pour mieux visualiser les zones importantes
    threshold_cam = np.copy(resized_cam)
    threshold = np.percentile(threshold_cam[threshold_cam > 0], 50) if np.any(threshold_cam > 0) else 0
    threshold_cam[threshold_cam < threshold] = 0
    plt.imshow(threshold_cam, cmap=custom_cmap)
    plt.colorbar(label='Importance (seuillée)')
    plt.axis('off')
    
    # Statistiques et informations
    plt.subplot(2, 3, 6)
    plt.title("Statistiques")
    plt.axis('off')
    
    padding_percentage = np.sum(padding_mask) / padding_mask.size * 100
    
    stats_text = (
        f"Taille de la matrice: {input_matrix.shape}\n"
        f"Pourcentage de padding: {padding_percentage:.2f}%\n"
        f"Moyenne (hors padding): {np.mean(input_matrix[~padding_mask]):.4f}\n"
        f"Écart-type (hors padding): {np.std(input_matrix[~padding_mask]):.4f}\n"
        f"Min (hors padding): {np.min(input_matrix[~padding_mask]):.4f}\n"
        f"Max (hors padding): {np.max(input_matrix[~padding_mask]):.4f}\n\n"
        f"Prédiction: {'IA' if pred_score > 0.5 else 'Humain'}\n"
        f"Score de confiance: {(pred_score if pred_score > 0.5 else 1-pred_score)*100:.2f}%\n\n"
        f"Note: Avec seulement 10 exemples d'entraînement,\n"
        f"le modèle n'a probablement pas convergé correctement.\n"
        f"Les résultats doivent être interprétés avec prudence."
    )
    plt.text(0.1, 0.9, stats_text, va='top', ha='left', fontsize=10)
    
    # Sauvegarder la figure
    output_path = os.path.join(output_dir, f"gradcam_detailed_{os.path.basename(filename).split('.')[0]}.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Visualisation détaillée sauvegardée dans: {output_path}")
    plt.close()

def main():
    # [Configuration des arguments reste la même]
    parser = argparse.ArgumentParser(description="Visualisation des cartes d'activation pour un modèle UNet")
    parser.add_argument('--model', type=str, required=True, help='Chemin vers le fichier du modèle (.pth)')
    parser.add_argument('--input', type=str, required=True, help='Chemin vers un fichier .npy')
    parser.add_argument('--output', type=str, default='activation_maps', help='Répertoire de sortie pour les visualisations')
    parser.add_argument('--device', type=str, default='', help='Device à utiliser (cuda/cpu, vide pour auto-détection)')
    parser.add_argument('--padding', type=float, default=100, help='Valeur utilisée pour le padding (par défaut: 100)')
    
    args = parser.parse_args()
    
    # [Chargement du modèle reste le même]
    if args.device:
        device = torch.device(args.device)
    else:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    print(f"Utilisation de: {device}")
    
    if not os.path.exists(args.model):
        print(f"Erreur: Le fichier modèle '{args.model}' n'existe pas!")
        return
    
    if not os.path.exists(args.input) or not args.input.endswith('.npy'):
        print(f"Erreur: '{args.input}' n'est pas un fichier .npy valide!")
        return
    
    try:
        model = UNetForCodeDetection()
        model.load_state_dict(torch.load(args.model, map_location=device))
        model.to(device)
        model.eval()
        print(f"Modèle chargé avec succès: {args.model}")
    except Exception as e:
        print(f"Erreur lors du chargement du modèle: {e}")
        return
    
    # Charger et prétraiter la matrice avec gestion du masque de padding
    try:
        matrix = np.load(args.input)
        matrix_orig = matrix.copy()
        
        # Prétraiter la matrice et obtenir le masque de padding
        matrix_preprocessed, padding_mask = preprocess_matrix(matrix, padding_value=args.padding)
        
        # Conversion en tenseur
        matrix_tensor = torch.tensor(matrix_preprocessed, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
        matrix_tensor = matrix_tensor.to(device)
        
        print(f"Matrice chargée avec succès: {args.input}")
        print(f"Dimensions: {matrix.shape}")
        print(f"Pourcentage de padding: {np.sum(padding_mask) / padding_mask.size * 100:.2f}%")
        
        # Générer la carte d'activation Grad-CAM
        print("Génération de la carte d'activation Grad-CAM...")
        cam_map, pred_score = generate_gradcam(model, matrix_tensor, padding_mask)
        
        # Visualiser et sauvegarder la carte d'activation
        print("Création de la visualisation...")
        visualize_gradcam(matrix_preprocessed, cam_map, pred_score, padding_mask, 
                          os.path.basename(args.input), args.output)
        
    except Exception as e:
        print(f"Erreur lors de la génération de la carte d'activation: {e}")
        import traceback
        traceback.print_exc()
        return

if __name__ == "__main__":
    main()