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
from .config import config, TBATCH_PREFIX, IABATCH_PREFIX

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("batch_manager.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SimpleBatchManager:
    """Gestionnaire simple pour les batchs OpenAI"""
    
    def __init__(self, api_key=None):
        """
        Initialise le gestionnaire de batch simple.
        
        Args:
            api_key (str, optional): Clé API OpenAI. Par défaut, utilise la clé définie dans la config.
        """
        # Initialiser le client OpenAI
        if api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            env_api_key = os.environ.get("OPENAI_API_KEY")
            if not env_api_key:
                raise ValueError("Aucune clé API OpenAI trouvée.")
            self.client = OpenAI(api_key=env_api_key)
    
    def get_batch_directory(self, batch_id):
        """
        Détermine le répertoire approprié pour un batch donné.
        
        Args:
            batch_id (str): ID du batch
            
        Returns:
            Path: Chemin du répertoire approprié
        """
        return config.get_batch_path(batch_id)
    
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
            batch = self.client.batches.retrieve(batch_id)
            return batch
        except Exception as e:
            logger.error(f"Erreur lors de la récupération du batch {batch_id}: {e}")
            return None
    
    def get_batch_results(self, batch_id):
        """
        Récupère les résultats d'un batch.
        
        Args:
            batch_id (str): ID du batch
            
        Returns:
            dict: Résultats du batch
        """
        batch = self.get_batch(batch_id)
        if not batch:
            logger.error(f"Batch {batch_id} introuvable.")
            return {}
        
        if batch.status != "completed":
            logger.warning(f"Le batch {batch_id} n'est pas terminé (statut: {batch.status}).")
            return {}
        
        try:
            # Télécharger et traiter les résultats
            output_response = self.client.files.content(batch.output_file_id)
            results = self._process_batch_results(output_response)
            
            # Sauvegarder les métadonnées
            self._save_metadata(batch_id, batch)
            
            return results
            
        except Exception as e:
            logger.error(f"Erreur lors de la récupération des résultats: {e}")
            return {}
    
    def _process_batch_results(self, response):
        """Traite les résultats bruts du batch"""
        results = {}
        try:
            for line in response.splitlines():
                if not line.strip():
                    continue
                    
                data = json.loads(line)
                custom_id = data.get("custom_id")
                if not custom_id:
                    continue
                
                content = self.clean_code_response(data.get("content", ""))
                alternatives = []
                
                if "alternatives" in data:
                    for alt in data["alternatives"]:
                        alternatives.append({
                            "token": alt.get("token", ""),
                            "logprob": alt.get("logprob", -100)
                        })
                
                results[custom_id] = {
                    "content": content,
                    "alternatives": alternatives
                }
            
            return results
            
        except Exception as e:
            logger.error(f"Erreur lors du traitement des résultats: {e}")
            return {}
    
    def _save_metadata(self, batch_id, batch):
        """Sauvegarde les métadonnées d'un batch"""
        metadata = {
            "id": batch_id,
            "status": batch.status,
            "created_at": str(batch.created_at),
            "completed_at": str(getattr(batch, "completed_at", None)),
            "request_counts": {
                "total": batch.request_counts.total,
                "completed": batch.request_counts.completed,
                "pending": batch.request_counts.pending,
                "failed": batch.request_counts.failed
            }
        }
        
        metadata_path = config.get_metadata_path(batch_id)
        with open(metadata_path, "w") as f:
            json.dump(metadata, f, indent=2)
    
    def save_results(self, batch_id, results):
        """
        Sauvegarde les résultats d'un batch.
        
        Args:
            batch_id (str): ID du batch
            results (dict): Résultats à sauvegarder
        """
        # Sauvegarder les résultats
        results_path = config.get_results_path(batch_id)
        with open(results_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Résultats sauvegardés dans {results_path}")
        
        # Si c'est un batch de tokens, sauvegarder aussi par script
        if batch_id.startswith(TBATCH_PREFIX):
            self._save_tokens_by_script(results, batch_id)
    
    def _save_tokens_by_script(self, results, batch_id):
        """Sauvegarde les tokens par script"""
        from collections import defaultdict
        import re
        
        scripts = defaultdict(dict)
        for custom_id, result in results.items():
            m = re.match(r"(.+):(\d+)$", custom_id)
            if not m:
                continue
                
            script_id, token_index = m.group(1), int(m.group(2))
            token_data = {
                "token": result["content"],
                "alternatives": result.get("alternatives", [])
            }
            scripts[script_id][token_index] = token_data
        
        # Sauvegarder chaque script
        save_dir = self.get_batch_directory(batch_id)
        for script_id, tokens_dict in scripts.items():
            tokens = [tokens_dict[i] for i in sorted(tokens_dict)]
            filename = f"{script_id}__{len(tokens)}_tokens.json"
            file_path = save_dir / filename
            
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(tokens, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Tokens sauvegardés pour {script_id} dans {file_path}")
    
    def clean_code_response(self, response):
        """Nettoie la réponse de l'API"""
        if not response:
            return response
            
        response = response.strip()
        
        # Supprimer les délimiteurs Markdown
        if response.startswith("```") and response.endswith("```"):
            response = response[3:-3].strip()
            
            # Supprimer l'indication du langage si présente
            if response.startswith("python\n"):
                response = response[7:].strip()
        
        return response

# Fonctions de commande
def command_list(args):
    """Liste les batchs disponibles"""
    try:
        manager = SimpleBatchManager(api_key=args.api_key)
        batches = manager.list_batches(limit=args.limit)
        
        if not batches:
            print("Aucun batch trouvé.")
            return True
        
        print("\nBatches disponibles:")
        for batch in batches:
            batch_type = "Token Batch" if batch.id.startswith(TBATCH_PREFIX) else \
                        "IA Script Batch" if batch.id.startswith(IABATCH_PREFIX) else \
                        "Batch standard"
            
            print(f"{batch.id} ({batch_type})")
            print(f"  Status: {batch.status}")
            print(f"  Créé le: {batch.created_at}")
            if batch.error_file_id:
                print("  ⚠️ Erreurs détectées")
            print()
        
        return True
        
    except Exception as e:
        logger.error(f"Erreur lors de la liste des batchs: {e}")
        return False

def command_status(args):
    """Vérifie l'état d'un batch"""
    try:
        manager = SimpleBatchManager(api_key=args.api_key)
        batch = manager.get_batch(args.batch_id)
        
        if not batch:
            print(f"Batch {args.batch_id} introuvable.")
            return False
        
        batch_type = "Token Batch" if args.batch_id.startswith(TBATCH_PREFIX) else \
                    "IA Script Batch" if args.batch_id.startswith(IABATCH_PREFIX) else \
                    "Batch standard"
        
        print(f"\nDétails du batch {args.batch_id} ({batch_type}):")
        print(f"Status: {batch.status}")
        print(f"Créé le: {batch.created_at}")
        
        if batch.error_file_id:
            print("⚠️ Des erreurs ont été détectées")
        
        if hasattr(batch, "request_counts"):
            print(f"\nStatistiques des requêtes:")
            print(f"  Total: {batch.request_counts.total}")
            print(f"  Complétées: {batch.request_counts.completed}")
            print(f"  En attente: {batch.request_counts.pending}")
            print(f"  En erreur: {batch.request_counts.failed}")
        
        return True
        
    except Exception as e:
        logger.error(f"Erreur lors de la vérification du batch: {e}")
        return False

def command_fetch(args):
    """Récupère les résultats d'un batch"""
    try:
        manager = SimpleBatchManager(api_key=args.api_key)
        results = manager.get_batch_results(args.batch_id)
        
        if not results:
            print(f"Aucun résultat trouvé pour le batch {args.batch_id}.")
            return False
        
        manager.save_results(args.batch_id, results)
        return True
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération du batch: {e}")
        return False

def main():
    """Point d'entrée principal"""
    parser = argparse.ArgumentParser(description="Gestionnaire de batchs OpenAI")
    parser.add_argument("--api-key", help="Clé API OpenAI")
    
    subparsers = parser.add_subparsers(dest="command", help="Commande à exécuter")
    
    # Commande list
    list_parser = subparsers.add_parser("list", help="Liste les batchs disponibles")
    list_parser.add_argument("--limit", type=int, default=100, help="Nombre maximum de batchs à lister")
    
    # Commande status
    status_parser = subparsers.add_parser("status", help="Vérifie l'état d'un batch")
    status_parser.add_argument("batch_id", help="ID du batch à vérifier")
    
    # Commande fetch
    fetch_parser = subparsers.add_parser("fetch", help="Récupère les résultats d'un batch")
    fetch_parser.add_argument("batch_id", help="ID du batch à récupérer")
    
    args = parser.parse_args()
    
    if args.command == "list":
        success = command_list(args)
    elif args.command == "status":
        success = command_status(args)
    elif args.command == "fetch":
        success = command_fetch(args)
    else:
        parser.print_help()
        success = False
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())