#!/usr/bin/env python3
import numpy as np
import torch
import torch.nn as nn
import os
import glob
import argparse
import logging
import json
import matplotlib.pyplot as plt
from collections import defaultdict
from torch.utils.data import DataLoader, Subset
import random
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score
import re

# Importer les modules nécessaires
from train_unet import PreTiledCodeMatrixDataset, UNetForCodeDetection

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def extract_input_size_from_model_name(model_path):
    """
    Extrait les dimensions d'entrée du nom du modèle.
    Format attendu: *_HxW_* où H et W sont les dimensions.
    Par exemple: unet_batch1_64x128_best_e100_b32.pth
    
    Returns:
        tuple: (height, width) ou (64, 128) par défaut si non trouvé
    """
    try:
        # Chercher le pattern de dimensions dans le nom du fichier
        filename = os.path.basename(model_path)
        match = re.search(r'_(\d+)x(\d+)_', filename)
        
        if match:
            height = int(match.group(1))
            width = int(match.group(2))
            logger.info(f"Dimensions extraites du nom du modèle : {height}x{width}")
            return height, width
        else:
            logger.warning("Dimensions non trouvées dans le nom du modèle, utilisation des valeurs par défaut (64x128)")
            return 64, 128
    except Exception as e:
        logger.warning(f"Erreur lors de l'extraction des dimensions : {e}. Utilisation des valeurs par défaut (64x128)")
        return 64, 128

def load_model(model_path, device):
    """
    Charge un modèle préentraîné et configure ses dimensions d'entrée.
    Les dimensions sont extraites du nom du fichier du modèle.
    """
    # Extraire les dimensions du nom du modèle
    input_height, input_width = extract_input_size_from_model_name(model_path)
    
    # Créer le modèle avec les dimensions extraites
    model = UNetForCodeDetection()
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()
    
    # Stocker les dimensions comme attributs du modèle pour référence future
    model.input_height = input_height
    model.input_width = input_width
    
    return model

def analyze_model_weights(model):
    """Analyse les poids du modèle pour détecter des anomalies."""
    logger.info("Analyse des poids du modèle...")
    
    # Statistiques sur les poids de chaque couche
    layer_stats = {}
    for name, param in model.named_parameters():
        if param.requires_grad:
            # Calculer des statistiques de base
            mean = param.data.mean().item()
            std = param.data.std().item()
            min_val = param.data.min().item()
            max_val = param.data.max().item()
            
            layer_stats[name] = {
                'mean': mean,
                'std': std,
                'min': min_val,
                'max': max_val,
                'near_zero': (abs(param.data) < 1e-6).float().mean().item() * 100  # % de poids proches de zéro
            }
            
            logger.info(f"Couche {name}: mean={mean:.6f}, std={std:.6f}, min={min_val:.6f}, max={max_val:.6f}, "
                   f"near_zero={layer_stats[name]['near_zero']:.2f}%")
            
            # Détecter les anomalies potentielles
            if std < 1e-4:
                logger.warning(f"Couche {name}: Variance très faible, possible problème d'initialisation ou d'apprentissage")
            
            if abs(mean) > 1.0:
                logger.warning(f"Couche {name}: Moyenne élevée, possible biais dans les prédictions")
    
    # Analyser spécifiquement la couche de sortie
    output_layers = [name for name in layer_stats.keys() if 'classifier' in name and 'weight' in name]
    if output_layers:
        logger.info("Analyse de la couche de sortie...")
        for layer_name in output_layers:
            stats = layer_stats[layer_name]
            if stats['mean'] > 0.1:
                logger.warning(f"La couche de sortie {layer_name} a un biais positif (favorise la classe IA)")
            elif stats['mean'] < -0.1:
                logger.warning(f"La couche de sortie {layer_name} a un biais négatif (favorise la classe Humain)")
    
    return layer_stats

def visualize_predictions(model, dataset, num_samples=10, device='cuda'):
    """Visualise un échantillon de prédictions pour inspection."""
    logger.info("Visualisation des prédictions sur un échantillon...")
    
    # Sélectionner un échantillon aléatoire
    indices = random.sample(range(len(dataset)), min(num_samples, len(dataset)))
    
    predictions = []
    labels = []
    matrix_ids = []
    
    for idx in indices:
        tile, label, matrix_id, _ = dataset[idx]
        
        # Prédiction
        tile = tile.unsqueeze(0).to(device)  # Ajouter dimension batch et déplacer vers device
        with torch.no_grad():
            output = model(tile).squeeze().item()
        
        # Collecter les résultats
        predictions.append(output)
        labels.append(label.item())
        matrix_ids.append(matrix_id.item())
        
        logger.info(f"Exemple {idx}: Matrice {matrix_id.item()}, Label={label.item()}, Prédiction={output:.6f}")
    
    # Visualiser les distributions
    plt.figure(figsize=(10, 6))
    plt.scatter([i for i in range(len(predictions))], predictions, c=['r' if l == 1 else 'b' for l in labels])
    plt.axhline(y=0.5, color='g', linestyle='--')
    plt.xlabel('Exemple')
    plt.ylabel('Prédiction')
    plt.title('Prédictions par exemple (Rouge=IA, Bleu=Humain)')
    plt.savefig('predictions_sample.png')
    logger.info("Graphique des prédictions enregistré dans 'predictions_sample.png'")
    
    return predictions, labels, matrix_ids

def analyze_dataset(dataset):
    """Analyse le dataset pour détecter des anomalies ou des biais."""
    logger.info("Analyse du dataset...")
    
    # Comptage des classes
    labels = []
    matrix_to_label = {}
    
    for i in range(len(dataset)):
        _, label, matrix_id, _ = dataset[i]
        labels.append(label.item())
        
        # Associer chaque matrice à son label
        if hasattr(dataset, 'unique_matrices'):
            matrix_name = dataset.unique_matrices[matrix_id.item()]
            matrix_to_label[matrix_name] = label.item()
    
    # Distribution des classes
    unique, counts = np.unique(labels, return_counts=True)
    distribution = dict(zip(unique, counts))
    
    logger.info(f"Distribution des classes: {distribution}")
    
    if len(distribution) < 2:
        logger.error("PROBLÈME CRITIQUE: Une seule classe présente dans le dataset!")
    elif 0 in distribution and 1 in distribution:
        ratio = max(distribution[0], distribution[1]) / min(distribution[0], distribution[1])
        if ratio > 3:
            logger.warning(f"Déséquilibre important des classes: {ratio:.2f}:1")
    
    # Analyse des tuiles par matrice
    matrix_tile_counts = defaultdict(int)
    if hasattr(dataset, 'matrix_to_tiles'):
        for matrix_id, tiles in dataset.matrix_to_tiles.items():
            matrix_tile_counts[matrix_id] = len(tiles)
        
        # Statistiques sur le nombre de tuiles par matrice
        tile_counts = list(matrix_tile_counts.values())
        mean_tiles = np.mean(tile_counts)
        std_tiles = np.std(tile_counts)
        min_tiles = np.min(tile_counts)
        max_tiles = np.max(tile_counts)
        
        logger.info(f"Tuiles par matrice - Moyenne: {mean_tiles:.2f}, Std: {std_tiles:.2f}, Min: {min_tiles}, Max: {max_tiles}")
        
        # Vérifier si certaines matrices ont très peu de tuiles
        few_tile_matrices = [m for m, c in matrix_tile_counts.items() if c < 3]
        if few_tile_matrices:
            logger.warning(f"{len(few_tile_matrices)} matrices ont moins de 3 tuiles, ce qui peut affecter l'agrégation")
    
    return distribution, matrix_to_label

def evaluate_full_dataset(model, dataset, device='cuda', batch_size=32):
    """Évalue le modèle sur l'ensemble du dataset avec des métriques détaillées."""
    logger.info("Évaluation sur l'ensemble du dataset...")
    
    # Créer un DataLoader
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    
    # Prédictions et labels
    all_preds = []
    all_labels = []
    all_matrix_ids = []
    
    # Évaluation
    model.eval()
    with torch.no_grad():
        for tiles, labels, matrix_ids, _ in dataloader:
            tiles = tiles.to(device)
            outputs = model(tiles).squeeze()
            
            # Gérer le cas d'un seul élément
            if outputs.ndim == 0:
                outputs = outputs.unsqueeze(0)
            
            # Collecter les résultats
            all_preds.extend(outputs.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
            all_matrix_ids.extend(matrix_ids.cpu().numpy())
    
    # Convertir en numpy arrays
    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)
    all_matrix_ids = np.array(all_matrix_ids)
    
    # Calculer la ROC et l'AUC
    fpr, tpr, thresholds = roc_curve(all_labels, all_preds)
    roc_auc = auc(fpr, tpr)
    
    # Courbe precision-recall
    precision, recall, _ = precision_recall_curve(all_labels, all_preds)
    pr_auc = average_precision_score(all_labels, all_preds)
    
    logger.info(f"AUC-ROC: {roc_auc:.4f}")
    logger.info(f"AUC-PR: {pr_auc:.4f}")
    
    # Trouver le meilleur seuil sur la courbe ROC (point le plus proche de (0,1))
    optimal_idx = np.argmin(np.sqrt((1-tpr)**2 + fpr**2))
    optimal_threshold = thresholds[optimal_idx]
    
    logger.info(f"Seuil optimal (basé sur ROC): {optimal_threshold:.4f}")
    
    # Calculer l'accuracy à différents seuils
    standard_threshold = 0.5
    optimal_accuracy = np.mean((all_preds >= optimal_threshold) == all_labels)
    standard_accuracy = np.mean((all_preds >= standard_threshold) == all_labels)
    
    logger.info(f"Accuracy avec seuil standard (0.5): {standard_accuracy:.4f}")
    logger.info(f"Accuracy avec seuil optimal ({optimal_threshold:.4f}): {optimal_accuracy:.4f}")
    
    # Analyse par matrice
    matrix_to_preds = defaultdict(list)
    matrix_to_labels = {}
    
    for i in range(len(all_matrix_ids)):
        matrix_id = all_matrix_ids[i]
        matrix_to_preds[matrix_id].append(all_preds[i])
        if matrix_id not in matrix_to_labels:
            matrix_to_labels[matrix_id] = all_labels[i]
    
    # Agréger les prédictions par matrice
    matrix_preds = []
    matrix_labels = []
    
    for matrix_id, preds in matrix_to_preds.items():
        avg_pred = np.mean(preds)
        matrix_preds.append(avg_pred)
        matrix_labels.append(matrix_to_labels[matrix_id])
    
    matrix_preds = np.array(matrix_preds)
    matrix_labels = np.array(matrix_labels)
    
    # Accuracy au niveau des matrices
    matrix_accuracy = np.mean((matrix_preds >= standard_threshold) == matrix_labels)
    logger.info(f"Accuracy au niveau des matrices: {matrix_accuracy:.4f}")
    
    # Tracer les courbes ROC et PR
    plt.figure(figsize=(12, 5))
    
    # ROC
    plt.subplot(1, 2, 1)
    plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.4f}')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('Taux de faux positifs')
    plt.ylabel('Taux de vrais positifs')
    plt.title('Courbe ROC')
    plt.legend()
    
    # Precision-Recall
    plt.subplot(1, 2, 2)
    plt.plot(recall, precision, label=f'AUC-PR = {pr_auc:.4f}')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Courbe Precision-Recall')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('roc_pr_curves.png')
    logger.info("Courbes ROC et PR enregistrées dans 'roc_pr_curves.png'")
    
    # Analyser les statistiques des prédictions
    # Histogramme des prédictions séparées par classe
    plt.figure(figsize=(12, 5))
    
    # Prédictions pour la classe Humain
    plt.subplot(1, 2, 1)
    human_preds = all_preds[all_labels == 0]
    if len(human_preds) > 0:
        plt.hist(human_preds, bins=20, alpha=0.7)
        plt.axvline(x=0.5, color='r', linestyle='--')
        plt.xlabel('Prédiction')
        plt.ylabel('Fréquence')
        plt.title(f'Prédictions pour Humain (n={len(human_preds)})')
    else:
        plt.text(0.5, 0.5, 'Pas de données Humain', horizontalalignment='center')
    
    # Prédictions pour la classe IA
    plt.subplot(1, 2, 2)
    ai_preds = all_preds[all_labels == 1]
    if len(ai_preds) > 0:
        plt.hist(ai_preds, bins=20, alpha=0.7)
        plt.axvline(x=0.5, color='r', linestyle='--')
        plt.xlabel('Prédiction')
        plt.ylabel('Fréquence')
        plt.title(f'Prédictions pour IA (n={len(ai_preds)})')
    else:
        plt.text(0.5, 0.5, 'Pas de données IA', horizontalalignment='center')
    
    plt.tight_layout()
    plt.savefig('prediction_histograms.png')
    logger.info("Histogrammes des prédictions enregistrés dans 'prediction_histograms.png'")
    
    # Retourner les statistiques et métriques
    metrics = {
        'roc_auc': roc_auc,
        'pr_auc': pr_auc,
        'optimal_threshold': optimal_threshold,
        'standard_accuracy': standard_accuracy,
        'optimal_accuracy': optimal_accuracy,
        'matrix_accuracy': matrix_accuracy
    }
    
    return metrics, all_preds, all_labels, all_matrix_ids

def main():
    parser = argparse.ArgumentParser(description="Outil de diagnostic pour modèles de détection de code IA")
    parser.add_argument('--model_path', type=str, required=True, help="Chemin vers le modèle à analyser")
    parser.add_argument('--data_dir', type=str, required=True, help="Répertoire contenant les tuiles")
    parser.add_argument('--output_dir', type=str, default="diagnostics", help="Répertoire pour les résultats")
    parser.add_argument('--batch_size', type=int, default=32, help="Taille du batch pour l'évaluation")
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu', 
                        help="Dispositif à utiliser (cuda/cpu)")
    
    args = parser.parse_args()
    
    # Créer le répertoire de sortie
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Configurer le logger pour écrire dans un fichier
    file_handler = logging.FileHandler(os.path.join(args.output_dir, 'diagnostic.log'))
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    
    logger.info(f"Démarrage du diagnostic sur le modèle: {args.model_path}")
    logger.info(f"Données: {args.data_dir}")
    logger.info(f"Dispositif: {args.device}")
    
    # Charger le modèle
    try:
        model = load_model(args.model_path, args.device)
        logger.info("Modèle chargé avec succès")
    except Exception as e:
        logger.error(f"Erreur lors du chargement du modèle: {str(e)}")
        return
    
    # Analyser les poids du modèle
    weight_stats = analyze_model_weights(model)
    
    # Rechercher les tuiles
    try:
        tile_paths = glob.glob(os.path.join(args.data_dir, "*tuile_*.npy"))
        logger.info(f"Trouvé {len(tile_paths)} tuiles")
        
        if len(tile_paths) == 0:
            logger.error("Aucune tuile trouvée dans le répertoire spécifié")
            return
    except Exception as e:
        logger.error(f"Erreur lors de la recherche des tuiles: {str(e)}")
        return
    
    # Créer le dataset
    try:
        dataset = PreTiledCodeMatrixDataset(tile_paths, group_by_matrix=True)
        logger.info(f"Dataset créé avec {len(dataset)} tuiles")
    except Exception as e:
        logger.error(f"Erreur lors de la création du dataset: {str(e)}")
        return
    
    # Analyser le dataset
    class_distribution, matrix_labels = analyze_dataset(dataset)
    
    # Visualiser quelques prédictions
    sample_preds, sample_labels, sample_matrix_ids = visualize_predictions(
        model, dataset, num_samples=20, device=args.device
    )
    
    # Évaluer sur l'ensemble du dataset
    metrics, all_preds, all_labels, all_matrix_ids = evaluate_full_dataset(
        model, dataset, device=args.device, batch_size=args.batch_size
    )
    
    # Sauvegarder les métriques et statistiques
    results = {
        'model_path': args.model_path,
        'data_dir': args.data_dir,
        'num_tiles': len(dataset),
        'class_distribution': {str(k): int(v) for k, v in class_distribution.items()},
        'metrics': {k: float(v) for k, v in metrics.items()},
        'weight_stats': {k: {k2: float(v2) for k2, v2 in v.items()} for k, v in weight_stats.items()},
    }
    
    with open(os.path.join(args.output_dir, 'diagnostic_results.json'), 'w') as f:
        json.dump(results, f, indent=4)
    
    logger.info(f"Diagnostic terminé. Résultats enregistrés dans {args.output_dir}")
    logger.info(f"Résumé: AUC-ROC={metrics['roc_auc']:.4f}, Accuracy={metrics['standard_accuracy']:.4f}")
    
    if metrics['standard_accuracy'] < 0.6:
        logger.warning("PROBLÈME DÉTECTÉ: Accuracy très faible, le modèle pourrait ne pas apprendre correctement")
    
    if abs(metrics['standard_accuracy'] - max(class_distribution.values()) / sum(class_distribution.values())) < 0.05:
        logger.warning("PROBLÈME DÉTECTÉ: Accuracy proche de la distribution majoritaire, le modèle pourrait prédire toujours la même classe")
    
    # Suggestions pour améliorer le modèle
    logger.info("\n=== SUGGESTIONS D'AMÉLIORATION ===")
    
    if len(class_distribution) < 2 or max(class_distribution.values()) / min(class_distribution.values()) > 3:
        logger.info("1. Équilibrer les classes dans les données d'entraînement")
        logger.info("   - Utiliser un sampler pondéré (WeightedRandomSampler)")
        logger.info("   - Appliquer des poids de classe dans la fonction de perte")
    
    if metrics['optimal_threshold'] != 0.5 and abs(metrics['optimal_threshold'] - 0.5) > 0.1:
        logger.info(f"2. Ajuster le seuil de décision à {metrics['optimal_threshold']:.4f} au lieu de 0.5")
    
    if any(s['near_zero'] > 50 for s in weight_stats.values()):
        logger.info("3. Problème potentiel d'évanouissement du gradient, essayer:")
        logger.info("   - Réduire la profondeur du réseau")
        logger.info("   - Utiliser des connexions résiduelles")
        logger.info("   - Modifier l'initialisation des poids")
    
    logger.info("4. Essayer une architecture plus simple (CNN standard)")
    logger.info("5. Augmenter la régularisation (dropout, weight decay)")
    logger.info("6. Vérifier le prétraitement des données")

if __name__ == "__main__":
    main() 