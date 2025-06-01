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
import argparse  # Ajouté pour gérer les arguments en ligne de commande
import json  # Pour sauvegarder les métadonnées d'entraînement
import datetime  # Pour générer des noms de fichiers uniques

# Dataset pour les tuiles pré-découpées avec identification simplifiée des matrices sources
class PreTiledCodeMatrixDataset(Dataset):
    def __init__(self, tile_paths, group_by_matrix=True, default_label=None):
        self.tile_paths = tile_paths
        self.default_label = default_label
        
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
            if self.default_label is not None:
                # Utiliser l'étiquette par défaut si spécifiée
                label = float(self.default_label)
            # Identifier les codes générés par IA - Chercher aussi "var" et "gen" dans le nom du fichier complet
            elif ("gen" in matrix_id.lower() or "var" in matrix_id.lower() or 
                  "ia" in matrix_id.lower() or "ai" in matrix_id.lower() or 
                  "gen" in filename.lower() or "var" in filename.lower()):
                label = 1.0  # Code généré par IA
            # Identifier les codes humains
            elif "human" in matrix_id.lower() or "original" in matrix_id.lower():
                label = 0.0  # Code écrit par humain
            # Reconnaître les formats spécifiques mat_* 
            elif matrix_id.startswith("mat_"):
                # Analyser le nom après le préfixe mat_
                base_name = matrix_id[4:]  # Enlever "mat_"
                
                # Déterminer le type de code basé sur le nom du fichier original
                if ("gen" in base_name.lower() or "var" in base_name.lower() or 
                    "ia" in base_name.lower() or "ai" in base_name.lower() or
                    "gen" in filename.lower() or "var" in filename.lower()):
                    label = 1.0  # Code généré par IA
                elif ("human" in base_name.lower() or "original" in base_name.lower() or 
                      "codenet" in base_name.lower() and not "ai" in base_name.lower()):
                    label = 0.0  # Code écrit par humain
                else:
                    # Par défaut, considérer comme du code humain
                    label = 0.0
            # Reconnaissance des formats spécifiques à CodeNet
            elif "_s" in matrix_id.lower() and "batch" in matrix_id.lower():
                # Pour les matrices de CodeNet (s = solution), on suppose que c'est un code humain
                label = 0.0  # Code humain (CodeNet)
            else:
                # Par défaut, considérer tous les autres fichiers comme du code humain
                label = 0.0
            
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

# Générer un nom de fichier unique pour le modèle
def generate_model_filename(batch_name, model_type, num_epochs, batch_size, accuracy=None):
    """
    Génère un nom de fichier unique pour le modèle.
    
    Args:
        batch_name: Nom du batch utilisé pour l'entraînement
        model_type: Type de modèle ('best', 'final')
        num_epochs: Nombre d'époques d'entraînement
        batch_size: Taille du batch utilisé
        accuracy: Précision du modèle (optionnel)
    
    Returns:
        Nom de fichier unique
    """
    # Obtenir la date et l'heure actuelles au format YYYYMMDD_HHMMSS
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Nettoyer le nom du batch pour qu'il soit utilisable dans un nom de fichier
    batch_name = os.path.basename(batch_name)
    batch_name = ''.join(c if c.isalnum() else '_' for c in batch_name)
    
    # Construire le nom de fichier
    filename = f"unet_{batch_name}_{model_type}_e{num_epochs}_b{batch_size}"
    
    # Ajouter la précision si disponible
    if accuracy is not None:
        accuracy_str = f"{accuracy:.4f}".replace('.', '')
        filename += f"_acc{accuracy_str}"
    
    # Ajouter le timestamp et l'extension
    filename += f"_{timestamp}.pth"
    
    return filename

# Fonction d'entraînement modifiée
def train_model_with_tiles(model, train_loader, val_loader, criterion, optimizer, 
                          num_epochs=10, device='cuda', model_save_dir='.', 
                          batch_name='default'):
    model.to(device)
    best_val_acc = 0.0
    best_epoch = -1
    best_model_filename = None  # Initialiser à None pour gérer le cas où aucun meilleur modèle n'est trouvé
    
    # Créer le dossier pour sauvegarder si nécessaire
    os.makedirs(model_save_dir, exist_ok=True)
    
    # Préparer le nom de base du modèle
    batch_size = train_loader.batch_size
    
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
            best_epoch = epoch + 1
            
            # Générer un nom de fichier unique pour le meilleur modèle
            best_model_filename = generate_model_filename(
                batch_name, "best", num_epochs, batch_size, val_acc
            )
            best_model_path = os.path.join(model_save_dir, best_model_filename)
            
            torch.save(model.state_dict(), best_model_path)
            print(f"Meilleur modèle sauvegardé avec précision de validation: {val_acc:.4f}")
            print(f"Chemin: {best_model_path}")
    
    # Si aucun meilleur modèle n'a été trouvé (rare, mais possible)
    if best_model_filename is None:
        print("Attention: Aucune amélioration de la précision pendant l'entraînement.")
        # Créer un nom de fichier pour le modèle final qui servira aussi de meilleur modèle
        best_model_filename = generate_model_filename(
            batch_name, "best_final", num_epochs, batch_size, 0.0
        )
        best_model_path = os.path.join(model_save_dir, best_model_filename)
        torch.save(model.state_dict(), best_model_path)
        print(f"Modèle sauvegardé comme meilleur modèle par défaut: {best_model_path}")
    
    return model, best_val_acc, best_epoch, best_model_filename

# Fonction principale modifiée pour accepter les arguments en ligne de commande
def main():
    # Configuration de l'analyse des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Entraînement du modèle de détection de code IA")
    parser.add_argument('--batch_directory', type=str, default="default_batch",
                       help="Dossier contenant les données de batch, les tuiles seront recherchées dans batch_directory/tiles")
    parser.add_argument('--batch_size', type=int, default=16,
                       help="Taille du batch pour l'entraînement")
    parser.add_argument('--num_epochs', type=int, default=20,
                       help="Nombre d'époques d'entraînement")
    parser.add_argument('--learning_rate', type=float, default=0.001,
                       help="Taux d'apprentissage")
    parser.add_argument('--model_save_dir', type=str, default="models",
                       help="Dossier où sauvegarder les modèles")
    parser.add_argument('--default_label', type=float, default=None,
                       help="Étiquette par défaut à utiliser pour toutes les tuiles (0=humain, 1=IA)")
    
    args = parser.parse_args()
    
    # Paramètres
    batch_dir = args.batch_directory
    batch_size = args.batch_size
    num_epochs = args.num_epochs
    learning_rate = args.learning_rate
    model_save_dir = args.model_save_dir
    default_label = args.default_label
    
    # Détection du dispositif
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Utilisation de: {device}")
    
    # Trouver toutes les tuiles dans le dossier de batch
    print(f"Dossier batch: {batch_dir}")
    
    # Chercher d'abord dans le dossier de tuiles s'il existe
    tiles_dir = os.path.join(batch_dir, "tiles")
    if not os.path.exists(tiles_dir):
        # Sinon, utiliser directement le dossier batch
        tiles_dir = batch_dir
    
    print(f"Dossier des tuiles: {tiles_dir}")
    
    # Trouver toutes les tuiles
    tile_paths = glob.glob(os.path.join(tiles_dir, "*tuile_*.npy"))
    print(f"Trouvé {len(tile_paths)} tuiles")
    
    if len(tile_paths) == 0:
        print("Aucune tuile trouvée. Vérifiez le dossier et le format des noms de fichiers.")
        return
    
    # Créer le dataset avec les tuiles pré-découpées
    dataset = PreTiledCodeMatrixDataset(tile_paths, group_by_matrix=True, default_label=default_label)
    
    # S'assurer qu'il y a des tuiles valides
    if len(dataset) == 0:
        print("Aucune tuile valide trouvée. Vérifiez les noms de fichiers ou utilisez --default_label pour spécifier le type de code.")
        return
    
    print(f"Nombre total de tuiles valides après traitement: {len(dataset)}")
    print(f"Nombre de matrices uniques: {len(dataset.unique_matrices)}")
    
    # Division en ensembles d'entraînement et de validation (au niveau des matrices)
    unique_matrix_indices = list(range(len(dataset.unique_matrices)))
    train_matrices, val_matrices = train_test_split(
        unique_matrix_indices, test_size=0.2, random_state=42
    )
    
    print(f"Matrices d'entraînement: {len(train_matrices)}")
    print(f"Matrices de validation: {len(val_matrices)}")
    
    # Obtenir les indices des tuiles pour chaque ensemble
    train_tile_indices = []
    for matrix_key in train_matrices:
        train_tile_indices.extend(dataset.matrix_to_tiles[dataset.unique_matrices[matrix_key]])
    
    val_tile_indices = []
    for matrix_key in val_matrices:
        val_tile_indices.extend(dataset.matrix_to_tiles[dataset.unique_matrices[matrix_key]])
    
    print(f"Indices des tuiles d'entraînement: {len(train_tile_indices)}")
    print(f"Indices des tuiles de validation: {len(val_tile_indices)}")
    
    # Vérifier qu'il y a des échantillons dans les ensembles d'entraînement et de validation
    if len(train_tile_indices) == 0:
        print("ERREUR: Aucune tuile dans l'ensemble d'entraînement. Vérifiez le mapping des matrices aux tuiles.")
        # Afficher quelques exemples pour le débogage
        for i, matrix_id in enumerate(dataset.unique_matrices):
            if i < 5:  # Limiter à 5 exemples
                print(f"Matrice {i}: {matrix_id} -> {len(dataset.matrix_to_tiles[matrix_id])} tuiles")
        return
    
    if len(val_tile_indices) == 0:
        print("ERREUR: Aucune tuile dans l'ensemble de validation. Utilisation de 10% des tuiles d'entraînement comme validation.")
        # Solution de secours: diviser les tuiles d'entraînement
        train_size = int(0.9 * len(train_tile_indices))
        train_tile_indices, val_tile_indices = train_tile_indices[:train_size], train_tile_indices[train_size:]
    
    # Créer des sous-ensembles pour l'entraînement et la validation
    from torch.utils.data import Subset
    train_dataset = Subset(dataset, train_tile_indices)
    val_dataset = Subset(dataset, val_tile_indices)
    
    print(f"Tuiles d'entraînement: {len(train_dataset)}")
    print(f"Tuiles de validation: {len(val_dataset)}")
    
    # Vérification finale avant de créer les dataloaders
    if len(train_dataset) == 0 or len(val_dataset) == 0:
        print("ERREUR CRITIQUE: Dataset vide après subdivision. Impossible de continuer l'entraînement.")
        return
    
    # Création des dataloaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)
    
    # Initialisation du modèle
    model = UNetForCodeDetection()
    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
    # Entraînement du modèle
    print(f"Début de l'entraînement...")
    model, best_val_acc, best_epoch, best_model_filename = train_model_with_tiles(
        model, train_loader, val_loader, criterion, optimizer, 
        num_epochs, device, model_save_dir, batch_dir
    )
    
    # Sauvegarder le modèle final
    final_model_filename = generate_model_filename(
        batch_dir, "final", num_epochs, batch_size
    )
    final_model_path = os.path.join(model_save_dir, final_model_filename)
    torch.save(model.state_dict(), final_model_path)
    print(f"Modèle final sauvegardé à: {final_model_path}")
    
    # Évaluer le modèle final
    final_val_acc, _ = evaluate_model(model, val_loader, device)
    
    # Sauvegarder les métadonnées d'entraînement
    metadata = {
        'batch_directory': batch_dir,
        'num_epochs': num_epochs,
        'batch_size': batch_size,
        'learning_rate': learning_rate,
        'best_validation_accuracy': float(best_val_acc),
        'best_epoch': best_epoch,
        'final_validation_accuracy': float(final_val_acc),
        'num_tiles': len(tile_paths),
        'num_matrices': len(unique_matrix_indices),
        'num_train_tiles': len(train_dataset),
        'num_val_tiles': len(val_dataset),
        'device': str(device),
        'best_model_file': best_model_filename if best_model_filename is not None else "none",
        'final_model_file': final_model_filename,
        'training_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Générer un nom pour le fichier de métadonnées
    # Extraire uniquement le nom du dossier batch, pas le chemin complet
    batch_name = os.path.basename(batch_dir)
    # Sanitiser le nom pour éviter les caractères invalides
    batch_name_safe = ''.join(c if c.isalnum() else '_' for c in batch_name)
    metadata_filename = f"training_metadata_{batch_name_safe}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    metadata_path = os.path.join(model_save_dir, metadata_filename)
    
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=4)
    
    print(f"Métadonnées d'entraînement sauvegardées à: {metadata_path}")
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
        
        # Classification heads pour chaque niveau d'encodeur
        self.final_conv = nn.Conv2d(64, 32, kernel_size=1)  # Pour e1 et d1
        self.final_conv_e2 = nn.Conv2d(128, 32, kernel_size=1)  # Pour e2
        self.final_conv_e3 = nn.Conv2d(256, 32, kernel_size=1)  # Pour e3
        
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
        # Récupérer les dimensions spatiales d'entrée
        _, _, h, w = x.shape
        
        # Encoder
        e1 = self.enc1(x)
        # Appliquer le pooling seulement si les dimensions sont suffisantes
        if h > 1 and w > 1:
            p1 = self.pool(e1)
            
            e2 = self.enc2(p1)
            # Vérifier à nouveau les dimensions
            _, _, h2, w2 = e2.shape
            if h2 > 1 and w2 > 1:
                p2 = self.pool(e2)
                
                e3 = self.enc3(p2)
                # Vérifier à nouveau les dimensions
                _, _, h3, w3 = e3.shape
                if h3 > 1 and w3 > 1:
                    p3 = self.pool(e3)
                    
                    # Bottleneck
                    e4 = self.enc4(p3)
                    
                    # Decoder avec skip connections complets
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
                    
                    # Classification avec le chemin complet
                    x = self.final_conv(d1)
                else:
                    # Si trop petit après le 2e pooling, utiliser directement e3
                    x = self.final_conv_e3(e3)
            else:
                # Si trop petit après le 1er pooling, utiliser directement e2
                x = self.final_conv_e2(e2)
        else:
            # Si déjà trop petit pour le 1er pooling, utiliser directement e1
            x = self.final_conv(e1)
        
        # Final classification (global pooling + MLP)
        output = self.classifier(x)
        return output

if __name__ == "__main__":
    main()