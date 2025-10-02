# Cassiopée - Système de détection de code généré par IA

Cassiopée est un système complet d'analyse et de détection de code généré par intelligence artificielle. Cette application fournit une interface graphique pour faciliter l'utilisation de l'ensemble du pipeline, de la génération de scripts d'entraînement jusqu'à la détection finale.

## Installation

1. Cloner ce dépôt:
```bash
git clone https://github.com/votre-utilisateur/Cassiopee.git
cd Cassiopee
```

2. Installer les dépendances:
```bash
pip install -r requirements.txt
```

3. Lancer l'application:
```bash
python main.py
```

## Vue d'ensemble de l'interface

L'interface principale de Cassiopée est divisée en 7 onglets, chacun correspondant à une étape du pipeline de traitement:

1. **Génération de Code IA** - Génération de scripts Python à l'aide de modèles IA
2. **Récupération de Batches** - Récupération des résultats des appels par batch à l'API OpenAI
3. **Génération des Matrices** - Création de matrices de log-probabilités pour l'analyse
4. **Génération des Tuiles** - Découpage des matrices en tuiles pour l'entraînement
5. **Entraînement U-Net** - Entraînement du modèle de détection
6. **Test U-Net** - Évaluation et utilisation du modèle entraîné
7. **Visualisation** - Visualisation des matrices et des activations du modèle

## Description détaillée des onglets

### 1. Génération de Code IA

Cet onglet permet de générer des échantillons de code Python à l'aide de modèles d'IA (GPT-4o, GPT-4.1, etc.) à partir de problèmes de programmation existants ou de code source.

**Fonctionnalités principales:**
- Sélection du dataset d'entrée (CodeNet, The Stack, etc.)
- Configuration du modèle d'IA à utiliser
- Génération de variations de code existant
- Génération de nouvelles solutions
- Mode batch pour les requêtes à l'API OpenAI
- Contrôle du volume de génération et estimation des coûts

### 2. Récupération de Batches

Cet onglet permet de récupérer les résultats des traitements par batch soumis à l'API OpenAI, que ce soit pour la génération de scripts ou pour la création de matrices.

**Fonctionnalités principales:**
- Vérification du statut des batches
- Récupération des résultats par ID de batch
- Listage des batches disponibles
- Options de sauvegarde des résultats bruts ou traités
- Construction automatique de matrices (pour les batchs de tokenisation)

### 3. Génération des Matrices

Cet onglet permet de générer des matrices de log-probabilités pour l'analyse de code, ce qui constitue la base de la détection.

**Fonctionnalités principales:**
- Deux méthodes de génération: directe ou par batch
- Analyse de fichiers individuels ou de dossiers complets
- Sélection des modèles de tokenisation et de prédiction
- Options de traitement batch (taille, intervalle de sondage, etc.)
- Gestion des erreurs et des reconnexions
- Console de sortie en temps réel

### 4. Génération des Tuiles

Cet onglet permet de découper les matrices générées en tuiles plus petites pour faciliter l'entraînement du modèle de détection.

**Fonctionnalités principales:**
- Sélection du dossier de matrices
- Configuration de la taille des tuiles (lignes et colonnes)
- Gestion automatique du padding
- Visualisation des métadonnées des tuiles générées

### 5. Entraînement U-Net

Cet onglet permet d'entraîner le modèle de détection (U-Net ou ResNet) sur les tuiles ou matrices générées.

**Fonctionnalités principales:**
- Choix entre entraînement sur tuiles ou matrices complètes
- Sélection du type de modèle (UNet ou ResNet)
- Configuration des hyperparamètres d'entraînement
- Options de normalisation et de redimensionnement
- Visualisation des courbes d'apprentissage en temps réel
- Early stopping et stratification des données
- Équilibrage des classes

### 6. Test U-Net

Cet onglet permet d'évaluer les performances du modèle entraîné et de l'utiliser pour détecter si un code est généré par IA ou écrit par un humain.

**Fonctionnalités principales:**
- Analyse de fichiers individuels ou de dossiers
- Visualisation des résultats de détection
- Affichage des scores de confiance
- Statistiques globales sur les analyses
- Options de visualisation des tuiles et des activations
- Interface glisser-déposer

### 7. Visualisation

Cet onglet permet de visualiser les matrices générées et les activations du modèle pour mieux comprendre le processus de détection.

**Fonctionnalités principales:**
- Visualisation des matrices brutes (heatmap ou catégorique)
- Visualisation des activations du modèle
- Options de sauvegarde des visualisations
- Configuration des paramètres d'affichage

## Workflow typique

1. **Génération de données d'entraînement**:
   - Utiliser l'onglet "Génération de Code IA" pour créer un ensemble de scripts Python générés par IA
   - Utiliser l'onglet "Récupération de Batches" pour récupérer les résultats

2. **Création des matrices**:
   - Utiliser l'onglet "Génération des Matrices" pour créer des matrices de log-probabilités à partir des scripts
   - Utiliser l'onglet "Génération des Tuiles" pour découper les matrices en tuiles

3. **Entraînement et évaluation**:
   - Utiliser l'onglet "Entraînement U-Net" pour entraîner le modèle de détection
   - Utiliser l'onglet "Test U-Net" pour évaluer les performances

4. **Analyse**:
   - Utiliser l'onglet "Visualisation" pour comprendre les patterns détectés

## Notes techniques

- L'application utilise PyQt5 pour l'interface graphique
- Le traitement des matrices est réalisé à l'aide de NumPy
- Les modèles de détection sont implémentés avec PyTorch
- Les requêtes à l'API OpenAI utilisent la bibliothèque officielle OpenAI

## Contribution

Les contributions sont les bienvenues. Veuillez consulter le fichier CONTRIBUTING.md pour plus d'informations.

## Licence

Ce projet est sous licence MIT.
