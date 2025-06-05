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

# Réutiliser la même classe MatrixDataset du fichier train_resnet_matrices.py
# On importe cette classe depuis l'autre fichier
try:
    from train_resnet_matrices import MatrixDataset, AugmentedMatrixDataset, custom_collate_fn, create_balanced_sampler, evaluate_model
except ImportError:
    # Si le module n'est pas accessible directement, essayer avec le préfixe du dossier
    try:
        from unet.train_resnet_matrices import MatrixDataset, AugmentedMatrixDataset, custom_collate_fn, create_balanced_sampler, evaluate_model
    except ImportError:
        # Si toujours pas accessible, afficher un message d'erreur
        logging.error("Impossible d'importer les classes nécessaires depuis train_resnet_matrices.py")
        logging.error("Assurez-vous que ce fichier est dans le même dossier ou dans le dossier 'unet'")
        raise

# Définition du bloc de convolution double pour UNet
class DoubleConv(nn.Module):
    def __init__(self, in_channels, out_channels, mid_channels=None):
        super().__init__()
        if not mid_channels:
            mid_channels = out_channels
        self.double_conv = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(mid_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(mid_channels, out_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.double_conv(x)

# Définition du bloc de down-sampling pour UNet
class Down(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.maxpool_conv = nn.Sequential(
            nn.MaxPool2d(2),
            DoubleConv(in_channels, out_channels)
        )

    def forward(self, x):
        return self.maxpool_conv(x)

# Définition du bloc de up-sampling pour UNet
class Up(nn.Module):
    def __init__(self, in_channels, out_channels, bilinear=True):
        super().__init__()

        # Si bilinear, utiliser une up-convolution normal sans convolution transposée
        if bilinear:
            self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
            self.conv = DoubleConv(in_channels, out_channels, in_channels // 2)
        else:
            self.up = nn.ConvTranspose2d(in_channels, in_channels // 2, kernel_size=2, stride=2)
            self.conv = DoubleConv(in_channels, out_channels)

    def forward(self, x1, x2):
        x1 = self.up(x1)
        # Gestion dynamique des différences de dimensions
        diffY = x2.size()[2] - x1.size()[2]
        diffX = x2.size()[3] - x1.size()[3]

        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
                        diffY // 2, diffY - diffY // 2])
        x = torch.cat([x2, x1], dim=1)
        return self.conv(x)

# Définition du bloc de sortie pour UNet
class OutConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(OutConv, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1)

    def forward(self, x):
        return self.conv(x)

# Modèle UNet adapté pour des matrices de tailles variables avec classification binaire
class AdaptiveUNet(nn.Module):
    def __init__(self, n_channels=1, bilinear=False, dropout_rate=0.5):
        super(AdaptiveUNet, self).__init__()
        self.n_channels = n_channels
        self.bilinear = bilinear
        
        factor = 2 if bilinear else 1
        
        # Encodeur
        self.inc = DoubleConv(n_channels, 64)
        self.down1 = Down(64, 128)
        self.down2 = Down(128, 256)
        self.down3 = Down(256, 512)
        self.down4 = Down(512, 1024 // factor)
        
        # Décodeur
        self.up1 = Up(1024, 512 // factor, bilinear)
        self.up2 = Up(512, 256 // factor, bilinear)
        self.up3 = Up(256, 128 // factor, bilinear)
        self.up4 = Up(128, 64, bilinear)
        
        # Couche de classification finale
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.dropout = nn.Dropout(dropout_rate)
        self.fc = nn.Linear(64, 1)
        self.sigmoid = nn.Sigmoid()
        
        # Initialisation des poids
        self._init_weights()
        
    def _init_weights(self):
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
        
    def forward(self, x):
        # Encodeur
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        
        # Décodeur
        x = self.up1(x5, x4)
        x = self.up2(x, x3)
        x = self.up3(x, x2)
        x = self.up4(x, x1)
        
        # Classification
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.dropout(x)
        x = self.fc(x)
        x = self.sigmoid(x)
        
        return x

def create_unet_model(input_channels=1, bilinear=False, dropout_rate=0.5):
    """
    Crée un modèle UNet adaptatif
    
    Args:
        input_channels (int): Nombre de canaux d'entrée
        bilinear (bool): Utiliser l'interpolation bilinéaire pour l'upsampling
        dropout_rate (float): Taux de dropout
    
    Returns:
        Un modèle UNet adaptatif configuré
    """
    return AdaptiveUNet(n_channels=input_channels, bilinear=bilinear, dropout_rate=dropout_rate)

# Fonction principale d'entraînement (adaptée de train_resnet_matrices.py)
def train_model(model, train_loader, val_loader, criterion, optimizer, 
               scheduler=None, num_epochs=30, device='cuda', 
               model_save_dir='models', batch_name='default', 
               early_stopping_patience=10, class_weights=None,
               use_amp=False):
    """
    Fonction d'entraînement complète pour le modèle UNet.
    
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
            best_model_filename = f"adaptive_unet_{batch_name}_e{epoch+1}_acc{val_acc:.4f}_{timestamp}.pth"
            best_model_path = os.path.join(model_save_dir, best_model_filename)
            
            torch.save(model.state_dict(), best_model_path)
            logger.info(f"Meilleur modèle sauvegardé: {best_model_path}")
            
            # Si l'accuracy est très bonne, sauvegarder un checkpoint supplémentaire
            if val_acc > 0.9 and val_acc_per_class.get(0, 0) > 0.8 and val_acc_per_class.get(1, 0) > 0.8:
                checkpoint_path = os.path.join(model_save_dir, f"adaptive_unet_checkpoint_acc{val_acc:.4f}.pth")
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
    final_model_filename = f"adaptive_unet_{batch_name}_final_e{num_epochs}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pth"
    final_model_path = os.path.join(model_save_dir, final_model_filename)
    torch.save(model.state_dict(), final_model_path)
    logger.info(f"Modèle final sauvegardé: {final_model_path}")
    
    # Sauvegarder l'historique d'entraînement
    batch_name_safe = ''.join(c if c.isalnum() else '_' for c in os.path.basename(batch_name))
    history_filename = f"adaptive_unet_history_{batch_name_safe}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
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
    plot_path = os.path.join(model_save_dir, f"adaptive_unet_learning_curves_{batch_name_safe}.png")
    plt.savefig(plot_path)
    logger.info(f"Courbes d'apprentissage sauvegardées: {plot_path}")
    
    return model, best_val_acc, best_epoch

def main():
    parser = argparse.ArgumentParser(description="Entraînement de UNet adaptatif pour la détection de code IA vs humain")
    parser.add_argument('--matrix_directory', type=str, required=True, help="Dossier contenant les matrices")
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
    parser.add_argument('--bilinear', action='store_true', 
                       help="Utiliser l'interpolation bilinéaire pour l'upsampling")
    
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
    
    # Créer le modèle UNet adaptatif
    logger.info(f"Création du modèle UNet adaptatif (bilinear={args.bilinear})")
    model = create_unet_model(
        input_channels=1,
        bilinear=args.bilinear,
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
    logger.info(f"Modèle: UNet adaptatif (bilinear={args.bilinear})")
    logger.info(f"Stratégie de redimensionnement: {args.resize_strategy}")
    logger.info(f"Meilleure accuracy: {best_val_acc:.4f} (epoch {best_epoch})")
    logger.info(f"Nombre de matrices d'entraînement: {len(train_dataset)}")
    logger.info(f"Nombre de matrices de validation: {len(val_dataset)}")
    logger.info("Entraînement terminé!")

if __name__ == "__main__":
    main() 