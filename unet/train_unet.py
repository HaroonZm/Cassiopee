import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
import os
import glob
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from collections import defaultdict
import argparse  # Ajouté pour gérer les arguments en ligne de commande
import json  # Pour sauvegarder les métadonnées d'entraînement
import datetime  # Pour générer des noms de fichiers uniques
import logging  # Pour une meilleure gestion des logs
from torch.cuda.amp import autocast, GradScaler  # Pour la précision mixte

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Dataset pour les tuiles pré-découpées avec identification simplifiée des matrices sources
class PreTiledCodeMatrixDataset(Dataset):
    def __init__(self, tile_paths, group_by_matrix=True, default_label=None, target_size=None):
        self.tile_paths = tile_paths
        self.default_label = default_label
        self.target_size = target_size  # (height, width)
        
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
        
        # Redimensionner la tuile si nécessaire
        if self.target_size is not None:
            tile = torch.tensor(tile, dtype=torch.float32).unsqueeze(0)  # Ajouter dimension canal
            if tile.shape[-2:] != self.target_size:
                tile = F.interpolate(tile.unsqueeze(0), size=self.target_size, mode='bilinear', align_corners=True)
                tile = tile.squeeze(0)  # Retirer la dimension batch
        else:
            tile = torch.tensor(tile, dtype=torch.float32).unsqueeze(0)
        
        # Créer un identifiant numérique pour la matrice source
        matrix_id = self.unique_matrices.index(info['matrix_id']) if hasattr(self, 'unique_matrices') else -1
        
        # Conversion en tenseurs
        label_tensor = torch.tensor(info['label'], dtype=torch.float32)
        matrix_id_tensor = torch.tensor(matrix_id, dtype=torch.long)
        
        # Calculer le ratio de contenu non-padding
        padding_value = 100
        content_ratio = torch.mean((tile != padding_value).float())
        content_ratio_tensor = torch.tensor(content_ratio, dtype=torch.float32)
        
        return tile, label_tensor, matrix_id_tensor, content_ratio_tensor

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
            # Vote majoritaire - calcul explicite du nombre de votes pour chaque classe
            votes_positive = sum(1 for p in preds if p > 0.5)
            votes_negative = len(preds) - votes_positive
            results[matrix_idx] = 1.0 if votes_positive > votes_negative else 0.0
        
        elif strategy == 'weighted' and content_ratios is not None:
            # Moyenne pondérée par le contenu - s'assurer que les poids sont normalisés
            ratios = matrix_to_ratios[matrix_idx]
            total_ratio = sum(ratios)
            if total_ratio > 0:
                weights = [r / total_ratio for r in ratios]
                results[matrix_idx] = sum(p * w for p, w in zip(preds, weights))
            else:
                results[matrix_idx] = np.mean(preds)
        
        elif strategy == 'hybrid':
            # Stratégie hybride adaptative avec biais corrigé
            n_tiles = len(preds)
            ratios = matrix_to_ratios[matrix_idx] if content_ratios is not None else [1.0] * n_tiles
            
            # Calculer statistiques des prédictions pour détecter les biais
            mean_pred = np.mean(preds)
            median_pred = np.median(preds)
            std_pred = np.std(preds)
            
            # Si les prédictions sont toutes proches (peu de variance),
            # être plus prudent dans l'agrégation
            if std_pred < 0.1:
                # Pour les cas où les prédictions sont toutes similaires
                # et proches de 0.5, pencher légèrement vers la classe humain
                if 0.45 <= mean_pred <= 0.55:
                    results[matrix_idx] = 0.48  # Léger biais vers humain quand incertain
                else:
                    results[matrix_idx] = mean_pred
            else:
                # Pour des prédictions plus variées, utiliser vote majoritaire pondéré
                weighted_positive = sum(ratios[i] for i in range(n_tiles) if preds[i] > 0.5)
                weighted_negative = sum(ratios[i] for i in range(n_tiles) if preds[i] <= 0.5)
                total_weight = weighted_positive + weighted_negative
                
                if weighted_positive > weighted_negative:
                    # Classe IA - s'assurer que la décision est forte
                    strength = 0.5 + 0.5 * (weighted_positive / total_weight)
                    # Appliquer un facteur de correction pour éviter le biais systématique
                    strength = min(strength, 0.95)  # Limiter la confiance max
                    results[matrix_idx] = strength
                else:
                    # Classe Humain
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
def generate_model_filename(batch_name, model_type, num_epochs, batch_size, input_size=(64, 128), accuracy=None):
    """
    Génère un nom de fichier unique pour le modèle.
    
    Args:
        batch_name: Nom du batch utilisé pour l'entraînement
        model_type: Type de modèle ('best', 'final')
        num_epochs: Nombre d'époques d'entraînement
        batch_size: Taille du batch utilisé
        input_size: Tuple (hauteur, largeur) de la taille d'entrée
        accuracy: Précision du modèle (optionnel)
    
    Returns:
        Nom de fichier unique
    """
    # Obtenir la date et l'heure actuelles au format YYYYMMDD_HHMMSS
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Nettoyer le nom du batch pour qu'il soit utilisable dans un nom de fichier
    batch_name = os.path.basename(batch_name)
    batch_name = ''.join(c if c.isalnum() else '_' for c in batch_name)
    
    # Construire le nom de fichier avec les dimensions
    filename = f"unet_{batch_name}_{input_size[0]}x{input_size[1]}_{model_type}_e{num_epochs}_b{batch_size}"
    
    # Ajouter la précision si disponible
    if accuracy is not None:
        accuracy_str = f"{accuracy:.4f}".replace('.', '')
        filename += f"_acc{accuracy_str}"
    
    # Ajouter le timestamp et l'extension
    filename += f"_{timestamp}.pth"
    
    return filename

# Nouvelles fonctions pour l'entraînement amélioré

def custom_weight_init(m):
    """
    Initialisation personnalisée des poids pour éviter les plateaux et les biais
    """
    if isinstance(m, nn.Conv2d):
        nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
        if m.bias is not None:
            # Initialiser les biais à un petit nombre négatif pour réduire les activations initiales
            # Cela aide à éviter le biais vers la classe positive (IA)
            nn.init.constant_(m.bias, -0.1)
    elif isinstance(m, nn.Linear):
        if m.out_features == 1:  # Couche de sortie pour classification binaire
            # Initialisation spéciale pour la couche de sortie
            nn.init.normal_(m.weight, mean=0.0, std=0.01)
            nn.init.constant_(m.bias, -0.2)  # Biais légèrement négatif pour contrer la tendance à prédire la classe 1
        else:
            nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            nn.init.zeros_(m.bias)
    elif isinstance(m, nn.BatchNorm2d):
        nn.init.ones_(m.weight)
        nn.init.zeros_(m.bias)

def create_balanced_sampler(dataset):
    """
    Crée un sampler pondéré pour équilibrer les classes avec une attention particulière 
    aux cas extrêmes de déséquilibre
    """
    # Récupérer les étiquettes des tuiles
    labels = []
    for i in range(len(dataset)):
        _, label, _, _ = dataset[i]
        # Convertir en entier pour bincount
        labels.append(int(label.item()))
    
    # Calculer la distribution des classes
    class_counts = np.bincount(labels)
    
    # Afficher la distribution pour le diagnostic
    logger.info(f"Distribution des classes avant équilibrage: {class_counts}")
    
    # Vérifier s'il y a un déséquilibre extrême
    if len(class_counts) > 1:
        ratio = max(class_counts) / min(class_counts)
        if ratio > 20:
            logger.warning(f"Déséquilibre extrême détecté: ratio de {ratio:.2f}. Application d'un plafonnement.")
            # Plafonner le ratio à 20 pour éviter sur-pondération excessive
            majority_count = max(class_counts)
            minority_count = min(class_counts)
            
            # Trouver les indices des classes majoritaire et minoritaire
            majority_idx = np.argmax(class_counts)
            minority_idx = np.argmin(class_counts)
            
            # Créer des poids de classe personnalisés avec plafonnement
            effective_ratio = min(ratio, 20.0)
            weights = np.ones_like(class_counts, dtype=float)
            weights[majority_idx] = 1.0
            weights[minority_idx] = effective_ratio
            
            # Calculer les poids des exemples
            sample_weights = [weights[label] for label in labels]
        else:
            # Calcul standard des poids inversement proportionnels
            class_weights = 1.0 / class_counts
            sample_weights = [class_weights[label] for label in labels]
    else:
        # S'il n'y a qu'une seule classe, utiliser des poids uniformes
        logger.warning("Une seule classe détectée dans le dataset! Vérifiez vos données.")
        sample_weights = np.ones(len(labels))
    
    # Normaliser les poids
    total_weight = sum(sample_weights)
    sample_weights = [w / total_weight * len(sample_weights) for w in sample_weights]
    
    # Créer le sampler
    weights_tensor = torch.DoubleTensor(sample_weights)
    sampler = WeightedRandomSampler(weights_tensor, len(weights_tensor))
    
    return sampler

def get_class_distribution(dataset):
    """
    Retourne la distribution des classes dans le dataset
    """
    labels = []
    for i in range(len(dataset)):
        _, label, _, _ = dataset[i]
        labels.append(label.item())
    
    # Calculer la distribution
    unique, counts = np.unique(labels, return_counts=True)
    distribution = dict(zip(unique, counts))
    
    return distribution

# Remplacer la fonction d'entraînement existante par une version améliorée
def train_model_with_tiles(model, train_loader, val_loader, criterion, optimizer, 
                          num_epochs=10, device='cuda', model_save_dir='.', 
                          batch_name='default', use_amp=True, 
                          early_stopping_patience=5, lr_scheduler=None, 
                          use_class_weight=False, class_weights=None,
                          input_size=(64, 128)):
    """
    Fonction d'entraînement améliorée avec:
    - Pondération des classes
    - Early stopping
    - Régularisation du gradient
    - Affichage détaillé des métriques
    """
    model.to(device)
    best_val_acc = 0.0
    best_val_loss = float('inf')
    best_epoch = -1
    best_model_filename = None
    patience_counter = 0
    
    # Créer le dossier pour sauvegarder si nécessaire
    os.makedirs(model_save_dir, exist_ok=True)
    
    # Préparer le nom de base du modèle
    batch_size = train_loader.batch_size
    
    # Initialiser le scaler pour la précision mixte
    scaler = GradScaler() if use_amp and device != 'cpu' else None
    
    # Historique des métriques
    history = {
        'train_loss': [],
        'val_loss': [],
        'val_acc': [],
        'val_acc_per_class': [],
        'learning_rate': []
    }
    
    for epoch in range(num_epochs):
        # Mode entraînement
        model.train()
        train_loss = 0.0
        batch_count = 0
        
        # Barre de progression
        train_pbar = tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs} - Training")
        
        for inputs, labels, _, _ in train_pbar:
            inputs, labels = inputs.to(device), labels.to(device)
            
            # Forward pass avec précision mixte si activée
            optimizer.zero_grad()
            
            if use_amp and device != 'cpu':
                with autocast():
                    outputs = model(inputs).squeeze()
                    
                    # Si une seule tuile dans le batch
                    if outputs.ndim == 0:
                        outputs = outputs.unsqueeze(0)
                    
                    # Calculer la perte avec ou sans poids de classe
                    loss = criterion(outputs, labels)
                    
                    # Appliquer les poids de classe manuellement si nécessaire
                    if use_class_weight and class_weights is not None:
                        # Créer un tenseur de poids correspondant aux étiquettes
                        sample_weights = torch.ones_like(labels)
                        for i, label in enumerate(labels):
                            sample_weights[i] = class_weights[int(label.item())]
                        loss = loss * sample_weights
                        loss = loss.mean()
                
                # Backward pass avec précision mixte
                scaler.scale(loss).backward()
                scaler.step(optimizer)
                scaler.update()
            else:
                outputs = model(inputs).squeeze()
                
                # Si une seule tuile dans le batch
                if outputs.ndim == 0:
                    outputs = outputs.unsqueeze(0)
                
                # Calculer la perte avec ou sans poids de classe
                loss = criterion(outputs, labels)
                
                # Appliquer les poids de classe manuellement si nécessaire
                if use_class_weight and class_weights is not None:
                    # Créer un tenseur de poids correspondant aux étiquettes
                    sample_weights = torch.ones_like(labels)
                    for i, label in enumerate(labels):
                        sample_weights[i] = class_weights[int(label.item())]
                    loss = loss * sample_weights
                    loss = loss.mean()
                
                # Backward pass standard
                loss.backward()
                optimizer.step()
            
            # Mettre à jour les métriques
            train_loss += loss.item()
            batch_count += 1
            
            # Mettre à jour la barre de progression
            train_pbar.set_postfix({'loss': f"{loss.item():.4f}"})
        
        # Calculer la perte moyenne d'entraînement
        train_loss = train_loss / batch_count
        
        # Évaluation sur l'ensemble de validation
        val_loss, val_acc, val_acc_per_class = evaluate_model_with_metrics(
            model, val_loader, criterion, device
        )
        
        # Mettre à jour l'historique
        history['train_loss'].append(train_loss)
        history['val_loss'].append(val_loss)
        history['val_acc'].append(val_acc)
        history['val_acc_per_class'].append(val_acc_per_class)
        history['learning_rate'].append(optimizer.param_groups[0]['lr'])
        
        # Afficher les métriques
        logger.info(f"\nEpoch {epoch+1}/{num_epochs}:")
        logger.info(f"Train Loss: {train_loss:.4f}")
        logger.info(f"Val Loss: {val_loss:.4f}")
        logger.info(f"Val Accuracy: {val_acc:.4f}")
        logger.info(f"Val Accuracy per class: {val_acc_per_class}")
        
        # Mettre à jour le scheduler si nécessaire
        if lr_scheduler is not None:
            if isinstance(lr_scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
                lr_scheduler.step(val_loss)
            else:
                lr_scheduler.step()
        
        # Sauvegarder le meilleur modèle
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_epoch = epoch + 1
            best_model_filename = generate_model_filename(
                batch_name, "best", num_epochs, batch_size, 
                input_size=input_size, accuracy=val_acc
            )
            best_model_path = os.path.join(model_save_dir, best_model_filename)
            torch.save(model.state_dict(), best_model_path)
            logger.info(f"Nouveau meilleur modèle sauvegardé: {best_model_filename}")
            patience_counter = 0
        else:
            patience_counter += 1
        
        # Early stopping
        if patience_counter >= early_stopping_patience:
            logger.info(f"Early stopping après {epoch + 1} époques")
            break
    
    # Sauvegarder le modèle final
    final_model_filename = generate_model_filename(
        batch_name, "final", num_epochs, batch_size,
        input_size=input_size
    )
    final_model_path = os.path.join(model_save_dir, final_model_filename)
    torch.save(model.state_dict(), final_model_path)
    logger.info(f"Modèle final sauvegardé: {final_model_filename}")
    
    return model, best_val_acc, best_epoch, best_model_filename

def evaluate_model_with_metrics(model, val_loader, criterion, device):
    """
    Évalue le modèle avec des métriques détaillées par classe et diagnostics avancés
    """
    model.eval()
    all_predictions = []
    all_matrix_indices = []
    all_labels = []
    all_raw_outputs = []  # Stocker les sorties brutes avant sigmoid
    val_loss = 0.0
    batch_count = 0
    
    with torch.no_grad():
        for inputs, labels, matrix_indices, _ in val_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            matrix_indices = matrix_indices.to(device)
            
            # Obtenir les prédictions brutes (avant sigmoid)
            raw_outputs = model(inputs).squeeze()
            
            # Si une seule tuile dans le batch
            if raw_outputs.ndim == 0:
                raw_outputs = raw_outputs.unsqueeze(0)
            
            # Calculer la perte
            loss = criterion(raw_outputs, labels)
            val_loss += loss.item()
            batch_count += 1
            
            # Collecter les résultats
            all_predictions.append(raw_outputs.sigmoid())  # Appliquer sigmoid pour les prédictions
            all_raw_outputs.append(raw_outputs)  # Stocker les sorties brutes
            all_matrix_indices.append(matrix_indices)
            all_labels.append(labels)
    
    # Calculer la perte moyenne
    avg_val_loss = val_loss / batch_count if batch_count > 0 else float('inf')
    
    # Concaténer tous les résultats
    all_predictions = torch.cat(all_predictions)
    all_raw_outputs = torch.cat(all_raw_outputs)
    all_matrix_indices = torch.cat(all_matrix_indices)
    all_labels = torch.cat(all_labels)
    
    # Diagnostic sur la distribution des prédictions
    pred_mean = all_predictions.mean().item()
    pred_std = all_predictions.std().item()
    pred_min = all_predictions.min().item()
    pred_max = all_predictions.max().item()
    pred_median = all_predictions.median().item()
    
    # Histogramme des prédictions
    pred_hist = torch.histc(all_predictions, bins=10, min=0.0, max=1.0).cpu().numpy()
    
    logger.info(f"Statistiques des prédictions - Mean: {pred_mean:.4f}, Std: {pred_std:.4f}, " 
          f"Min: {pred_min:.4f}, Max: {pred_max:.4f}, Median: {pred_median:.4f}")
    logger.info(f"Histogramme des prédictions: {pred_hist}")
    
    # Diagnostics sur les sorties brutes (avant sigmoid)
    raw_mean = all_raw_outputs.mean().item()
    raw_std = all_raw_outputs.std().item()
    logger.info(f"Sorties brutes (avant sigmoid) - Mean: {raw_mean:.4f}, Std: {raw_std:.4f}")
    
    # Histogramme des sorties brutes
    raw_hist = torch.histc(all_raw_outputs, bins=10, min=all_raw_outputs.min().item(), max=all_raw_outputs.max().item()).cpu().numpy()
    logger.info(f"Histogramme des sorties brutes: {raw_hist}")
    
    # Si les prédictions sont très biaisées vers une classe, proposer un seuil ajusté
    if pred_mean > 0.7:
        # Si la plupart des prédictions sont > 0.7, suggérer un seuil plus élevé
        suggested_threshold = min(0.9, pred_mean + 0.5 * pred_std)
        logger.warning(f"Biais vers la classe IA détecté! Seuil suggéré: {suggested_threshold:.4f}")
    elif pred_mean < 0.3:
        # Si la plupart des prédictions sont < 0.3, suggérer un seuil plus bas
        suggested_threshold = max(0.1, pred_mean - 0.5 * pred_std)
        logger.warning(f"Biais vers la classe Humain détecté! Seuil suggéré: {suggested_threshold:.4f}")
    else:
        suggested_threshold = 0.5
    
    # Agréger les prédictions par matrice
    matrix_to_preds = defaultdict(list)
    matrix_to_labels = {}
    
    for i, matrix_idx in enumerate(all_matrix_indices.cpu().numpy()):
        matrix_to_preds[matrix_idx].append(all_predictions[i].item())
        if matrix_idx not in matrix_to_labels:
            matrix_to_labels[matrix_idx] = all_labels[i].item()
    
    # Agréger et analyser
    matrix_preds = []
    matrix_labels = []
    
    for matrix_idx, preds in matrix_to_preds.items():
        avg_pred = np.mean(preds)
        matrix_preds.append(avg_pred)
        matrix_labels.append(matrix_to_labels[matrix_idx])
    
    matrix_preds = np.array(matrix_preds)
    matrix_labels = np.array(matrix_labels)
    
    # Évaluer avec différents seuils pour trouver l'optimal
    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    best_threshold = 0.5
    best_accuracy = 0
    
    threshold_results = {}
    for threshold in thresholds:
        matrix_pred_classes = (matrix_preds >= threshold).astype(int)
        accuracy = np.mean(matrix_pred_classes == matrix_labels)
        threshold_results[threshold] = accuracy
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_threshold = threshold
    
    logger.info(f"Performances avec différents seuils: {threshold_results}")
    logger.info(f"Meilleur seuil: {best_threshold} (Accuracy: {best_accuracy:.4f})")
    
    # Utiliser le seuil de 0.5 standard pour les métriques officielles
    matrix_pred_classes = (matrix_preds >= 0.5).astype(int)
    
    # Calculer l'accuracy globale
    accuracy = np.mean(matrix_pred_classes == matrix_labels)
    
    # Calculer l'accuracy par classe
    accuracy_per_class = {}
    for cls in np.unique(matrix_labels):
        mask = matrix_labels == cls
        if np.sum(mask) > 0:
            accuracy_per_class[int(cls)] = np.mean(matrix_pred_classes[mask] == matrix_labels[mask])
        else:
            accuracy_per_class[int(cls)] = 0.0
    
    # Calculer les métriques supplémentaires
    true_pos = np.sum((matrix_pred_classes == 1) & (matrix_labels == 1))
    false_pos = np.sum((matrix_pred_classes == 1) & (matrix_labels == 0))
    true_neg = np.sum((matrix_pred_classes == 0) & (matrix_labels == 0))
    false_neg = np.sum((matrix_pred_classes == 0) & (matrix_labels == 1))
    
    # Éviter la division par zéro
    precision = true_pos / (true_pos + false_pos) if (true_pos + false_pos) > 0 else 0
    recall = true_pos / (true_pos + false_neg) if (true_pos + false_neg) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    
    logger.info(f"Métriques détaillées - Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {f1:.4f}")
    logger.info(f"Matrice de confusion - TP: {true_pos}, FP: {false_pos}, TN: {true_neg}, FN: {false_neg}")
    
    return avg_val_loss, accuracy, accuracy_per_class

# Modification de la fonction principale pour intégrer les nouvelles options
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
    parser.add_argument('--use_amp', action='store_true', 
                       help="Utiliser la précision mixte automatique pour accélérer l'entraînement (GPU uniquement)")
    parser.add_argument('--weight_decay', type=float, default=1e-5, 
                       help="Facteur de décroissance des poids (L2)")
    parser.add_argument('--scheduler', type=str, default='none', choices=['reduce', 'cosine', 'step', 'none'], 
                       help="Type de scheduler pour le taux d'apprentissage")
    parser.add_argument('--use_sampler', action='store_true', 
                       help="Utiliser un sampler pondéré pour équilibrer les classes")
    parser.add_argument('--early_stopping', type=int, default=5, 
                       help="Patience pour l'early stopping")
    parser.add_argument('--class_weight', action='store_true', 
                       help="Appliquer des poids de classe dans la fonction de perte")
    parser.add_argument('--stratify', action='store_true', 
                       help="Stratifier les données d'entraînement et de validation par classe")
    parser.add_argument('--input_height', type=int, default=64,
                       help="Hauteur des images d'entrée pour le modèle")
    parser.add_argument('--input_width', type=int, default=128,
                       help="Largeur des images d'entrée pour le modèle")
    
    args = parser.parse_args()
    
    # Paramètres
    batch_dir = args.batch_directory
    batch_size = args.batch_size
    num_epochs = args.num_epochs
    learning_rate = args.learning_rate
    model_save_dir = args.model_save_dir
    default_label = args.default_label
    use_amp = args.use_amp
    weight_decay = args.weight_decay
    use_sampler = args.use_sampler
    early_stopping_patience = args.early_stopping
    use_class_weight = args.class_weight
    stratify = args.stratify
    input_size = (args.input_height, args.input_width)
    
    # Détection du dispositif
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(f"Utilisation de: {device}")
    
    if use_amp and device == 'cpu':
        logger.warning("La précision mixte automatique est désactivée sur CPU, seuls les GPU sont supportés")
        use_amp = False
    
    # Trouver toutes les tuiles dans le dossier de batch
    logger.info(f"Dossier batch: {batch_dir}")
    
    # Chercher d'abord dans le dossier de tuiles s'il existe
    tiles_dir = os.path.join(batch_dir, "tiles")
    if not os.path.exists(tiles_dir):
        # Sinon, utiliser directement le dossier batch
        tiles_dir = batch_dir
    
    logger.info(f"Dossier des tuiles: {tiles_dir}")
    
    # Trouver toutes les tuiles
    try:
        tile_paths = glob.glob(os.path.join(tiles_dir, "*tuile_*.npy"))
        logger.info(f"Trouvé {len(tile_paths)} tuiles")
        
        if len(tile_paths) == 0:
            logger.error("Aucune tuile trouvée. Vérifiez le dossier et le format des noms de fichiers.")
            return
    except Exception as e:
        logger.error(f"Erreur lors de la recherche des tuiles: {str(e)}")
        return
    
    # Créer le dataset avec les tuiles pré-découpées
    try:
        dataset = PreTiledCodeMatrixDataset(
            tile_paths, 
            group_by_matrix=True, 
            default_label=default_label,
            target_size=input_size
        )
        
        # S'assurer qu'il y a des tuiles valides
        if len(dataset) == 0:
            logger.error("Aucune tuile valide trouvée. Vérifiez les noms de fichiers ou utilisez --default_label pour spécifier le type de code.")
            return
        
        logger.info(f"Nombre total de tuiles valides après traitement: {len(dataset)}")
        logger.info(f"Nombre de matrices uniques: {len(dataset.unique_matrices)}")
    except Exception as e:
        logger.error(f"Erreur lors de la création du dataset: {str(e)}")
        return
    
    # Division en ensembles d'entraînement et de validation (au niveau des matrices)
    unique_matrix_indices = list(range(len(dataset.unique_matrices)))
    
    if stratify:
        # Obtenir les étiquettes des matrices pour la stratification
        matrix_labels = []
        for idx in unique_matrix_indices:
            matrix_id = dataset.unique_matrices[idx]
            tile_idx = dataset.matrix_to_tiles[matrix_id][0]
            _, label, _, _ = dataset[tile_idx]
            matrix_labels.append(label.item())
        
        # Stratifier par classe
        train_matrices, val_matrices = train_test_split(
            unique_matrix_indices, test_size=0.2, random_state=42, stratify=matrix_labels
        )
        logger.info("Utilisation de la stratification par classe pour la division des données")
    else:
        # Division aléatoire sans stratification
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
    
    # Obtenir la distribution des classes
    train_distribution = get_class_distribution(train_dataset)
    val_distribution = get_class_distribution(val_dataset)
    
    logger.info(f"Distribution des classes dans l'ensemble d'entraînement: {train_distribution}")
    logger.info(f"Distribution des classes dans l'ensemble de validation: {val_distribution}")
    
    # Créer un sampler pondéré si demandé
    train_sampler = None
    if use_sampler:
        train_sampler = create_balanced_sampler(train_dataset)
        logger.info("Utilisation d'un sampler pondéré pour équilibrer les classes")
    
    # Création des dataloaders
    train_loader = DataLoader(
        train_dataset, 
        batch_size=batch_size, 
        shuffle=(train_sampler is None),
        sampler=train_sampler
    )
    val_loader = DataLoader(val_dataset, batch_size=batch_size)
    
    # Initialisation du modèle
    model = UNetForCodeDetection()
    
    # Initialisation personnalisée des poids
    model.apply(custom_weight_init)
    logger.info("Initialisation personnalisée des poids appliquée au modèle")
    
    # Définir les poids des classes pour la fonction de perte si demandé
    class_weights = None
    criterion = nn.BCELoss()  # Default criterion without weights
    
    if use_class_weight:
        # Calculer les poids inversement proportionnels à la fréquence des classes
        class_counts = np.array([train_distribution.get(0, 0), train_distribution.get(1, 0)])
        if np.all(class_counts > 0):
            class_weights = len(train_dataset) / (2.0 * class_counts)
            logger.info(f"Poids des classes: {class_weights}")
    
    # Optimiseur avec régularisation L2
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
    
    # Scheduler pour le taux d'apprentissage
    lr_scheduler = None
    if args.scheduler == 'reduce':
        lr_scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer, mode='min', factor=0.5, patience=2, verbose=True
        )
        logger.info("Utilisation d'un scheduler ReduceLROnPlateau")
    elif args.scheduler == 'cosine':
        lr_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=num_epochs, eta_min=learning_rate/10
        )
        logger.info("Utilisation d'un scheduler CosineAnnealingLR")
    elif args.scheduler == 'step':
        lr_scheduler = torch.optim.lr_scheduler.StepLR(
            optimizer, step_size=5, gamma=0.5
        )
        logger.info("Utilisation d'un scheduler StepLR")
    
    # Entraînement du modèle
    logger.info(f"Début de l'entraînement...")
    model, best_val_acc, best_epoch, best_model_filename = train_model_with_tiles(
        model, train_loader, val_loader, criterion, optimizer, 
        num_epochs, device, model_save_dir, batch_dir, use_amp, 
        early_stopping_patience, lr_scheduler, use_class_weight, class_weights,
        input_size=input_size
    )
    
    # Sauvegarder le modèle final
    final_model_filename = generate_model_filename(
        batch_dir, "final", num_epochs, batch_size,
        input_size=input_size
    )
    final_model_path = os.path.join(model_save_dir, final_model_filename)
    torch.save(model.state_dict(), final_model_path)
    logger.info(f"Modèle final sauvegardé à: {final_model_path}")
    
    # Évaluer le modèle final
    final_val_loss, final_val_acc, final_val_acc_per_class = evaluate_model_with_metrics(model, val_loader, criterion, device)
    
    # Sauvegarder les métadonnées d'entraînement
    metadata = {
        'batch_directory': batch_dir,
        'num_epochs': num_epochs,
        'batch_size': batch_size,
        'learning_rate': float(learning_rate),
        'weight_decay': float(weight_decay),
        'use_sampler': use_sampler,
        'use_class_weight': use_class_weight,
        'scheduler': args.scheduler,
        'best_validation_accuracy': float(best_val_acc),
        'best_epoch': best_epoch,
        'final_validation_accuracy': float(final_val_acc),
        'final_validation_accuracy_per_class': {str(k): float(v) for k, v in final_val_acc_per_class.items()},
        'num_tiles': len(tile_paths),
        'num_matrices': len(unique_matrix_indices),
        'num_train_tiles': len(train_dataset),
        'num_val_tiles': len(val_dataset),
        'train_class_distribution': {str(k): int(v) for k, v in train_distribution.items()},
        'val_class_distribution': {str(k): int(v) for k, v in val_distribution.items()},
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
    
    logger.info(f"Métadonnées d'entraînement sauvegardées à: {metadata_path}")
    logger.info("Entraînement terminé!")
    logger.info(f"Meilleure accuracy: {best_val_acc:.4f} (epoch {best_epoch})")
    logger.info(f"Accuracy finale: {final_val_acc:.4f}")
    logger.info(f"Accuracy par classe - Humain: {final_val_acc_per_class.get(0, 0):.4f}, IA: {final_val_acc_per_class.get(1, 0):.4f}")

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