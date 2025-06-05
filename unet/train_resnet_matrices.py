#!/usr/bin/env python3
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler, Subset, random_split
import os
import glob
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from collections import defaultdict
import argparse
import json
import datetime
import logging
import matplotlib.pyplot as plt
import random
from torch.cuda.amp import autocast, GradScaler

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MatrixDataset(Dataset):
    """
    Dataset pour charger directement les matrices au lieu des tuiles
    Gère les matrices de différentes tailles
    """
    def __init__(self, matrix_paths, normalize_type='minmax', resize_strategy='pad_to_max'):
        self.matrix_paths = matrix_paths
        self.normalize_type = normalize_type
        self.resize_strategy = resize_strategy
        
        # Extraire les métadonnées des noms de fichiers
        self.matrix_info = []
        
        logger.info("Chargement des métadonnées des matrices...")
        for i, path in enumerate(tqdm(matrix_paths)):
            filename = os.path.basename(path)
            
            # Déterminer l'étiquette à partir du nom de la matrice
            # Identifier les codes générés par IA
            if ("gen" in filename.lower() or "var" in filename.lower() or 
                "ia" in filename.lower() or "ai" in filename.lower()):
                label = 1.0  # Code généré par IA
            # Identifier les codes humains
            elif "human" in filename.lower() or "original" in filename.lower():
                label = 0.0  # Code écrit par humain
            # Reconnaître les formats spécifiques mat_* 
            elif filename.startswith("mat_"):
                # Analyser le nom après le préfixe mat_
                base_name = filename[4:]  # Enlever "mat_"
                
                # Déterminer le type de code basé sur le nom du fichier original
                if ("gen" in base_name.lower() or "var" in base_name.lower() or 
                    "ia" in base_name.lower() or "ai" in base_name.lower()):
                    label = 1.0  # Code généré par IA
                elif ("human" in base_name.lower() or "original" in base_name.lower() or 
                      "codenet" in base_name.lower() and not "ai" in base_name.lower()):
                    label = 0.0  # Code écrit par humain
                else:
                    # Par défaut, considérer comme du code humain
                    label = 0.0
            # Reconnaissance des formats spécifiques à CodeNet
            elif "_s" in filename.lower() and "batch" in filename.lower():
                # Pour les matrices de CodeNet (s = solution), on suppose que c'est un code humain
                label = 0.0  # Code humain (CodeNet)
            else:
                # Par défaut, considérer tous les autres fichiers comme du code humain
                label = 0.0
            
            # Stocker les informations
            self.matrix_info.append({
                'path': path,
                'label': label,
                'filename': filename
            })
        
        # Trouver la taille maximale pour le padding (si nécessaire)
        if resize_strategy == 'pad_to_max':
            max_rows, max_cols = 0, 0
            valid_matrices = []
            
            for info in self.matrix_info:
                try:
                    matrix = self._load_matrix(info['path'])
                    
                    # Normaliser l'orientation des matrices
                    rows, cols = matrix.shape
                    if rows > cols:
                        # Si la matrice est plus haute que large, la transposer
                        matrix = matrix.T
                        rows, cols = cols, rows
                    
                    max_rows = max(max_rows, rows)
                    max_cols = max(max_cols, cols)
                    valid_matrices.append(info)
                except Exception as e:
                    logger.warning(f"Erreur lors du chargement de {info['path']}: {e}")
                    # Ne pas ajouter cette matrice à la liste valide
            
            # Remplacer la liste originale par la liste des matrices valides
            self.matrix_info = valid_matrices
            logger.info(f"Nombre de matrices valides après filtrage: {len(self.matrix_info)}")
            
            # Définir la taille maximale avec orientation cohérente (hauteur <= largeur)
            self.max_size = (max_rows, max_cols)
            logger.info(f"Taille maximale des matrices après normalisation d'orientation: {self.max_size}")
    
    def __len__(self):
        return len(self.matrix_info)
    
    def _load_matrix(self, path):
        """
        Charge une matrice à partir d'un fichier.
        Supporte plusieurs formats.
        """
        try:
            if path.endswith('.npy'):
                # Charger un fichier .npy
                return np.load(path)
            elif path.endswith('.npz'):
                # Charger un fichier .npz (archive de plusieurs matrices)
                # On prend la première matrice de l'archive
                with np.load(path) as data:
                    return data[list(data.keys())[0]]
            elif path.endswith('.txt') or path.endswith('.csv'):
                # Charger un fichier texte
                return np.loadtxt(path)
            else:
                raise ValueError(f"Format de fichier non supporté: {path}")
        except Exception as e:
            raise Exception(f"Erreur lors du chargement de la matrice: {e}")
    
    def _normalize_matrix(self, matrix):
        """
        Normalise une matrice selon la méthode spécifiée
        """
        # Remplacer les valeurs NaN et inf
        matrix = np.nan_to_num(matrix, neginf=-100.0)
        
        if self.normalize_type == 'minmax':
            # Min-max normalization
            min_val = np.min(matrix)
            max_val = np.max(matrix)
            if max_val > min_val:  # Éviter la division par zéro
                matrix = (matrix - min_val) / (max_val - min_val)
            else:
                matrix = np.zeros_like(matrix)
        elif self.normalize_type == 'zscore':
            # Z-score normalization
            mean = np.mean(matrix)
            std = np.std(matrix)
            if std > 0:  # Éviter la division par zéro
                matrix = (matrix - mean) / std
            else:
                matrix = np.zeros_like(matrix)
        elif self.normalize_type == 'robust':
            # Robust scaling basé sur les quantiles
            q25 = np.percentile(matrix, 25)
            q75 = np.percentile(matrix, 75)
            iqr = q75 - q25
            if iqr > 0:
                matrix = (matrix - q25) / iqr
            else:
                # Si IQR == 0, utiliser min-max
                min_val = np.min(matrix)
                max_val = np.max(matrix)
                if max_val > min_val:
                    matrix = (matrix - min_val) / (max_val - min_val)
                else:
                    matrix = np.zeros_like(matrix)
        
        # Contraindre les valeurs entre 0 et 1
        matrix = np.clip(matrix, 0, 1)
        return matrix
    
    def _resize_matrix(self, matrix):
        """
        Redimensionne la matrice selon la stratégie choisie
        """
        # Normaliser l'orientation des matrices
        # Pour que toutes les matrices aient la même orientation (hauteur ≤ largeur)
        rows, cols = matrix.shape
        if rows > cols:
            # Transposer la matrice si elle est plus haute que large
            matrix = matrix.T
            # Mettre à jour les dimensions
            rows, cols = matrix.shape
        
        if self.resize_strategy == 'pad_to_max':
            # Padding pour atteindre la taille maximale
            padded = np.zeros(self.max_size)
            padded[:rows, :cols] = matrix
            return padded
        elif self.resize_strategy == 'center_crop':
            # Redimensionner à une taille fixe (64x64) par cropping ou padding
            target_size = (64, 64)
            result = np.zeros(target_size)
            
            # Calculer les offsets pour le centrage
            row_offset = max(0, (target_size[0] - rows) // 2)
            col_offset = max(0, (target_size[1] - cols) // 2)
            
            # Déterminer la région à copier
            src_row_start = max(0, (rows - target_size[0]) // 2)
            src_col_start = max(0, (cols - target_size[1]) // 2)
            
            src_row_end = min(rows, src_row_start + target_size[0])
            src_col_end = min(cols, src_col_start + target_size[1])
            
            # Calculer les dimensions à copier
            copy_rows = src_row_end - src_row_start
            copy_cols = src_col_end - src_col_start
            
            # Copier la partie centrale
            result[row_offset:row_offset+copy_rows, col_offset:col_offset+copy_cols] = \
                matrix[src_row_start:src_row_end, src_col_start:src_col_end]
            
            return result
        elif self.resize_strategy == 'adaptive_pooling':
            # Utiliser un pooling adaptatif pour redimensionner à une taille fixe
            # Cette approche est plus efficace avec PyTorch
            target_size = (64, 64)
            
            # Convertir en tenseur pour utiliser le pooling adaptatif
            tensor = torch.from_numpy(matrix).float().unsqueeze(0).unsqueeze(0)  # [1, 1, H, W]
            
            # Appliquer un pooling adaptatif
            pooled = F.adaptive_avg_pool2d(tensor, target_size)
            
            # Reconvertir en numpy
            return pooled.squeeze().numpy()
        else:
            # Retourner la matrice telle quelle
            return matrix
    
    def __getitem__(self, idx):
        # Charger les informations de la matrice
        info = self.matrix_info[idx]
        
        # Charger la matrice
        try:
            matrix = self._load_matrix(info['path'])
        except Exception as e:
            logger.error(f"Erreur lors du chargement de {info['path']}: {e}")
            # Retourner une matrice vide en cas d'erreur
            matrix = np.zeros((64, 64))
        
        # Prétraiter la matrice
        matrix = self._normalize_matrix(matrix)
        
        # Redimensionner si nécessaire
        matrix = self._resize_matrix(matrix)
        
        # Forcer la taille standard pour toutes les matrices
        if self.resize_strategy == 'pad_to_max':
            # S'assurer que la matrice a exactement la taille maximale
            # et toujours le même format (hauteur, largeur)
            standardized = np.zeros(self.max_size)
            rows, cols = matrix.shape
            
            # Garantir que l'orientation est correcte - hauteur (rows) <= largeur (cols)
            if rows > cols:
                # Transposer si la matrice est verticale
                matrix = matrix.T
                rows, cols = cols, rows
            
            # Appliquer le padding
            standardized[:rows, :cols] = matrix
            matrix = standardized
        
        # Conversion en tenseurs
        matrix_tensor = torch.tensor(matrix, dtype=torch.float32).unsqueeze(0)  # Ajouter la dimension du canal
        label_tensor = torch.tensor(info['label'], dtype=torch.float32)
        
        return matrix_tensor, label_tensor, info['filename']

# Classe pour l'augmentation de données sur les matrices complètes
class MatrixAugmentation:
    def __init__(self, p_flip=0.5, p_rotate=0.5, p_noise=0.3, p_mask=0.2):
        self.p_flip = p_flip
        self.p_rotate = p_rotate
        self.p_noise = p_noise
        self.p_mask = p_mask
    
    def __call__(self, matrix):
        # Horizontal flip
        if random.random() < self.p_flip:
            matrix = torch.flip(matrix, [2])  # Flip horizontal
        
        # Vertical flip
        if random.random() < self.p_flip:
            matrix = torch.flip(matrix, [1])  # Flip vertical
        
        # Rotation (90, 180, 270 degrés)
        if random.random() < self.p_rotate:
            k = random.choice([1, 2, 3])  # 90, 180 ou 270 degrés
            matrix = torch.rot90(matrix, k, [1, 2])
        
        # Ajout de bruit gaussien
        if random.random() < self.p_noise:
            noise = torch.randn_like(matrix) * 0.05
            matrix = matrix + noise
            matrix = torch.clamp(matrix, 0, 1)  # Garder les valeurs entre 0 et 1
        
        # Masquage aléatoire (pour simuler des parties manquantes)
        if random.random() < self.p_mask:
            mask = torch.ones_like(matrix)
            h, w = matrix.shape[1:]
            
            # Générer un masque aléatoire
            block_size = random.randint(3, max(5, min(h, w) // 8))
            num_blocks = random.randint(1, 3)
            
            for _ in range(num_blocks):
                top = random.randint(0, h - block_size)
                left = random.randint(0, w - block_size)
                mask[:, top:top+block_size, left:left+block_size] = 0
            
            # Appliquer le masque
            matrix = matrix * mask
        
        return matrix

# Dataset avec augmentation
class AugmentedMatrixDataset(Dataset):
    def __init__(self, dataset, apply_augmentation=True):
        self.dataset = dataset
        self.apply_augmentation = apply_augmentation
        self.augmentation = MatrixAugmentation()
    
    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, idx):
        matrix, label, filename = self.dataset[idx]
        
        # Appliquer l'augmentation seulement si demandé
        if self.apply_augmentation:
            matrix = self.augmentation(matrix)
        
        return matrix, label, filename

# Définition du bloc résiduel avec pooling adaptatif
class AdaptiveResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super(AdaptiveResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.downsample = downsample
        
    def forward(self, x):
        identity = x
        
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        
        out = self.conv2(out)
        out = self.bn2(out)
        
        if self.downsample is not None:
            identity = self.downsample(x)
        
        out += identity
        out = self.relu(out)
        
        return out

# Modèle ResNet adapté pour des matrices de tailles variables
class AdaptiveResNet(nn.Module):
    def __init__(self, input_channels=1, num_classes=1, block=AdaptiveResidualBlock, layers=[2, 2, 2, 2], dropout_rate=0.5):
        super(AdaptiveResNet, self).__init__()
        self.in_channels = 64
        
        # Couche d'entrée adaptée aux matrices de taille variable
        self.conv1 = nn.Conv2d(input_channels, 64, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        
        # Blocs résiduels
        self.layer1 = self._make_layer(block, 64, layers[0], stride=1)
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2)
        
        # Global Average Pooling adaptatif - fonctionne pour toutes les tailles d'entrée
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.dropout = nn.Dropout(dropout_rate)
        self.fc = nn.Linear(512, num_classes)
        self.sigmoid = nn.Sigmoid()
        
        # Initialisation des poids
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                # Initialisation légèrement biaisée vers la classe négative (humain)
                nn.init.normal_(m.weight, 0, 0.01)
                if m.bias is not None:
                    nn.init.constant_(m.bias, -0.1)  # Biais négatif pour contrer la tendance à prédire IA
                    
    def _make_layer(self, block, out_channels, blocks, stride=1):
        downsample = None
        if stride != 1 or self.in_channels != out_channels:
            downsample = nn.Sequential(
                nn.Conv2d(self.in_channels, out_channels, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels),
            )
        
        layers = []
        layers.append(block(self.in_channels, out_channels, stride, downsample))
        self.in_channels = out_channels
        
        for _ in range(1, blocks):
            layers.append(block(self.in_channels, out_channels))
        
        return nn.Sequential(*layers)
    
    def forward(self, x):
        # Première couche
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        
        # Blocs résiduels
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        
        # Global Average Pooling adaptatif
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.dropout(x)
        
        # Couche fully connected
        x = self.fc(x)
        
        # Pour la classification binaire, retourner une seule valeur sigmoïde
        if x.size(1) == 1:
            x = self.sigmoid(x)
        
        return x

# Fonction pour créer différentes variantes de ResNet
def create_adaptive_resnet_model(model_type="resnet18", input_channels=1, num_classes=1, dropout_rate=0.5):
    """
    Crée un modèle ResNet adaptatif du type spécifié.
    
    Args:
        model_type (str): Type de ResNet ('resnet18', 'resnet34', etc.)
        input_channels (int): Nombre de canaux d'entrée
        num_classes (int): Nombre de classes de sortie
        dropout_rate (float): Taux de dropout
    
    Returns:
        Un modèle ResNet adaptatif configuré
    """
    if model_type == "resnet18":
        return AdaptiveResNet(input_channels, num_classes, AdaptiveResidualBlock, [2, 2, 2, 2], dropout_rate)
    elif model_type == "resnet34":
        return AdaptiveResNet(input_channels, num_classes, AdaptiveResidualBlock, [3, 4, 6, 3], dropout_rate)
    elif model_type == "resnet10":
        # Une version plus légère
        return AdaptiveResNet(input_channels, num_classes, AdaptiveResidualBlock, [1, 1, 1, 1], dropout_rate)
    elif model_type == "resnet26":
        # Une version intermédiaire
        return AdaptiveResNet(input_channels, num_classes, AdaptiveResidualBlock, [2, 3, 4, 3], dropout_rate)
    else:
        raise ValueError(f"Type de modèle inconnu: {model_type}") 

# Fonction pour créer un sampler pondéré pour équilibrer les classes
def create_balanced_sampler(dataset):
    """
    Crée un sampler pondéré pour équilibrer les classes
    """
    # Récupérer les étiquettes
    labels = []
    for i in range(len(dataset)):
        _, label, _ = dataset[i]
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

# Fonction d'évaluation du modèle
def evaluate_model(model, val_loader, device):
    """
    Évalue le modèle sur un ensemble de validation.
    
    Args:
        model: Le modèle à évaluer
        val_loader: DataLoader pour les données de validation
        device: Dispositif sur lequel exécuter l'évaluation
    
    Returns:
        Accuracy globale, dictionnaire d'accuracy par classe, dictionnaire de métriques détaillées
    """
    model.eval()
    all_predictions = []
    all_labels = []
    all_filenames = []
    
    with torch.no_grad():
        for inputs, labels, filenames in val_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            
            # Prédiction
            outputs = model(inputs).squeeze()
            
            # Si une seule matrice dans le batch
            if outputs.ndim == 0:
                outputs = outputs.unsqueeze(0)
            
            # Collecter les résultats
            all_predictions.append(outputs)
            all_labels.append(labels)
            all_filenames.extend(filenames)
    
    # Concaténer tous les résultats
    all_predictions = torch.cat(all_predictions)
    all_labels = torch.cat(all_labels)
    
    # Calculer des statistiques sur les prédictions
    pred_mean = all_predictions.mean().item()
    pred_std = all_predictions.std().item()
    pred_min = all_predictions.min().item()
    pred_max = all_predictions.max().item()
    
    logger.info(f"Statistiques des prédictions - Mean: {pred_mean:.4f}, Std: {pred_std:.4f}, "
               f"Min: {pred_min:.4f}, Max: {pred_max:.4f}")
    
    # Si les prédictions sont très biaisées, afficher un avertissement
    if pred_mean > 0.8:
        logger.warning("Les prédictions sont fortement biaisées vers la classe IA!")
    elif pred_mean < 0.2:
        logger.warning("Les prédictions sont fortement biaisées vers la classe Humain!")
    
    # Convertir en classes binaires
    predicted_classes = (all_predictions > 0.5).float()
    labels_np = all_labels.cpu().numpy()
    predictions_np = predicted_classes.cpu().numpy()
    
    # Calculer l'accuracy globale
    correct = (predicted_classes == all_labels).float().sum().item()
    total = len(all_labels)
    accuracy = correct / total if total > 0 else 0
    
    # Pour calculer l'accuracy par classe
    class_correct = defaultdict(int)
    class_total = defaultdict(int)
    
    # Pour calculer les métriques détaillées
    true_pos = 0
    false_pos = 0
    true_neg = 0
    false_neg = 0
    
    for i in range(len(labels_np)):
        label = int(labels_np[i])
        pred = int(predictions_np[i])
        
        # Calculer l'accuracy par classe
        if pred == label:
            class_correct[label] += 1
        class_total[label] += 1
        
        # Métriques détaillées
        if label == 1 and pred == 1:
            true_pos += 1
        elif label == 0 and pred == 1:
            false_pos += 1
        elif label == 0 and pred == 0:
            true_neg += 1
        elif label == 1 and pred == 0:
            false_neg += 1
    
    # Calculer l'accuracy par classe
    accuracy_per_class = {}
    for cls in class_total:
        accuracy_per_class[cls] = class_correct[cls] / class_total[cls] if class_total[cls] > 0 else 0
    
    # Calculer précision, rappel et f1
    precision = true_pos / (true_pos + false_pos) if (true_pos + false_pos) > 0 else 0
    recall = true_pos / (true_pos + false_neg) if (true_pos + false_neg) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    
    # Métriques détaillées
    metrics = {
        'accuracy': accuracy,
        'accuracy_per_class': accuracy_per_class,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'true_pos': true_pos,
        'false_pos': false_pos,
        'true_neg': true_neg,
        'false_neg': false_neg,
        'pred_mean': pred_mean,
        'pred_std': pred_std
    }
    
    return accuracy, accuracy_per_class, metrics

# Fonction principale d'entraînement
def train_model(model, train_loader, val_loader, criterion, optimizer, 
               scheduler=None, num_epochs=30, device='cuda', 
               model_save_dir='models', batch_name='default', 
               early_stopping_patience=10, class_weights=None,
               use_amp=False):
    """
    Fonction d'entraînement complète pour le modèle ResNet.
    
    Args:
        model: Le modèle à entraîner
        train_loader: DataLoader pour les données d'entraînement
        val_loader: DataLoader pour les données de validation
        criterion: Fonction de perte
        optimizer: Optimiseur
        scheduler: Scheduler de taux d'apprentissage (optionnel)
        num_epochs: Nombre d'époques d'entraînement
        device: Dispositif sur lequel exécuter l'entraînement
        model_save_dir: Répertoire où sauvegarder les modèles
        batch_name: Nom du lot de données
        early_stopping_patience: Patience pour l'arrêt anticipé
        class_weights: Poids des classes pour la fonction de perte
        use_amp: Utiliser la précision mixte automatique
    
    Returns:
        Le modèle entraîné, meilleure accuracy, numéro de la meilleure époque
    """
    model.to(device)
    
    # Créer le dossier de sauvegarde
    os.makedirs(model_save_dir, exist_ok=True)
    
    # Initialiser le scaler pour la précision mixte
    scaler = GradScaler() if use_amp and device != 'cpu' else None
    
    # Métriques de suivi
    best_val_acc = 0.0
    best_val_loss = float('inf')
    best_epoch = -1
    best_model_filename = None
    patience_counter = 0
    
    # Historique pour tracer les courbes
    history = {
        'train_loss': [],
        'train_acc': [],
        'val_loss': [],
        'val_acc': [],
        'val_acc_per_class': [],
        'learning_rate': []
    }
    
    # Fonction pour calculer l'accuracy
    def calculate_accuracy(outputs, labels):
        predicted = (outputs >= 0.5).float()
        correct = (predicted == labels).float().sum()
        return correct / len(labels)
    
    for epoch in range(num_epochs):
        # Phase d'entraînement
        model.train()
        train_loss = 0.0
        train_acc = 0.0
        batch_count = 0
        
        # Barre de progression
        pbar = tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs} - Training")
        for inputs, labels, _ in pbar:
            inputs, labels = inputs.to(device), labels.to(device)
            
            # Nettoyer les gradients
            optimizer.zero_grad()
            
            # Forward pass avec précision mixte si activée
            if use_amp and device != 'cpu':
                with autocast():
                    outputs = model(inputs).squeeze()
                    
                    # Si une seule matrice dans le batch
                    if outputs.ndim == 0:
                        outputs = outputs.unsqueeze(0)
                    
                    # Calculer la perte
                    loss = criterion(outputs, labels)
                    
                    # Appliquer les poids de classe manuellement si fournis
                    if class_weights is not None:
                        sample_weights = torch.ones_like(labels)
                        for i, label in enumerate(labels):
                            weight_idx = int(label.item())
                            sample_weights[i] = torch.tensor(class_weights[weight_idx], device=device)
                        
                        loss = loss * sample_weights
                        loss = loss.mean()
                
                # Backward pass avec scaling
                scaler.scale(loss).backward()
                
                # Clip gradient norm pour éviter l'explosion du gradient
                scaler.unscale_(optimizer)
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                
                scaler.step(optimizer)
                scaler.update()
            else:
                # Version standard sans précision mixte
                outputs = model(inputs).squeeze()
                
                # Si une seule matrice dans le batch
                if outputs.ndim == 0:
                    outputs = outputs.unsqueeze(0)
                
                # Calculer la perte
                loss = criterion(outputs, labels)
                
                # Appliquer les poids de classe manuellement si fournis
                if class_weights is not None:
                    sample_weights = torch.ones_like(labels)
                    for i, label in enumerate(labels):
                        weight_idx = int(label.item())
                        sample_weights[i] = torch.tensor(class_weights[weight_idx], device=device)
                    
                    loss = loss * sample_weights
                    loss = loss.mean()
                
                # Backward pass
                loss.backward()
                
                # Clip gradient norm pour éviter l'explosion du gradient
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                
                optimizer.step()
            
            # Calculer l'accuracy
            acc = calculate_accuracy(outputs, labels)
            
            # Mettre à jour les statistiques
            train_loss += loss.item()
            train_acc += acc.item()
            batch_count += 1
            
            # Mettre à jour la barre de progression
            pbar.set_postfix({'loss': loss.item(), 'acc': acc.item()})
        
        # Calculer les moyennes
        avg_train_loss = train_loss / batch_count if batch_count > 0 else float('inf')
        avg_train_acc = train_acc / batch_count if batch_count > 0 else 0
        
        # Phase d'évaluation
        model.eval()
        val_loss = 0.0
        val_batch_count = 0
        
        with torch.no_grad():
            for inputs, labels, _ in val_loader:
                inputs, labels = inputs.to(device), labels.to(device)
                
                # Forward pass
                outputs = model(inputs).squeeze()
                
                # Si une seule matrice dans le batch
                if outputs.ndim == 0:
                    outputs = outputs.unsqueeze(0)
                
                # Calculer la perte
                loss = criterion(outputs, labels)
                
                # Mettre à jour les statistiques
                val_loss += loss.item()
                val_batch_count += 1
        
        # Calculer la perte moyenne de validation
        avg_val_loss = val_loss / val_batch_count if val_batch_count > 0 else float('inf')
        
        # Évaluer le modèle sur l'ensemble de validation
        val_acc, val_acc_per_class, val_metrics = evaluate_model(model, val_loader, device)
        
        # Mettre à jour l'historique
        history['train_loss'].append(avg_train_loss)
        history['train_acc'].append(avg_train_acc)
        history['val_loss'].append(avg_val_loss)
        history['val_acc'].append(val_acc)
        history['val_acc_per_class'].append(val_acc_per_class)
        history['learning_rate'].append(optimizer.param_groups[0]['lr'])
        
        # Afficher les résultats
        logger.info(f"Epoch {epoch+1}/{num_epochs} - "
               f"Train Loss: {avg_train_loss:.4f}, Train Acc: {avg_train_acc:.4f}, "
               f"Val Loss: {avg_val_loss:.4f}, Val Acc: {val_acc:.4f}")
        
        logger.info(f"Val Metrics - Precision: {val_metrics['precision']:.4f}, "
               f"Recall: {val_metrics['recall']:.4f}, F1: {val_metrics['f1']:.4f}")
        
        logger.info(f"Val Accuracy par classe - "
               f"Humain: {val_acc_per_class.get(0, 0):.4f}, IA: {val_acc_per_class.get(1, 0):.4f}")
        
        # Mettre à jour le scheduler si fourni
        if scheduler is not None:
            if isinstance(scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
                scheduler.step(avg_val_loss)
            else:
                scheduler.step()
        
        # Sauvegarder le meilleur modèle (basé sur l'accuracy de validation)
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_val_loss = avg_val_loss
            best_epoch = epoch + 1
            patience_counter = 0
            
            # Générer un nom de fichier unique
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            best_model_filename = f"adaptive_resnet_{batch_name}_e{epoch+1}_acc{val_acc:.4f}_{timestamp}.pth"
            best_model_path = os.path.join(model_save_dir, best_model_filename)
            
            torch.save(model.state_dict(), best_model_path)
            logger.info(f"Meilleur modèle sauvegardé: {best_model_path}")
            
            # Si l'accuracy est très bonne, sauvegarder un checkpoint supplémentaire
            if val_acc > 0.9 and val_acc_per_class.get(0, 0) > 0.8 and val_acc_per_class.get(1, 0) > 0.8:
                checkpoint_path = os.path.join(model_save_dir, f"adaptive_resnet_checkpoint_acc{val_acc:.4f}.pth")
                torch.save(model.state_dict(), checkpoint_path)
                logger.info(f"Checkpoint de haute qualité sauvegardé: {checkpoint_path}")
        else:
            patience_counter += 1
            logger.info(f"Pas d'amélioration. Patience: {patience_counter}/{early_stopping_patience}")
            
            # Early stopping
            if patience_counter >= early_stopping_patience:
                logger.info(f"Early stopping après {epoch+1} époques")
                break
    
    # Sauvegarder le modèle final
    final_model_filename = f"adaptive_resnet_{batch_name}_final_e{num_epochs}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pth"
    final_model_path = os.path.join(model_save_dir, final_model_filename)
    torch.save(model.state_dict(), final_model_path)
    logger.info(f"Modèle final sauvegardé: {final_model_path}")
    
    # Sauvegarder l'historique d'entraînement
    batch_name_safe = ''.join(c if c.isalnum() else '_' for c in os.path.basename(batch_name))
    history_filename = f"adaptive_resnet_history_{batch_name_safe}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    history_path = os.path.join(model_save_dir, history_filename)
    
    # Convertir les données pour JSON
    json_history = {}
    for key, values in history.items():
        if key == 'val_acc_per_class':
            json_history[key] = [{str(k): float(v) for k, v in d.items()} for d in values]
        else:
            json_history[key] = [float(v) for v in values]
    
    with open(history_path, 'w') as f:
        json.dump(json_history, f, indent=4)
    
    logger.info(f"Historique d'entraînement sauvegardé: {history_path}")
    
    # Tracer les courbes d'apprentissage
    plt.figure(figsize=(12, 10))
    
    # Perte
    plt.subplot(2, 2, 1)
    plt.plot(history['train_loss'], label='Train Loss')
    plt.plot(history['val_loss'], label='Val Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    
    # Accuracy
    plt.subplot(2, 2, 2)
    plt.plot(history['train_acc'], label='Train Acc')
    plt.plot(history['val_acc'], label='Val Acc')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.legend()
    
    # Accuracy par classe
    plt.subplot(2, 2, 3)
    human_acc = [d.get(0, 0) for d in history['val_acc_per_class']]
    ai_acc = [d.get(1, 0) for d in history['val_acc_per_class']]
    plt.plot(human_acc, label='Human Acc')
    plt.plot(ai_acc, label='AI Acc')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Validation Accuracy per Class')
    plt.legend()
    
    # Learning rate
    plt.subplot(2, 2, 4)
    plt.plot(history['learning_rate'])
    plt.xlabel('Epoch')
    plt.ylabel('Learning Rate')
    plt.title('Learning Rate Schedule')
    
    plt.tight_layout()
    
    # Sauvegarder le graphique
    plot_path = os.path.join(model_save_dir, f"adaptive_resnet_learning_curves_{batch_name_safe}.png")
    plt.savefig(plot_path)
    logger.info(f"Courbes d'apprentissage sauvegardées: {plot_path}")
    
    return model, best_val_acc, best_epoch

# Fonction personnalisée pour collecter les éléments d'un batch
def custom_collate_fn(batch):
    """
    Fonction personnalisée pour collecter les éléments d'un batch.
    Garantit que toutes les matrices ont la même taille avant de les empiler.
    """
    matrices = []
    labels = []
    filenames = []
    
    # Extraire les éléments du batch
    for matrix, label, filename in batch:
        matrices.append(matrix)
        labels.append(label)
        filenames.append(filename)
    
    # Vérifier et standardiser la forme des matrices
    first_shape = matrices[0].shape
    target_shape = first_shape
    
    # Déterminer la forme standard (toujours avoir la plus petite dimension en premier)
    height, width = first_shape[1], first_shape[2]
    if height > width:
        # La forme standard devrait avoir height <= width
        target_shape = (first_shape[0], width, height)
    
    # Normaliser toutes les matrices à la même forme
    for i in range(len(matrices)):
        curr_shape = matrices[i].shape
        # Si les dimensions sont inversées, transposer la matrice
        if curr_shape[1] != target_shape[1] or curr_shape[2] != target_shape[2]:
            # Transposer les dimensions spatiales (1=hauteur et 2=largeur)
            matrices[i] = matrices[i].transpose(1, 2)
            logger.info(f"Matrice {i} transposée de {curr_shape} à {matrices[i].shape}")
    
    # Empiler les matrices et les labels
    matrices_tensor = torch.stack(matrices)
    labels_tensor = torch.stack(labels)
    
    return matrices_tensor, labels_tensor, filenames

def main():
    parser = argparse.ArgumentParser(description="Entraînement de ResNet adaptatif pour la détection de code IA vs humain")
    parser.add_argument('--matrix_directory', type=str, required=True, help="Dossier contenant les matrices")
    parser.add_argument('--model_type', type=str, default="resnet18", 
                       choices=["resnet10", "resnet18", "resnet26", "resnet34"],
                       help="Type de modèle ResNet à utiliser")
    parser.add_argument('--batch_size', type=int, default=16, help="Taille du batch pour l'entraînement")
    parser.add_argument('--num_epochs', type=int, default=50, help="Nombre d'époques d'entraînement")
    parser.add_argument('--learning_rate', type=float, default=0.001, help="Taux d'apprentissage initial")
    parser.add_argument('--weight_decay', type=float, default=1e-5, help="Facteur de régularisation L2")
    parser.add_argument('--dropout', type=float, default=0.5, help="Taux de dropout")
    parser.add_argument('--model_save_dir', type=str, default="models", help="Dossier où sauvegarder les modèles")
    parser.add_argument('--scheduler', type=str, default='cosine', 
                       choices=['cosine', 'reduce', 'step', 'none'],
                       help="Type de scheduler pour le taux d'apprentissage")
    parser.add_argument('--normalize', type=str, default='minmax', 
                       choices=['minmax', 'zscore', 'robust'],
                       help="Type de normalisation des données")
    parser.add_argument('--resize_strategy', type=str, default='pad_to_max', 
                       choices=['pad_to_max', 'center_crop', 'adaptive_pooling'],
                       help="Stratégie de redimensionnement des matrices")
    parser.add_argument('--augmentation', action='store_true',
                       help="Activer l'augmentation de données")
    parser.add_argument('--balance_classes', action='store_true',
                       help="Équilibrer les classes pour l'entraînement")
    parser.add_argument('--stratify', action='store_true',
                       help="Stratifier les données d'entraînement/validation par classe")
    parser.add_argument('--early_stopping', type=int, default=15,
                       help="Patience pour l'early stopping")
    parser.add_argument('--use_amp', action='store_true',
                       help="Utiliser la précision mixte automatique (accélère l'entraînement sur GPU)")
    parser.add_argument('--val_split', type=float, default=0.2,
                       help="Pourcentage des données à utiliser pour la validation")
    parser.add_argument('--seed', type=int, default=42, help="Graine aléatoire pour la reproductibilité")
    
    args = parser.parse_args()
    
    # Définir la graine aléatoire pour la reproductibilité
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)
    random.seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(args.seed)
    
    # Détection du dispositif
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(f"Utilisation de: {device}")
    
    # Désactiver AMP si sur CPU
    use_amp = args.use_amp and device.type == 'cuda'
    if args.use_amp and device.type != 'cuda':
        logger.warning("La précision mixte automatique (AMP) est désactivée sur CPU")
    
    # Rechercher les matrices de manière récursive
    logger.info(f"Recherche récursive de matrices dans {args.matrix_directory} et tous ses sous-dossiers...")
    matrix_paths = []
    extensions = ['.npy', '.npz']  # Ignorer les fichiers .txt et .csv qui causent des problèmes
    
    # Utiliser os.walk pour parcourir récursivement tous les sous-dossiers
    for root, _, files in os.walk(args.matrix_directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                full_path = os.path.join(root, file)
                matrix_paths.append(full_path)
    
    if not matrix_paths:
        logger.error(f"Aucune matrice trouvée dans {args.matrix_directory} et ses sous-dossiers")
        return
    
    logger.info(f"Trouvé {len(matrix_paths)} matrices")
    
    # Créer le dataset
    dataset = MatrixDataset(
        matrix_paths,
        normalize_type=args.normalize,
        resize_strategy=args.resize_strategy
    )
    
    # Vérifier qu'il y a des matrices valides
    if len(dataset) == 0:
        logger.error("Aucune matrice valide après traitement!")
        return
    
    # Collecter les labels pour l'analyse et la stratification
    labels = []
    for i in range(len(dataset)):
        _, label, _ = dataset[i]
        labels.append(label.item())
    
    # Division en ensembles d'entraînement et de validation
    if args.stratify:
        # Stratifier par classe
        train_indices, val_indices = train_test_split(
            range(len(dataset)), test_size=args.val_split, random_state=args.seed, 
            stratify=labels
        )
        logger.info("Stratification par classe appliquée pour la division train/val")
    else:
        # Division aléatoire
        train_indices, val_indices = train_test_split(
            range(len(dataset)), test_size=args.val_split, random_state=args.seed
        )
    
    # Créer des sous-ensembles
    train_dataset = Subset(dataset, train_indices)
    val_dataset = Subset(dataset, val_indices)
    
    logger.info(f"Matrices d'entraînement: {len(train_dataset)}")
    logger.info(f"Matrices de validation: {len(val_dataset)}")
    
    # Appliquer l'augmentation si demandée
    if args.augmentation:
        logger.info("Application de l'augmentation de données à l'ensemble d'entraînement")
        train_dataset = AugmentedMatrixDataset(train_dataset, apply_augmentation=True)
    
    # Analyse de la distribution des classes
    train_labels = [labels[i] for i in train_indices]
    val_labels = [labels[i] for i in val_indices]
    
    train_class_counts = np.bincount([int(label) for label in train_labels])
    val_class_counts = np.bincount([int(label) for label in val_labels])
    
    logger.info(f"Distribution des classes d'entraînement: {train_class_counts}")
    logger.info(f"Distribution des classes de validation: {val_class_counts}")
    
    # Créer un sampler pondéré si demandé
    train_sampler = None
    if args.balance_classes:
        logger.info("Création d'un sampler pondéré pour équilibrer les classes")
        train_sampler = create_balanced_sampler(train_dataset)
    
    # Créer les dataloaders avec notre fonction de collate personnalisée
    train_loader = DataLoader(
        train_dataset,
        batch_size=args.batch_size,
        shuffle=(train_sampler is None),
        sampler=train_sampler,
        num_workers=0,  # Ajuster si nécessaire
        pin_memory=True if device.type == 'cuda' else False,
        collate_fn=custom_collate_fn  # Utiliser notre fonction personnalisée
    )
    
    val_loader = DataLoader(
        val_dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=0,  # Ajuster si nécessaire
        pin_memory=True if device.type == 'cuda' else False,
        collate_fn=custom_collate_fn  # Utiliser notre fonction personnalisée
    )
    
    # Créer le modèle ResNet adaptatif
    logger.info(f"Création du modèle {args.model_type}")
    model = create_adaptive_resnet_model(
        model_type=args.model_type,
        input_channels=1,  # Les matrices sont en niveaux de gris
        num_classes=1,     # Classification binaire
        dropout_rate=args.dropout
    )
    
    # Définir la fonction de perte
    criterion = nn.BCELoss()
    
    # Définir l'optimiseur
    optimizer = torch.optim.Adam(
        model.parameters(), 
        lr=args.learning_rate, 
        weight_decay=args.weight_decay
    )
    
    # Définir le scheduler pour le taux d'apprentissage
    scheduler = None
    if args.scheduler == 'cosine':
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=args.num_epochs, eta_min=args.learning_rate/10
        )
        logger.info("Utilisation du scheduler CosineAnnealingLR")
    elif args.scheduler == 'reduce':
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer, mode='min', factor=0.5, patience=5, verbose=True
        )
        logger.info("Utilisation du scheduler ReduceLROnPlateau")
    elif args.scheduler == 'step':
        scheduler = torch.optim.lr_scheduler.StepLR(
            optimizer, step_size=10, gamma=0.5
        )
        logger.info("Utilisation du scheduler StepLR")
    
    # Calculer les poids des classes pour la fonction de perte
    class_weights = None
    if args.balance_classes and len(train_class_counts) > 1:
        weights = len(train_labels) / (len(train_class_counts) * train_class_counts)
        class_weights = weights / weights.sum() * len(train_class_counts)
        logger.info(f"Poids des classes: {class_weights}")
    
    # Entraîner le modèle
    logger.info(f"Début de l'entraînement pour {args.num_epochs} époques...")
    
    # Créer un nom pour le batch
    batch_name = os.path.basename(os.path.normpath(args.matrix_directory))
    
    model, best_val_acc, best_epoch = train_model(
        model=model,
        train_loader=train_loader,
        val_loader=val_loader,
        criterion=criterion,
        optimizer=optimizer,
        scheduler=scheduler,
        num_epochs=args.num_epochs,
        device=device,
        model_save_dir=args.model_save_dir,
        batch_name=batch_name,
        early_stopping_patience=args.early_stopping,
        class_weights=class_weights,
        use_amp=use_amp
    )
    
    # Résumé final
    logger.info("\n=== Résumé de l'entraînement ===")
    logger.info(f"Modèle: {args.model_type}")
    logger.info(f"Stratégie de redimensionnement: {args.resize_strategy}")
    logger.info(f"Meilleure accuracy: {best_val_acc:.4f} (epoch {best_epoch})")
    logger.info(f"Nombre de matrices d'entraînement: {len(train_dataset)}")
    logger.info(f"Nombre de matrices de validation: {len(val_dataset)}")
    logger.info("Entraînement terminé!")

if __name__ == "__main__":
    main() 