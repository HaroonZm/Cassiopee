# Guide d'utilisation des outils OpenAI Batch API

Outils pour traiter des datasets de code Python avec l'API Batch d'OpenAI (50% d'économie sur les coûts API).


## Flexible Batch Processor

Traite des datasets de code Python et génère des variations avec l'API Batch.

### Utilisation de base

```bash
# Pour dataset CodeNet (avec énoncés)
python flexible_batch_processor.py --input codenet --output output_dir

# Pour dataset de code Python simple
python flexible_batch_processor.py --input dossier_code --output output_dir
```

### Options principales

```bash
--test              # Mode test (petit échantillon)
--variations N      # Nombre de variations par fichier (défaut: 3)
--generations N     # Nombre de générations par problème (défaut: 2, CodeNet uniquement)
--problems N        # Limite de problèmes à traiter (CodeNet uniquement)
--files N           # Limite de fichiers à traiter (dataset simple uniquement)
--batch-size N      # Taille des batchs (défaut: 1000, max: 50000)
```

### Exemples

```bash
# Mode test
python flexible_batch_processor.py --input codenet --output test_dir --test

# Contrôle avancé
python flexible_batch_processor.py --input codenet --output output_dir \
  --variations 5 --problems 20 --batch-size 5000
```

## Simple Batch Manager

Permet de gérer et récupérer les résultats des batchs indépendamment.

### Commandes

```bash
# Lister tous les batchs
python batch_manager.py list

# Vérifier l'état d'un batch
python batch_manager.py status batch_abc123

# Récupérer les résultats
python batch_manager.py fetch batch_abc123 --save
```

### Options fetch

```bash
--save              # Sauvegarde les résultats dans des fichiers
--save-raw          # Sauvegarde les résultats bruts (JSONL)
--force             # Force la récupération même si non terminé
--destination DIR   # Répertoire personnalisé pour les résultats
```

## Workflow typique

```bash
# 1. Soumettre les batchs
python flexible_batch_processor.py --input codenet --output output_dir

# 2. Vérifier l'état périodiquement
python simple_batch_manager.py list
python simple_batch_manager.py status batch_abc123

# 3. Récupérer les résultats quand terminés
python simple_batch_manager.py fetch batch_abc123 --save
```

## Structure des résultats

### CodeNet
```
output_dir/
  ├── metadata/
  │    └── dataset_metadata.jsonl
  └── p00000/
       ├── original_s12345.py/
       │    ├── original.py
       │    ├── ai_style_functional.py
       │    └── ai_style_oop.py
       └── from_scratch/
            └── ai_generated_standard.py
```

### The Stack
```
output_dir/
  ├── metadata/
  │    └── dataset_metadata.jsonl
  └── dossier/
       └── script1/
           ├── original.py
           ├── ai_style_functional.py
           └── ai_style_oop.py
```

## Astuces

- Commencez avec `--test` pour valider votre configuration
- Utilisez `--batch-size 5000` pour les grands datasets
- Pour les très grands datasets, utilisez `--problems`/`--files` pour traiter par lots
- L'API Batch offre 50% d'économie mais surveiller vos coûts sur le tableau de bord OpenAI