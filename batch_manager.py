#!/usr/bin/env python3
"""
Gestionnaire simple pour les batchs OpenAI.
Ce script permet de lister, vérifier l'état et récupérer les résultats des batchs OpenAI.
"""

import os
import time
import json
import argparse
import logging
from pathlib import Path
from openai import OpenAI

OPENAI_API_KEY="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"

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("simple_batch_manager.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SimpleBatchManager:
    """Gestionnaire simple pour les batchs OpenAI"""
    
    def __init__(self, api_key=None, output_dir="detector_dataset"):
        """
        Initialise le gestionnaire de batch simple.
        
        Args:
            api_key (str, optional): Clé API OpenAI. Par défaut, utilise la clé définie dans le script.
            output_dir (str): Répertoire de sortie pour les résultats
        """
        # Priorité: clé dans le script > argument > variable d'environnement
        if OPENAI_API_KEY is not None:
            self.client = OpenAI(api_key=OPENAI_API_KEY)
        elif api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            env_api_key = os.environ.get("OPENAI_API_KEY")
            if not env_api_key:
                raise ValueError("Aucune clé API OpenAI trouvée.")
            self.client = OpenAI(api_key=env_api_key)
        
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def list_batches(self, limit=100):
        """
        Liste tous les batchs disponibles via l'API.
        
        Args:
            limit (int): Nombre maximum de batchs à récupérer
            
        Returns:
            list: Liste des batchs
        """
        try:
            print(f"Récupération des batchs depuis l'API OpenAI (limite: {limit})...")
            batches = []
            
            # Utilisation directe de l'itérateur de l'API
            for batch in self.client.batches.list(limit=limit):
                batches.append(batch)
            
            print(f"Trouvé {len(batches)} batchs.")
            return batches
        
        except Exception as e:
            logger.error(f"Erreur lors de la récupération des batchs: {e}")
            return []
    
    def get_batch(self, batch_id):
        """
        Récupère les informations d'un batch spécifique.
        
        Args:
            batch_id (str): ID du batch
            
        Returns:
            Batch: Objet Batch ou None en cas d'erreur
        """
        try:
            return self.client.batches.retrieve(batch_id)
        except Exception as e:
            logger.error(f"Erreur lors de la récupération du batch {batch_id}: {e}")
            return None
    
    def clean_code_response(self, response):
        """Nettoie la réponse de l'API en retirant les délimiteurs de code Markdown."""
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
    
    def get_batch_results(self, batch_id, save_raw=False):
        """
        Récupère les résultats d'un batch.
        
        Args:
            batch_id (str): ID du batch
            save_raw (bool): Indique s'il faut sauvegarder les résultats bruts
            
        Returns:
            dict: Dictionnaire des résultats par custom_id
        """
        batch = self.get_batch(batch_id)
        if not batch:
            print(f"Batch {batch_id} introuvable.")
            return {}
        
        if batch.status != "completed":
            print(f"Le batch {batch_id} n'est pas terminé (statut: {batch.status}).")
            return {}
        
        output_file_id = batch.output_file_id
        if not output_file_id:
            print(f"Aucun fichier de sortie trouvé pour le batch {batch_id}.")
            return {}
        
        try:
            # Télécharger le fichier de résultats
            print(f"Téléchargement des résultats du batch {batch_id}...")
            output_response = self.client.files.content(output_file_id)
            output_content = output_response.text
            
            # Sauvegarder les résultats bruts si demandé
            if save_raw:
                raw_dir = self.output_dir / "raw_results"
                raw_dir.mkdir(parents=True, exist_ok=True)
                raw_file = raw_dir / f"{batch_id}_results.jsonl"
                with open(raw_file, 'w') as f:
                    f.write(output_content)
                print(f"Résultats bruts sauvegardés dans {raw_file}")
            
            # Traiter les résultats
            results = {}
            for line in output_content.strip().split('\n'):
                if not line.strip():
                    continue
                
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
            
            print(f"Traitement terminé: {len(results)} résultats extraits.")
            return results
            
        except Exception as e:
            logger.error(f"Erreur lors du traitement des résultats: {e}")
            return {}
    
    def save_results(self, batch_id, results, output_dir=None):
        """
        Sauvegarde les résultats dans des fichiers individuels.
        
        Args:
            batch_id (str): ID du batch
            results (dict): Dictionnaire des résultats par custom_id
            output_dir (str, optional): Répertoire de sortie personnalisé
            
        Returns:
            int: Nombre de fichiers sauvegardés
        """
        if not results:
            print("Aucun résultat à sauvegarder.")
            return 0
        
        # Utiliser le répertoire de sortie personnalisé s'il est spécifié
        save_dir = Path(output_dir) if output_dir else self.output_dir / "results" / batch_id
        save_dir.mkdir(parents=True, exist_ok=True)
        
        saved_count = 0
        for custom_id, content in results.items():
            # Créer un nom de fichier basé sur le custom_id
            filename = f"{custom_id}.py"
            file_path = save_dir / filename
            
            # Sauvegarder le contenu
            with open(file_path, 'w') as f:
                f.write(content)
            
            saved_count += 1
        
        print(f"Sauvegarde terminée: {saved_count} fichiers sauvegardés dans {save_dir}")
        return saved_count


def command_list(args):
    """Commande pour lister les batchs"""
    manager = SimpleBatchManager(args.api_key, args.output)
    batches = manager.list_batches(args.limit)
    
    if not batches:
        print("Aucun batch trouvé.")
        return
    
    print("\nListe des batchs:")
    print("================\n")
    
    for i, batch in enumerate(batches):
        print(f"{i+1}. ID: {batch.id}")
        print(f"   Status: {batch.status}")
        print(f"   Créé le: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(batch.created_at))}")
        
        if batch.request_counts:
            total = batch.request_counts.total
            completed = batch.request_counts.completed
            failed = batch.request_counts.failed
            print(f"   Requêtes: {completed}/{total} terminées, {failed} échouées")
        
        print()

def command_status(args):
    """Commande pour vérifier l'état d'un batch"""
    manager = SimpleBatchManager(args.api_key, args.output)
    batch = manager.get_batch(args.batch_id)
    
    if not batch:
        print(f"Batch {args.batch_id} introuvable.")
        return
    
    print(f"\nBatch: {batch.id}")
    print(f"Status: {batch.status}")
    print(f"Créé le: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(batch.created_at))}")
    
    if batch.completed_at:
        print(f"Terminé le: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(batch.completed_at))}")
    
    if batch.request_counts:
        total = batch.request_counts.total
        completed = batch.request_counts.completed
        failed = batch.request_counts.failed
        print(f"Requêtes: {completed}/{total} terminées, {failed} échouées")
    
    if batch.output_file_id:
        print(f"Fichier de sortie: {batch.output_file_id}")
    
    if batch.error_file_id:
        print(f"Fichier d'erreurs: {batch.error_file_id}")
    
    if batch.status == "completed":
        print("\nLe batch est terminé et prêt à être récupéré.")
    elif batch.status in ["failed", "expired", "cancelled"]:
        print(f"\nLe batch a échoué avec le statut {batch.status}.")
    else:
        print(f"\nLe batch est en cours de traitement ({batch.status}).")

def command_fetch(args):
    """Commande pour récupérer les résultats d'un batch"""
    manager = SimpleBatchManager(args.api_key, args.output)
    
    # Vérifier l'état du batch
    batch = manager.get_batch(args.batch_id)
    if not batch:
        print(f"Batch {args.batch_id} introuvable.")
        return
    
    if batch.status != "completed" and not args.force:
        print(f"Le batch {args.batch_id} n'est pas terminé (statut: {batch.status}).")
        print("Utilisez --force pour récupérer les résultats partiels si disponibles.")
        return
    
    # Récupérer les résultats
    results = manager.get_batch_results(args.batch_id, args.save_raw)
    
    if not results:
        print("Aucun résultat n'a pu être récupéré.")
        return
    
    # Sauvegarder les résultats si demandé
    if args.save:
        manager.save_results(args.batch_id, results, args.destination)

def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description='Gestionnaire simple pour les batchs OpenAI')
    
    # Parent parser pour les arguments communs
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--api-key', type=str, help='Clé API OpenAI')
    parent_parser.add_argument('--output', type=str, default='detector_dataset', help='Répertoire de base')
    
    # Sous-parseurs pour les différentes commandes
    subparsers = parser.add_subparsers(dest='command', help='Commande à exécuter')
    
    # Commande 'list'
    list_parser = subparsers.add_parser('list', help='Liste tous les batchs', parents=[parent_parser])
    list_parser.add_argument('--limit', type=int, default=100, help='Nombre maximum de batchs à récupérer')
    list_parser.set_defaults(func=command_list)
    
    # Commande 'status'
    status_parser = subparsers.add_parser('status', help='Vérifie l\'état d\'un batch', parents=[parent_parser])
    status_parser.add_argument('batch_id', help='ID du batch à vérifier')
    status_parser.set_defaults(func=command_status)
    
    # Commande 'fetch'
    fetch_parser = subparsers.add_parser('fetch', help='Récupère les résultats d\'un batch', parents=[parent_parser])
    fetch_parser.add_argument('batch_id', help='ID du batch à récupérer')
    fetch_parser.add_argument('--force', action='store_true', help='Force la récupération même si le batch n\'est pas terminé')
    fetch_parser.add_argument('--save', action='store_true', help='Sauvegarde les résultats dans des fichiers')
    fetch_parser.add_argument('--save-raw', action='store_true', help='Sauvegarde les résultats bruts')
    fetch_parser.add_argument('--destination', type=str, help='Répertoire de destination pour les résultats')
    fetch_parser.set_defaults(func=command_fetch)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        args.func(args)
    except Exception as e:
        logger.error(f"Erreur: {e}")
        print(f"Une erreur s'est produite: {e}")

if __name__ == "__main__":
    main()
