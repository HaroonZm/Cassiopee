import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import os
import glob
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from collections import defaultdict

# Dataset pour les tuiles pré-découpées avec identification simplifiée des matrices sources
class PreTiledCodeMatrixDataset(Dataset):
    def __init__(self, tile_paths, group_by_matrix=True):
        self.tile_paths = tile_paths
        
        # Extraire les métadonnées des noms de fichiers
        self.tile_info = []
        self.matrix_to_tiles = defaultdict(list)
        
        print("Chargement des métadonnées des tuiles...")
        for i, path in enumerate(tqdm(tile_paths)):
            filename = os.path.basename(path)
            
            # Identifier la matrice source en prenant tout ce qui est avant "tuile_"
            parts = filename.split("tuile_")
            if len(parts) < 2:
                print(f"Format de nom de fichier non reconnu (pas de 'tuile_'): {filename}")
                continue
            
            # La partie avant "tuile_" est l'identifiant de la matrice
            matrix_id = parts[0].rstrip("_")  # Enlever le dernier underscore
            
            # Déterminer l'étiquette à partir du nom de la matrice
            if "gen" in matrix_id.lower() or "var" in matrix_id.lower() or "ia" in matrix_id.lower():
                label = 1.0  # Code généré par IA
            elif "human" in matrix_id.lower():
                label = 0.0  # Code écrit par humain
            else:
                print(f"Type de code non reconnu pour {filename}, ignoré")
                continue
            
            # Déterminer la position de la tuile (utile pour la visualisation)
            position_part = parts[1]  # Devrait être quelque chose comme "0_0.npy"
            try:
                row, col = map(int, position_part.split('.')[0].split('_'))
            except:
                # Si le format n'est pas comme attendu, utiliser des valeurs par défaut
                row, col = 0, 0
            
            # Stocker les informations
            tile_idx = len(self.tile_info)
            self.tile_info.append({
                'path': path,
                'matrix_id': matrix_id,
                'label': label,
                'row': row,
                'col': col
            })
            
            # Associer cette tuile à sa matrice source
            self.matrix_to_tiles[matrix_id].append(tile_idx)
        
        # Si on veut grouper par matrice, créer une structure pour ça
        if group_by_matrix:
            # Créer un index des matrices uniques
            self.unique_matrices = list(self.matrix_to_tiles.keys())
            print(f"Trouvé {len(self.unique_matrices)} matrices sources uniques avec un total de {len(self.tile_info)} tuiles")
        else:
            print(f"Chargé {len(self.tile_info)} tuiles individuelles")
    
    def __len__(self):
        return len(self.tile_info)
    
    def __getitem__(self, idx):
        # Charger les informations de la tuile
        info = self.tile_info[idx]
        
        # Charger la matrice de la tuile
        tile = np.load(info['path'])
        
        # Prétraiter la tuile (normalisation)
        tile = np.nan_to_num(tile, neginf=-100.0)
        min_val = np.min(tile)
        max_val = np.max(tile)
        if max_val > min_val:  # Éviter la division par zéro
            tile = (tile - min_val) / (max_val - min_val)
        
        # Créer un identifiant numérique pour la matrice source
        matrix_id = self.unique_matrices.index(info['matrix_id']) if hasattr(self, 'unique_matrices') else -1
        
        # Conversion en tenseurs
        tile_tensor = torch.tensor(tile, dtype=torch.float32).unsqueeze(0)
        label_tensor = torch.tensor(info['label'], dtype=torch.float32)
        matrix_id_tensor = torch.tensor(matrix_id, dtype=torch.long)
        
        # Calculer le ratio de contenu non-padding (si nécessaire)
        # Supposons que 100 est la valeur de padding
        padding_value = 100
        content_ratio = np.mean(tile != padding_value) if np.any(tile == padding_value) else 1.0
        content_ratio_tensor = torch.tensor(content_ratio, dtype=torch.float32)
        
        return tile_tensor, label_tensor, matrix_id_tensor, content_ratio_tensor

# Fonction d'agrégation des prédictions de tuiles
def aggregate_tile_predictions(predictions, matrix_indices, content_ratios=None, strategy='hybrid'):
    """
    Agrège les prédictions des tuiles par matrice.
    
    Args:
        predictions: Tensor de prédictions [n_tiles]
        matrix_indices: Tensor d'indices de matrices [n_tiles]
        content_ratios: Tensor de ratios de contenu par tuile [n_tiles]
        strategy: Stratégie d'agrégation ('mean', 'vote', 'weighted', 'hybrid')
        
    Returns:
        Dictionnaire {matrix_idx: prediction_aggregée}
    """
    # Convertir en numpy pour faciliter le traitement
    predictions = predictions.cpu().numpy()
    matrix_indices = matrix_indices.cpu().numpy()
    if content_ratios is not None:
        content_ratios = content_ratios.cpu().numpy()
    
    # Regrouper par matrice
    matrix_to_preds = defaultdict(list)
    matrix_to_ratios = defaultdict(list)
    
    for i, matrix_idx in enumerate(matrix_indices):
        matrix_to_preds[matrix_idx].append(predictions[i])
        if content_ratios is not None:
            matrix_to_ratios[matrix_idx].append(content_ratios[i])
    
    # Agréger selon la stratégie choisie
    results = {}
    
    for matrix_idx, preds in matrix_to_preds.items():
        if strategy == 'mean':
            # Moyenne simple
            results[matrix_idx] = np.mean(preds)
        
        elif strategy == 'vote':
            # Vote majoritaire
            votes_positive = sum(1 for p in preds if p > 0.5)
            results[matrix_idx] = 1.0 if votes_positive > len(preds)/2 else 0.0
        
        elif strategy == 'weighted' and content_ratios is not None:
            # Moyenne pondérée par le contenu
            ratios = matrix_to_ratios[matrix_idx]
            total_ratio = sum(ratios)
            if total_ratio > 0:
                weights = [r / total_ratio for r in ratios]
                results[matrix_idx] = sum(p * w for p, w in zip(preds, weights))
            else:
                results[matrix_idx] = np.mean(preds)
        
        elif strategy == 'hybrid':
            # Stratégie hybride adaptative
            n_tiles = len(preds)
            ratios = matrix_to_ratios[matrix_idx] if content_ratios is not None else [1.0] * n_tiles
            
            if n_tiles < 3:
                # Pour peu de tuiles, utiliser la tuile la plus significative
                idx_max_ratio = np.argmax(ratios)
                results[matrix_idx] = preds[idx_max_ratio]
            
            elif n_tiles <= 10:
                # Pour un nombre moyen de tuiles, utiliser une moyenne pondérée
                total_ratio = sum(ratios)
                if total_ratio > 0:
                    weights = [r / total_ratio for r in ratios]
                    results[matrix_idx] = sum(p * w for p, w in zip(preds, weights))
                else:
                    results[matrix_idx] = np.mean(preds)
            
            else:
                # Pour beaucoup de tuiles, utiliser un vote pondéré
                weighted_positive = sum(ratios[i] for i in range(n_tiles) if preds[i] > 0.5)
                weighted_negative = sum(ratios[i] for i in range(n_tiles) if preds[i] <= 0.5)
                total_weight = weighted_positive + weighted_negative
                
                if weighted_positive > weighted_negative:
                    # Score entre 0.5 et 1.0 selon la force du vote
                    strength = 0.5 + 0.5 * (weighted_positive / total_weight)
                    results[matrix_idx] = strength
                else:
                    # Score entre 0.0 et 0.5 selon la force du vote
                    strength = 0.5 * (weighted_negative / total_weight)
                    results[matrix_idx] = 0.5 - strength
        
        else:
            # Par défaut, utiliser la moyenne
            results[matrix_idx] = np.mean(preds)
    
    return results

# Fonction d'évaluation pour les tuiles pré-découpées
def evaluate_model(model, val_loader, device):
    """
    Évalue le modèle sur un ensemble de validation avec l'approche par tuiles.
    """
    model.eval()
    all_predictions = []
    all_matrix_indices = []
    all_labels = []
    all_content_ratios = []
    
    with torch.no_grad():
        for inputs, labels, matrix_indices, content_ratios in val_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            matrix_indices = matrix_indices.to(device)
            content_ratios = content_ratios.to(device)
            
            # Prédiction
            outputs = model(inputs).squeeze()
            
            # Si une seule tuile dans le batch
            if outputs.ndim == 0:
                outputs = outputs.unsqueeze(0)
            
            # Collecter les résultats
            all_predictions.append(outputs)
            all_matrix_indices.append(matrix_indices)
            all_labels.append(labels)
            all_content_ratios.append(content_ratios)
    
    # Concaténer tous les résultats
    all_predictions = torch.cat(all_predictions)
    all_matrix_indices = torch.cat(all_matrix_indices)
    all_labels = torch.cat(all_labels)
    all_content_ratios = torch.cat(all_content_ratios)
    
    # Agréger les prédictions par matrice
    aggregated_results = aggregate_tile_predictions(
        all_predictions, 
        all_matrix_indices,
        all_content_ratios, 
        strategy='hybrid'
    )
    
    # Calculer les métriques
    # Pour chaque matrice, nous prenons la première étiquette associée
    # (toutes les tuiles d'une même matrice ont la même étiquette)
    matrix_to_label = {}
    for i, matrix_idx in enumerate(all_matrix_indices.cpu().numpy()):
        if matrix_idx not in matrix_to_label:
            matrix_to_label[matrix_idx] = all_labels[i].item()
    
    correct = 0
    total = 0
    
    for matrix_idx, pred in aggregated_results.items():
        label = matrix_to_label[matrix_idx]
        predicted_class = 1 if pred > 0.5 else 0
        
        if predicted_class == int(label):
            correct += 1
        total += 1
    
    accuracy = correct / total if total > 0 else 0
    
    return accuracy, aggregated_results

# Fonction d'entraînement modifiée
def train_model_with_tiles(model, train_loader, val_loader, criterion, optimizer, num_epochs=10, device='cuda'):
    model.to(device)
    best_val_acc = 0.0
    
    for epoch in range(num_epochs):
        # Mode entraînement
        model.train()
        train_loss = 0.0
        batch_count = 0
        
        for inputs, labels, _, _ in tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs} - Training"):
            inputs, labels = inputs.to(device), labels.to(device)
            
            # Forward pass
            optimizer.zero_grad()
            outputs = model(inputs).squeeze()
            
            # Si une seule tuile dans le batch
            if outputs.ndim == 0:
                outputs = outputs.unsqueeze(0)
                
            # Calculer la perte
            loss = criterion(outputs, labels)
            
            # Backward pass
            loss.backward()
            optimizer.step()
            
            # Statistiques
            train_loss += loss.item()
            batch_count += 1
        
        avg_train_loss = train_loss / batch_count if batch_count > 0 else float('inf')
        
        # Évaluation
        print("Évaluation sur l'ensemble de validation...")
        val_acc, _ = evaluate_model(model, val_loader, device)
        
        print(f"Epoch {epoch+1}/{num_epochs} - "
              f"Train Loss: {avg_train_loss:.4f}, Val Acc: {val_acc:.4f}")
        
        # Sauvegarde du meilleur modèle
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_unet_tile_detector.pth')
            print(f"Model saved with validation accuracy: {val_acc:.4f}")
    
    return model

# Fonction principale modifiée
def main():
    # Paramètres
    data_folder = "tuiled_matrixes"  # Dossier contenant les tuiles pré-découpées
    batch_size = 16
    num_epochs = 20
    learning_rate = 0.001
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    print(f"Utilisation de: {device}")
    
    # Trouver toutes les tuiles
    tile_paths = glob.glob(os.path.join(data_folder, "*.npy"))
    
    if not tile_paths:
        print(f"Aucune tuile trouvée dans {data_folder}")
        return
        
    print(f"Trouvé {len(tile_paths)} tuiles")
    
    # Créer le dataset avec toutes les tuiles
    dataset = PreTiledCodeMatrixDataset(tile_paths)
    
    # Obtenir les indices uniques des matrices
    unique_matrix_indices = list(dataset.matrix_to_tiles.keys())
    
    # Diviser les matrices en ensembles d'entraînement et de validation
    # C'est crucial que cette division se fasse au niveau des matrices, pas des tuiles
    train_matrices, val_matrices = train_test_split(
        unique_matrix_indices, test_size=0.2, random_state=42
    )
    
    # Obtenir les indices des tuiles pour chaque ensemble
    train_tile_indices = []
    for matrix_key in train_matrices:
        train_tile_indices.extend(dataset.matrix_to_tiles[matrix_key])
    
    val_tile_indices = []
    for matrix_key in val_matrices:
        val_tile_indices.extend(dataset.matrix_to_tiles[matrix_key])
    
    # Créer des sous-ensembles pour l'entraînement et la validation
    from torch.utils.data import Subset
    train_dataset = Subset(dataset, train_tile_indices)
    val_dataset = Subset(dataset, val_tile_indices)
    
    print(f"Tuiles d'entraînement: {len(train_dataset)}")
    print(f"Tuiles de validation: {len(val_dataset)}")
    
    # Création des dataloaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)
    
    # Initialisation du modèle
    model = UNetForCodeDetection()
    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
    # Entraînement du modèle
    print(f"Début de l'entraînement...")
    model = train_model_with_tiles(model, train_loader, val_loader, criterion, optimizer, num_epochs, device)
    
    print("Entraînement terminé!")

# Conserver votre architecture UNet originale
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

if __name__ == "__main__":
    main()