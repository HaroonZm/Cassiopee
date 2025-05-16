#!/usr/bin/env python3
"""
Script flexible pour le traitement de datasets de code Python avec l'API OpenAI.
Prend en charge deux types de datasets et deux modes d'API (Batch avec 50% d'économie, ou synchrone standard).
"""

import os
import time
import json
import uuid
import argparse
import logging
import random
import tempfile
from pathlib import Path
from openai import OpenAI

# ==============================================
# CONFIGURATION : ENTREZ VOTRE CLÉ API ICI
# ==============================================
# Remplacez None par votre clé API OpenAI entre guillemets
# Exemple: OPENAI_API_KEY = "sk-votreCleFournieParOpenAI"
OPENAI_API_KEY = "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"
# ==============================================

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("flexible_batch_processor.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Définition des templates de prompts pour les reformulations
REFORM_TEMPLATES = {
    # Styles de programmation
    "style_functional": "Réécris ce code Python en utilisant un style fonctionnel sans effets secondaires. Évite les variables mutables et privilégie les fonctions pures. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "style_oop": "Réécris ce code Python en utilisant une approche orientée objet avec des classes appropriées. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "style_procedural": "Réécris ce code Python en utilisant une approche procédurale, étape par étape. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Niveau d'expertise
    "expertise_beginner": "Réécris ce code Python comme si tu étais un programmeur débutant, avec une structure simple mais fonctionnelle. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "expertise_advanced": "Réécris ce code Python comme si tu étais un expert Python, en utilisant des fonctionnalités avancées du langage et des optimisations. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Documentation et lisibilité
    "docs_none": "Réécris ce code Python sans aucun commentaire ni docstring. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "docs_detailed": "Réécris ce code Python avec des commentaires détaillés expliquant chaque section et des docstrings complètes pour toutes les fonctions. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "format_verbose": "Réécris ce code Python avec des noms de variables très explicites et une structure espacée pour maximiser la lisibilité. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Signatures typiques d'IA (NOUVEAUX)
    "ai_complex_simple": "Réécris ce code Python avec des solutions élégantes mais inutilement complexes pour des problèmes simples. Préfère l'ingéniosité à la lisibilité. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "ai_naming_patterns": "Réécris ce code Python en utilisant des patterns de nommage extrêmement cohérents et systématiques (comme data_manager, data_processor, data_validator). Renvoie uniquement le code brut sans délimiteurs markdown.",
    "ai_overexplained": "Réécris ce code Python avec des commentaires excessivement détaillés expliquant même les concepts évidents et basiques. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Variété d'idiomes (NOUVEAUX)
    "idiom_avoid_pythonic": "Réécris ce code Python en évitant délibérément les idiomes Python courants et en préférant des approches plus verbales et explicites. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "idiom_overuse_comprehensions": "Réécris ce code Python en utilisant excessivement les compréhensions de liste/dictionnaire, même quand une approche plus simple serait plus appropriée. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "idiom_latest_features": "Réécris ce code Python en surchargeant le code avec des fonctionnalités Python récentes (3.10+) comme les pattern matching, les unions de types, etc. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Variations structurelles (NOUVEAUX)
    "structure_fragmented": "Réécris ce code Python en le fragmentant en de nombreuses petites fonctions, même quand cela rend le code plus complexe à suivre. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "structure_flat": "Réécris ce code Python avec une structure excessivement plate, en minimisant les fonctions et en préférant des blocs de code linéaires. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "structure_perfect_format": "Réécris ce code Python avec une indentation et un formatage parfaitement cohérents, comme si le code avait été généré par une machine. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Anti-détection (NOUVEAUX)
    "stealth_human_like": "Réécris ce code Python pour qu'il ressemble à du code écrit par un humain, avec de légères incohérences de style, quelques commentaires personnels et potentiellement quelques imperfections mineures. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "stealth_mixed_style": "Réécris ce code Python en mélangeant délibérément plusieurs styles de programmation pour éviter les patterns trop cohérents. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "stealth_quirky": "Réécris ce code Python avec quelques choix de conception non-conventionnels qui seraient typiques d'un développeur avec des préférences personnelles particulières. Renvoie uniquement le code brut sans délimiteurs markdown.",
}

# Templates pour générer du code depuis zéro à partir d'un énoncé (uniquement pour CodeNet)
GENERATION_TEMPLATES = {
    "standard": "Crée une solution complète en Python pour ce problème. Sois concis et efficace. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "detailed": "Crée une solution complète en Python pour ce problème avec des commentaires détaillés expliquant ton approche. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "optimized": "Crée la solution la plus optimisée possible en Python pour ce problème, en tenant compte de la complexité temporelle et spatiale. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Nouveaux templates de génération
    "gen_beginner_style": "Crée une solution en Python pour ce problème comme le ferait un programmeur débutant, avec une approche simple et directe, possiblement non-optimale. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "gen_over_engineered": "Crée une solution excessivement sophistiquée en Python pour ce problème, avec des abstractions peut-être superflues comme si tu anticipais de futures extensions même pour cette tâche simple. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "gen_minimalist": "Crée la solution la plus minimaliste et concise possible en Python pour ce problème, en utilisant le moins de lignes possible, même au détriment de la lisibilité. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "gen_production_ready": "Crée une solution robuste et prête pour la production pour ce problème, avec gestion des erreurs exhaustive, validation des entrées et journalisation appropriée. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "gen_human_like": "Crée une solution Python pour ce problème qui semble avoir été écrite par un humain, avec quelques commentaires personnels, peut-être une ou deux approches non-optimales et un style légèrement incohérent. Renvoie uniquement le code brut sans délimiteurs markdown.",
}

class BatchRequestItem:
    """Classe représentant une requête pour le traitement par lots"""
    
    def __init__(self, custom_id, prompt_template, content, metadata=None):
        """
        Initialise une requête batch.
        
        Args:
            custom_id (str): Identifiant unique pour cette requête
            prompt_template (str): Template de prompt à utiliser
            content (str): Contenu à traiter (code Python ou énoncé)
            metadata (dict, optional): Métadonnées associées à cette requête
        """
        self.custom_id = custom_id
        self.prompt_template = prompt_template
        self.content = content
        self.metadata = metadata or {}
    
    def to_jsonl(self):
        """Convertit la requête en format JSONL pour l'API Batch"""
        # Construire le système et le message utilisateur
        system_message = "Tu es un expert en Python chargé de reformuler ou générer du code selon des instructions spécifiques. Le code généré doit être fonctionnel et respecter les contraintes demandées."
        user_message = f"{self.prompt_template}\n\n{self.content}"
        
        # Créer la requête Batch
        batch_request = {
            "custom_id": self.custom_id,
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "gpt-4.1-mini",
                "messages": [
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                "max_tokens": 4096
            }
        }
        
        return json.dumps(batch_request)

class FlexibleBatchProcessor:
    """Processeur flexible pour les datasets de code Python"""
    
    def __init__(self, input_path, output_path, api_key=None, poll_interval=60, batch_size=1000, use_batch=True):
        """
        Initialise le processeur flexible.
        
        Args:
            input_path (str): Chemin vers le dataset d'entrée
            output_path (str): Chemin de sortie pour les fichiers générés
            api_key (str, optional): Clé API OpenAI. Par défaut, utilise la variable définie dans le script.
            poll_interval (int): Intervalle en secondes entre chaque vérification de l'état du batch
            batch_size (int): Taille maximale d'un lot de requêtes (max 50000)
            use_batch (bool): Utiliser l'API Batch (True) ou des appels synchrones (False)
        """
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.poll_interval = poll_interval
        self.batch_size = min(batch_size, 50000)  # OpenAI limite à 50000 requêtes par batch
        self.use_batch = use_batch
        
        # Initialiser le client OpenAI
        if OPENAI_API_KEY:
            self.client = OpenAI(api_key=OPENAI_API_KEY)
        elif api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            env_api_key = os.environ.get("OPENAI_API_KEY")
            if not env_api_key:
                raise ValueError("Aucune clé API OpenAI trouvée. Définissez-la dans le script, passez-la en paramètre ou utilisez la variable d'environnement OPENAI_API_KEY.")
            self.client = OpenAI(api_key=env_api_key)
        
        # Déterminer le type de dataset
        self.dataset_type = self._detect_dataset_type()
        logger.info(f"Type de dataset détecté: {self.dataset_type}")
        
        # Créer le répertoire de métadonnées
        self.metadata_dir = self.output_path / "metadata"
        self.metadata_dir.mkdir(parents=True, exist_ok=True)
        
        # Fichier de métadonnées global
        self.global_metadata_file = self.metadata_dir / "dataset_metadata.jsonl"
        if not self.global_metadata_file.exists():
            with open(self.global_metadata_file, 'w') as f:
                f.write('')
        
        # Statistiques
        self.stats = {
            "files_processed": 0,
            "problems_processed": 0,
            "variations_generated": 0,
            "solutions_from_scratch": 0,
            "batches_submitted": 0,
            "batches_completed": 0,
            "api_calls": 0,
            "api_errors": 0,
            "file_errors": 0
        }
    
    def _detect_dataset_type(self):
        """
        Détecte automatiquement le type de dataset à partir de sa structure.
        
        Returns:
            str: "codenet" pour le format CodeNet traditionnel avec énoncés,
                 "code_only" pour un dataset contenant uniquement des fichiers Python
        """
        # Vérifier s'il y a des fichiers prompt.txt (format CodeNet)
        prompt_files = list(self.input_path.glob("**/prompt.txt"))
        if prompt_files:
            return "codenet"
        
        # Vérifier s'il y a des fichiers .py (format code uniquement)
        python_files = list(self.input_path.glob("**/*.py"))
        if python_files:
            return "code_only"
        
        # Si aucun des deux formats n'est détecté, lever une exception
        raise ValueError(f"Impossible de détecter le type de dataset dans {self.input_path}. Aucun fichier prompt.txt ou .py trouvé.")
    
    def create_directories(self, path):
        """Crée les répertoires nécessaires s'ils n'existent pas déjà."""
        path.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Répertoire vérifié: {path}")
    
    def read_file(self, file_path):
        """Lit le contenu d'un fichier."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except UnicodeDecodeError:
            # Essayer avec une autre encodage si utf-8 échoue
            try:
                with open(file_path, 'r', encoding='latin-1') as file:
                    return file.read()
            except Exception as e:
                logger.error(f"Erreur lors de la lecture du fichier {file_path} avec l'encodage latin-1: {e}")
                self.stats["file_errors"] += 1
                return None
        except Exception as e:
            logger.error(f"Erreur lors de la lecture du fichier {file_path}: {e}")
            self.stats["file_errors"] += 1
            return None
    
    def write_file(self, file_path, content):
        """Écrit le contenu dans un fichier."""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            logger.debug(f"Fichier écrit: {file_path}")
            return True
        except Exception as e:
            logger.error(f"Erreur lors de l'écriture du fichier {file_path}: {e}")
            self.stats["file_errors"] += 1
            return False
    
    def append_metadata(self, metadata):
        """Ajoute une entrée de métadonnées au fichier global."""
        try:
            with open(self.global_metadata_file, 'a') as f:
                f.write(json.dumps(metadata) + '\n')
            return True
        except Exception as e:
            logger.error(f"Erreur lors de l'écriture des métadonnées: {e}")
            return False
    
    def clean_code_response(self, response):
        """
        Nettoie la réponse de l'API en retirant les délimiteurs de code Markdown.
        
        Args:
            response (str): Réponse de l'API
            
        Returns:
            str: Code nettoyé
        """
        if not response:
            return response
        
        # Supprimer les délimiteurs Markdown ```python et ```
        response = response.strip()
        
        # Cas 1: Code entouré de ```python ... ```
        if response.startswith("```python") and response.endswith("```"):
            response = response[len("```python"):].strip()
            response = response[:-3].strip()
        # Cas 2: Code entouré simplement de ``` ... ```
        elif response.startswith("```") and response.endswith("```"):
            response = response[3:].strip()
            response = response[:-3].strip()
        # Cas 3: Vérifier si le code commence par ```python mais ne se termine pas exactement par ```
        elif response.startswith("```python"):
            lines = response.split("\n")
            if len(lines) > 1:
                lines = lines[1:]  # Supprimer la première ligne contenant ```python
                # Rechercher la dernière ligne contenant ``` et la supprimer
                for i in range(len(lines)-1, -1, -1):
                    if lines[i].strip() == "```":
                        lines.pop(i)
                        break
                response = "\n".join(lines)
        # Cas 4: Vérifier si le code commence par ``` mais ne se termine pas exactement par ```
        elif response.startswith("```"):
            lines = response.split("\n")
            if len(lines) > 1:
                lines = lines[1:]  # Supprimer la première ligne contenant ```
                # Rechercher la dernière ligne contenant ``` et la supprimer
                for i in range(len(lines)-1, -1, -1):
                    if lines[i].strip() == "```":
                        lines.pop(i)
                        break
                response = "\n".join(lines)
        
        return response
    
    def create_batch_file(self, requests):
        """
        Crée un fichier temporaire JSONL pour les requêtes batch.
        
        Args:
            requests (list): Liste de BatchRequestItem
            
        Returns:
            str: Chemin du fichier temporaire créé
        """
        # Créer un fichier temporaire
        fd, temp_path = tempfile.mkstemp(suffix='.jsonl')
        os.close(fd)
        
        # Écrire les requêtes dans le fichier JSONL
        with open(temp_path, 'w', encoding='utf-8') as f:
            for request in requests:
                f.write(request.to_jsonl() + '\n')
        
        logger.info(f"Fichier batch créé: {temp_path} avec {len(requests)} requêtes")
        return temp_path
    
    def submit_batch(self, requests):
        """
        Soumet un lot de requêtes à l'API Batch d'OpenAI.
        
        Args:
            requests (list): Liste de BatchRequestItem
            
        Returns:
            tuple: (batch_id, requests_map) ou (None, None) en cas d'erreur
        """
        try:
            # Créer le fichier de requêtes
            batch_file_path = self.create_batch_file(requests)
            
            # Télécharger le fichier
            logger.info(f"Téléchargement du fichier batch avec {len(requests)} requêtes...")
            with open(batch_file_path, 'rb') as f:
                file = self.client.files.create(
                    file=f,
                    purpose="batch"
                )
            
            # Créer le batch
            logger.info(f"Création du batch avec le fichier {file.id}...")
            batch = self.client.batches.create(
                input_file_id=file.id,
                endpoint="/v1/chat/completions",
                completion_window="24h"
            )
            
            # Sauvegarder les métadonnées du batch
            batch_info = {
                "batch_id": batch.id,
                "status": batch.status,
                "created_at": batch.created_at,
                "request_counts": {
                    "total": batch.request_counts.total if batch.request_counts else 0
                },
                "custom_ids": [req.custom_id for req in requests]
            }
            
            batch_file = self.metadata_dir / f"batch_{batch.id}.json"
            with open(batch_file, 'w') as f:
                json.dump(batch_info, f, indent=2)
            
            # Sauvegarder les détails des requêtes
            requests_map = {req.custom_id: req.metadata for req in requests}
            requests_file = self.metadata_dir / f"requests_{batch.id}.json"
            with open(requests_file, 'w') as f:
                json.dump(requests_map, f, indent=2)
            
            # Supprimer le fichier temporaire
            os.unlink(batch_file_path)
            
            self.stats["batches_submitted"] += 1
            logger.info(f"Batch soumis avec succès: {batch.id}")
            
            return batch.id, requests_map
            
        except Exception as e:
            logger.error(f"Erreur lors de la soumission du batch: {e}")
            self.stats["api_errors"] += 1
            
            # Nettoyer le fichier temporaire en cas d'erreur
            if 'batch_file_path' in locals() and os.path.exists(batch_file_path):
                os.unlink(batch_file_path)
                
            return None, None
    
    def poll_batch_status(self, batch_id):
        """
        Vérifie périodiquement l'état du batch jusqu'à ce qu'il soit terminé.
        
        Args:
            batch_id (str): ID du batch à vérifier
            
        Returns:
            dict: Objet Batch final ou None en cas d'erreur
        """
        try:
            logger.info(f"Vérification de l'état du batch {batch_id}...")
            
            while True:
                batch = self.client.batches.retrieve(batch_id)
                status = batch.status
                
                requests_completed = batch.request_counts.completed if batch.request_counts else 0
                requests_total = batch.request_counts.total if batch.request_counts else 0
                
                logger.info(f"Batch {batch_id} - État: {status} - Terminé: {requests_completed}/{requests_total}")
                
                if status == "completed":
                    self.stats["batches_completed"] += 1
                    return batch
                elif status in ["failed", "expired", "cancelled"]:
                    logger.error(f"Batch {batch_id} a échoué avec le statut {status}")
                    return batch
                
                # Attendre avant la prochaine vérification
                time.sleep(self.poll_interval)
                
        except Exception as e:
            logger.error(f"Erreur lors de la vérification du batch {batch_id}: {e}")
            return None
    
    def process_batch_results(self, batch):
        """
        Traite les résultats d'un batch terminé.
        
        Args:
            batch: Objet Batch
            
        Returns:
            dict: Dictionnaire des résultats par custom_id
        """
        try:
            # Vérifier que le batch est bien terminé
            if batch.status != "completed":
                logger.error(f"Impossible de traiter les résultats: le batch {batch.id} n'est pas terminé (statut: {batch.status})")
                return {}
            
            # Obtenir le fichier de résultats
            logger.info(f"Téléchargement des résultats du batch {batch.id}...")
            output_response = self.client.files.content(batch.output_file_id)
            output_content = output_response.text
            
            # Sauvegarder les résultats bruts
            raw_results_file = self.metadata_dir / f"results_{batch.id}.jsonl"
            with open(raw_results_file, 'w') as f:
                f.write(output_content)
            
            # Obtenir le fichier d'erreurs s'il existe
            if batch.error_file_id:
                logger.warning(f"Le batch {batch.id} a des erreurs. Téléchargement du fichier d'erreurs...")
                error_response = self.client.files.content(batch.error_file_id)
                error_content = error_response.text
                
                error_file = self.metadata_dir / f"errors_{batch.id}.jsonl"
                with open(error_file, 'w') as f:
                    f.write(error_content)
            
            # Traiter les résultats
            results = {}
            for line in output_content.strip().split('\n'):
                result = json.loads(line)
                custom_id = result.get("custom_id")
                
                if result.get("error"):
                    logger.error(f"Erreur pour la requête {custom_id}: {result['error']}")
                    continue
                
                # Extraire la réponse
                if result.get("response") and result["response"].get("body"):
                    body = result["response"]["body"]
                    if "choices" in body and len(body["choices"]) > 0:
                        content = body["choices"][0]["message"]["content"]
                        # Nettoyer le code des délimiteurs markdown
                        cleaned_content = self.clean_code_response(content)
                        results[custom_id] = cleaned_content
            
            logger.info(f"Traitement terminé pour le batch {batch.id}: {len(results)} résultats")
            
            # Charger les métadonnées des requêtes
            requests_file = self.metadata_dir / f"requests_{batch.id}.json"
            if requests_file.exists():
                with open(requests_file, 'r') as f:
                    requests_map = json.load(f)
            else:
                requests_map = {}
                logger.warning(f"Fichier de requêtes {requests_file} introuvable.")
            
            # Sauvegarder les résultats dans les fichiers appropriés
            self.save_results_to_files(batch.id, results, requests_map)
            
            return results
            
        except Exception as e:
            logger.error(f"Erreur lors du traitement des résultats du batch {batch.id}: {e}")
            return {}
    
    def process_synchronous(self, requests):
        """
        Traite les requêtes de manière synchrone (sans utiliser l'API Batch).
        
        Args:
            requests (list): Liste de BatchRequestItem
            
        Returns:
            dict: Dictionnaire des résultats par custom_id
        """
        results = {}
        total = len(requests)
        
        logger.info(f"Traitement synchrone de {total} requêtes...")
        
        for i, request in enumerate(requests):
            try:
                logger.info(f"Traitement de la requête {i+1}/{total}: {request.custom_id}")
                
                # Construire le message système et utilisateur
                system_message = "Tu es un expert en Python chargé de reformuler ou générer du code selon des instructions spécifiques. Le code généré doit être fonctionnel et respecter les contraintes demandées."
                user_message = f"{request.prompt_template}\n\n{request.content}"
                
                # Appel API synchrone
                response = self.client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": user_message}
                    ],
                    max_tokens=4096
                )
                
                self.stats["api_calls"] += 1
                
                # Extraire et nettoyer la réponse
                if response and response.choices and len(response.choices) > 0:
                    content = response.choices[0].message.content
                    cleaned_content = self.clean_code_response(content)
                    results[request.custom_id] = cleaned_content
                
                # Ajouter un délai pour éviter les erreurs de rate limit
                if (i+1) % 10 == 0:
                    logger.info(f"Pause pour éviter le rate limit ({i+1}/{total} requêtes traitées)")
                    time.sleep(2)
                
            except Exception as e:
                logger.error(f"Erreur lors du traitement de la requête {request.custom_id}: {e}")
                self.stats["api_errors"] += 1
        
        logger.info(f"Traitement synchrone terminé: {len(results)}/{total} requêtes traitées avec succès")
        
        # Sauvegarder les résultats
        requests_map = {req.custom_id: req.metadata for req in requests}
        self.save_results_to_files("synchronous", results, requests_map)
        
        return results
    
    def save_results_to_files(self, batch_id, results, requests_map):
        """
        Sauvegarde les résultats dans les fichiers appropriés.
        
        Args:
            batch_id (str): ID du batch
            results (dict): Dictionnaire des résultats par custom_id
            requests_map (dict): Dictionnaire des métadonnées des requêtes
            
        Returns:
            int: Nombre de résultats traités avec succès
        """
        processed_count = 0
        
        for custom_id, code in results.items():
            # Récupérer les métadonnées de la requête
            metadata = requests_map.get(custom_id, {})
            
            if not metadata:
                logger.warning(f"Métadonnées non trouvées pour {custom_id}")
                continue
            
            # Déterminer le type de requête
            req_type = metadata.get("type")
            
            if req_type == "reformulation":
                # Traiter les reformulations
                file_path = metadata.get("file_path")
                variation_key = metadata.get("variation_key")
                problem_id = metadata.get("problem_id", "unknown")
                subdirs = metadata.get("subdirs", "")
                
                if not all([file_path, variation_key]):
                    logger.warning(f"Métadonnées incomplètes pour {custom_id}")
                    continue
                
                # Créer le chemin de sortie
                input_path = Path(file_path)
                
                # Construire solution_id en incluant les sous-dossiers si présents
                filename = input_path.name
                if subdirs:
                    solution_id = f"{subdirs}_{filename}"
                else:
                    solution_id = filename
                
                output_dir = self.output_path / problem_id / f"original_{solution_id}"
                output_file = output_dir / f"ai_{variation_key}.py"
                
                # Créer le répertoire de sortie
                self.create_directories(output_dir)
                
                # Sauvegarder l'original si ce n'est pas déjà fait
                original_file = output_dir / "original.py"
                if not original_file.exists() and input_path.exists():
                    original_code = self.read_file(input_path)
                    if original_code:
                        self.write_file(original_file, original_code)
                
                # Sauvegarder le résultat
                if self.write_file(output_file, code):
                    # Ajouter les métadonnées
                    result_metadata = {
                        "file_path": str(file_path),
                        "output_path": str(output_file),
                        "variation_type": variation_key,
                        "problem_id": problem_id,
                        "subdirs": subdirs,
                        "is_reformulation": True,
                        "batch_id": batch_id,
                        "custom_id": custom_id,
                        "timestamp": time.time()
                    }
                    self.append_metadata(result_metadata)
                    
                    processed_count += 1
                    self.stats["variations_generated"] += 1
            
            elif req_type == "generation" and self.dataset_type == "codenet":
                # Traiter les générations depuis zéro (uniquement pour CodeNet)
                problem_id = metadata.get("problem_id")
                template_key = metadata.get("template_key")
                
                if not all([problem_id, template_key]):
                    logger.warning(f"Métadonnées incomplètes pour {custom_id}")
                    continue
                
                # Créer le répertoire de sortie
                output_dir = self.output_path / problem_id / "from_scratch"
                self.create_directories(output_dir)
                
                # Sauvegarder le résultat
                output_file = output_dir / f"ai_generated_{template_key}.py"
                if self.write_file(output_file, code):
                    # Ajouter les métadonnées
                    result_metadata = {
                        "problem_id": problem_id,
                        "generation_type": template_key,
                        "is_generation": True,
                        "output_path": str(output_file),
                        "batch_id": batch_id,
                        "custom_id": custom_id,
                        "timestamp": time.time()
                    }
                    self.append_metadata(result_metadata)
                    
                    processed_count += 1
                    self.stats["solutions_from_scratch"] += 1
        
        logger.info(f"Sauvegarde terminée pour le batch {batch_id}: {processed_count}/{len(results)} résultats traités")
        return processed_count
    
    def collect_codenet_requests(self, problems, variation_limit=3, generation_limit=2, test_mode=False):
        """
        Collecte les requêtes pour le dataset au format CodeNet.
        
        Args:
            problems (list): Liste des ID de problèmes
            variation_limit (int): Nombre maximum de variations par solution
            generation_limit (int): Nombre maximum de solutions générées par problème
            test_mode (bool): Indique si le script est en mode test
            
        Returns:
            list: Liste de BatchRequestItem
        """
        all_requests = []
        
        for problem_id in problems:
            try:
                problem_dir = self.input_path / problem_id
                prompt_path = problem_dir / 'prompt.txt'
                
                if not prompt_path.exists():
                    logger.warning(f"L'énoncé du problème {problem_id} n'existe pas: {prompt_path}")
                    continue
                
                # Lire l'énoncé du problème
                prompt = self.read_file(prompt_path)
                if not prompt:
                    logger.warning(f"L'énoncé du problème {problem_id} n'a pas pu être lu.")
                    continue
                
                # Rechercher toutes les solutions Python existantes
                solutions = list(problem_dir.glob('*.py'))
                solutions = [s for s in solutions if s.name != 'prompt.py']
                
                # En mode test, limiter le nombre de solutions
                if test_mode:
                    if len(solutions) > 2:
                        solutions = solutions[:2]
                    variation_limit = min(variation_limit, 2)
                    generation_limit = min(generation_limit, 2)
                
                # Sélectionner aléatoirement un sous-ensemble de variations pour chaque solution
                available_variations = list(REFORM_TEMPLATES.keys())
                if len(available_variations) > variation_limit:
                    selected_variations = random.sample(available_variations, variation_limit)
                else:
                    selected_variations = available_variations
                
                # Collecter les requêtes pour les variations
                for solution_file in solutions:
                    solution_code = self.read_file(solution_file)
                    if not solution_code:
                        continue
                    
                    for variation_key in selected_variations:
                        custom_id = f"var_{problem_id}_{solution_file.name}_{variation_key}"
                        prompt_template = REFORM_TEMPLATES.get(variation_key)
                        
                        metadata = {
                            "type": "reformulation",
                            "file_path": str(solution_file),
                            "variation_key": variation_key,
                            "problem_id": problem_id
                        }
                        
                        request = BatchRequestItem(custom_id, prompt_template, solution_code, metadata)
                        all_requests.append(request)
                
                # Sélectionner aléatoirement un sous-ensemble de templates de génération
                available_templates = list(GENERATION_TEMPLATES.keys())
                if len(available_templates) > generation_limit:
                    selected_templates = random.sample(available_templates, generation_limit)
                else:
                    selected_templates = available_templates
                
                # Collecter les requêtes pour les générations depuis zéro
                for template_key in selected_templates:
                    custom_id = f"gen_{problem_id}_{template_key}"
                    prompt_template = GENERATION_TEMPLATES.get(template_key)
                    
                    metadata = {
                        "type": "generation",
                        "problem_id": problem_id,
                        "template_key": template_key
                    }
                    
                    request = BatchRequestItem(custom_id, prompt_template, prompt, metadata)
                    all_requests.append(request)
                
                self.stats["problems_processed"] += 1
                
            except Exception as e:
                logger.error(f"Erreur lors de la collecte des requêtes pour le problème {problem_id}: {e}")
        
        return all_requests
    
    def collect_code_only_requests(self, files, variation_limit=3, test_mode=False):
        """
        Collecte les requêtes pour le dataset contenant uniquement des fichiers Python.
        """
        all_requests = []
        
        # En mode test, limiter le nombre de fichiers
        if test_mode and len(files) > 5:
            files = files[:5]
            variation_limit = min(variation_limit, 2)
        
        # Sélectionner aléatoirement un sous-ensemble de variations
        available_variations = list(REFORM_TEMPLATES.keys())
        if len(available_variations) > variation_limit:
            selected_variations = random.sample(available_variations, variation_limit)
        else:
            selected_variations = available_variations
        
        for file_path in files:
            try:
                code = self.read_file(file_path)
                if not code:
                    continue
                
                # Obtenir le chemin relatif pour extraire les sous-dossiers
                relative_path = file_path.relative_to(self.input_path) if file_path.is_relative_to(self.input_path) else file_path.name
                
                # Extraire le premier niveau comme problem_id
                if len(relative_path.parts) > 0:
                    problem_id = relative_path.parts[0]
                    
                    # Capturer tous les sous-dossiers entre le premier niveau et le fichier
                    subdirs = '_'.join(str(part) for part in relative_path.parts[1:-1]) if len(relative_path.parts) > 2 else ""
                else:
                    problem_id = "unknown"
                    subdirs = ""
                
                for variation_key in selected_variations:
                    # Inclure le sous-dossier dans le custom_id pour l'identification
                    if subdirs:
                        custom_id = f"var_{problem_id}_{subdirs}_{file_path.stem}_{uuid.uuid4().hex[:4]}_{variation_key}"
                    else:
                        custom_id = f"var_{problem_id}_{file_path.stem}_{uuid.uuid4().hex[:4]}_{variation_key}"
                    
                    prompt_template = REFORM_TEMPLATES.get(variation_key)
                    
                    metadata = {
                        "type": "reformulation",
                        "file_path": str(file_path),
                        "variation_key": variation_key,
                        "problem_id": problem_id,
                        "subdirs": subdirs
                    }
                    
                    request = BatchRequestItem(custom_id, prompt_template, code, metadata)
                    all_requests.append(request)
                
                self.stats["files_processed"] += 1
                
            except Exception as e:
                logger.error(f"Erreur lors de la collecte des requêtes pour le fichier {file_path}: {e}")
        
        return all_requests
    
    def process_dataset(self, variation_limit=3, generation_limit=2, test_mode=False, problem_limit=None, file_limit=None):
        """
        Traite l'ensemble du dataset.
        
        Args:
            variation_limit (int): Nombre maximum de variations par solution/fichier
            generation_limit (int): Nombre maximum de solutions générées par problème (uniquement pour CodeNet)
            test_mode (bool): Indique si le script est en mode test
            problem_limit (int, optional): Limite le nombre de problèmes à traiter (pour CodeNet)
            file_limit (int, optional): Limite le nombre de fichiers à traiter (pour dataset code uniquement)
            
        Returns:
            dict: Statistiques de traitement
        """
        # Créer le répertoire de sortie principal
        self.create_directories(self.output_path)
        
        all_requests = []
        
        # Traiter le dataset selon son type
        if self.dataset_type == "codenet":
            # Format CodeNet: problème/solution
            problems = [d.name for d in self.input_path.iterdir() 
                      if d.is_dir() and d.name.startswith('p')]
            problems.sort()
            
            # En mode test, ne traiter que le premier problème
            if test_mode and len(problems) > 0:
                problems = [problems[0]]
            
            # Limiter le nombre de problèmes si demandé
            if problem_limit and len(problems) > problem_limit:
                problems = problems[:problem_limit]
            
            logger.info(f"Collecte des requêtes pour {len(problems)} problèmes au format CodeNet...")
            all_requests = self.collect_codenet_requests(problems, variation_limit, generation_limit, test_mode)
            
        else:
            # Format code uniquement: fichiers Python
            python_files = list(self.input_path.glob("**/*.py"))
            
            # Limiter le nombre de fichiers si demandé
            if file_limit and len(python_files) > file_limit:
                python_files = python_files[:file_limit]
            
            logger.info(f"Collecte des requêtes pour {len(python_files)} fichiers Python...")
            all_requests = self.collect_code_only_requests(python_files, variation_limit, test_mode)
        
        logger.info(f"Collecte terminée: {len(all_requests)} requêtes à traiter")
        
        # Traitement selon le mode (batch ou synchrone)
        if self.use_batch:
            # Mode Batch: diviser les requêtes en lots
            batches = []
            for i in range(0, len(all_requests), self.batch_size):
                batch_requests = all_requests[i:i+self.batch_size]
                batches.append(batch_requests)
            
            logger.info(f"Mode Batch: {len(all_requests)} requêtes divisées en {len(batches)} batches")
            
            # Traiter chaque batch
            for i, batch_requests in enumerate(batches):
                logger.info(f"Traitement du batch {i+1}/{len(batches)} avec {len(batch_requests)} requêtes...")
                
                # Soumettre le batch
                batch_id, _ = self.submit_batch(batch_requests)
                if not batch_id:
                    logger.error(f"Échec de la soumission du batch {i+1}/{len(batches)}")
                    continue
                
                # Vérifier l'état du batch jusqu'à ce qu'il soit terminé
                batch = self.poll_batch_status(batch_id)
                if not batch:
                    logger.error(f"Échec du suivi du batch {batch_id}")
                    continue
                
                # Traiter les résultats du batch
                self.process_batch_results(batch)
                
                # Afficher les statistiques intermédiaires
                logger.info(f"Statistiques intermédiaires: {self.stats}")
        else:
            # Mode synchrone: traiter les requêtes une par une
            logger.info(f"Mode synchrone: traitement de {len(all_requests)} requêtes...")
            self.process_synchronous(all_requests)
            logger.info(f"Statistiques finales: {self.stats}")
        
        return self.stats


def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description='Traitement flexible de datasets de code Python avec l\'API OpenAI.')
    parser.add_argument('--input', type=str, required=True, help='Chemin vers le dataset d\'entrée (CodeNet ou dossier de code Python)')
    parser.add_argument('--output', type=str, required=True, help='Chemin de sortie pour les fichiers générés')
    parser.add_argument('--test', action='store_true', help='Activer le mode test (traiter uniquement un petit échantillon)')
    parser.add_argument('--api-key', type=str, help='Clé API OpenAI (par défaut: définie dans le script ou variable d\'environnement)')
    parser.add_argument('--variations', type=int, default=3, help='Nombre de variations à générer par solution/fichier')
    parser.add_argument('--generations', type=int, default=2, help='Nombre de solutions à générer depuis zéro par problème (uniquement pour CodeNet)')
    parser.add_argument('--problems', type=int, help='Limite le nombre de problèmes à traiter (pour CodeNet)')
    parser.add_argument('--files', type=int, help='Limite le nombre de fichiers à traiter (pour dataset code uniquement)')
    parser.add_argument('--poll-interval', type=int, default=60, help='Intervalle en secondes entre chaque vérification de l\'état du batch')
    parser.add_argument('--batch-size', type=int, default=1000, help='Taille maximale d\'un lot de requêtes (max 50000)')
    parser.add_argument('--no-batch', action='store_true', help='Désactiver l\'API Batch et utiliser des appels synchrones standard')
    
    args = parser.parse_args()
    
    logger.info("=== Démarrage du processus de traitement de code Python ===")
    logger.info(f"Mode test: {'Activé' if args.test else 'Désactivé'}")
    logger.info(f"Mode API: {'Synchrone (standard)' if args.no_batch else 'Batch (50% moins cher)'}")
    logger.info(f"Chemin d'entrée: {args.input}")
    logger.info(f"Chemin de sortie: {args.output}")
    logger.info(f"Variations par solution/fichier: {args.variations}")
    logger.info(f"Générations par problème (CodeNet uniquement): {args.generations}")
    
    try:
        processor = FlexibleBatchProcessor(
            input_path=args.input,
            output_path=args.output,
            api_key=args.api_key,
            poll_interval=args.poll_interval,
            batch_size=args.batch_size,
            use_batch=not args.no_batch
        )
        
        stats = processor.process_dataset(
            variation_limit=args.variations,
            generation_limit=args.generations,
            test_mode=args.test,
            problem_limit=args.problems,
            file_limit=args.files
        )
        
        logger.info("=== Processus terminé ===")
        logger.info(f"Statistiques finales:")
        
        if processor.dataset_type == "codenet":
            logger.info(f"  - Problèmes traités: {stats['problems_processed']}")
            logger.info(f"  - Variations générées: {stats['variations_generated']}")
            logger.info(f"  - Solutions générées depuis zéro: {stats['solutions_from_scratch']}")
        else:
            logger.info(f"  - Fichiers traités: {stats['files_processed']}")
            logger.info(f"  - Variations générées: {stats['variations_generated']}")
        
        if not args.no_batch:
            logger.info(f"  - Batches soumis: {stats['batches_submitted']}")
            logger.info(f"  - Batches terminés: {stats['batches_completed']}")
        else:
            logger.info(f"  - Appels API: {stats['api_calls']}")
        
        logger.info(f"  - Erreurs API: {stats['api_errors']}")
        logger.info(f"  - Erreurs fichier: {stats['file_errors']}")
        
    except Exception as e:
        logger.error(f"Erreur critique: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())