#!/usr/bin/env python3
"""
Gestionnaire simple pour les batchs OpenAI, pour lister, vérifier et récupérer les résultats.
"""

import os
import time
import json
import argparse
import logging
from pathlib import Path
from openai import OpenAI
from datetime import datetime


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
    
    def __init__(self, api_key=None, output_dir="batches"):
        """
        Initialise le gestionnaire de batch simple.
        
        Args:
            api_key (str, optional): Clé API OpenAI. Si non fournie, utilise la variable d'environnement OPENAI_API_KEY.
            output_dir (str): Répertoire de sortie pour les résultats
        """
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("Aucune clé API OpenAI trouvée. Fournissez-la via le paramètre --api-key ou la variable d'environnement OPENAI_API_KEY.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def list_batches(self, limit=100):
        """
        Liste tous les batchs disponibles via l'API.
        
        Args:
            limit (int): Nombre maximum de batchs à récupérer au total.
            
        Returns:
            list: Liste des batchs
        """
        try:
            print(f"Récupération des batchs depuis l'API OpenAI (limite: {limit})...")
            
            all_batches = []
            # L'itérateur gère la pagination automatiquement.
            # On utilise limit=100 pour la taille de page (le max) pour être efficace.
            for batch in self.client.batches.list(limit=100):
                all_batches.append(batch)
                if len(all_batches) >= limit:
                    break
            
            print(f"Trouvé {len(all_batches)} batchs.")
            return all_batches
        
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
    
    def find_by_date(self, start_date_str, end_date_str, limit=1000):
        """
        Trouve les lots dans une plage de dates donnée.
        """
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").timestamp()
            end_date = datetime.strptime(end_date_str + " 23:59:59", "%Y-%m-%d %H:%M:%S").timestamp()
        except ValueError:
            logger.error("Format de date invalide. Utilisez YYYY-MM-DD.")
            return []

        all_batches = self.list_batches(limit=limit)
        
        found_batches = []
        for batch in all_batches:
            if start_date <= batch.created_at <= end_date:
                found_batches.append(batch)
        
        return found_batches
    
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
        Retourne un dict custom_id -> {'content': ..., 'alternatives': [...]}
        """
        batch = self.get_batch(batch_id)
        if not batch:
            print(f"Batch {batch_id} introuvable.")
            return {}
        
        print(f"Status du batch: {batch.status}")
        
        if batch.status != "completed":
            print(f"Le batch {batch_id} n'est pas terminé (statut: {batch.status}).")
            return {}
        
        output_file_id = batch.output_file_id
        if not output_file_id:
            print(f"Aucun fichier de sortie trouvé pour le batch {batch_id}.")
            return {}
        
        print(f"ID du fichier de sortie: {output_file_id}")
        
        try:
            # Télécharger le fichier de résultats
            print(f"Téléchargement des résultats du batch {batch_id}...")
            output_response = self.client.files.content(output_file_id)
            
            # Vérification de la réponse
            if output_response is None:
                print("Erreur: La réponse de l'API est None")
                return {}
            
            # Vérification du contenu
            output_content = getattr(output_response, 'text', None)
            if output_content is None:
                print("Erreur: Le contenu du fichier est None")
                # Essayer d'autres attributs
                if hasattr(output_response, 'content'):
                    output_content = output_response.content
                    if isinstance(output_content, bytes):
                        output_content = output_content.decode('utf-8')
                else:
                    print("Erreur: Impossible de récupérer le contenu du fichier")
                    return {}
            
            print(f"Taille du contenu récupéré: {len(output_content) if output_content else 0} caractères")
            
            if not output_content or not output_content.strip():
                print("Erreur: Le contenu du fichier est vide")
                return {}
            
            # Sauvegarder les résultats bruts si demandé
            if save_raw:
                raw_dir = self.output_dir / "raw_results"
                raw_dir.mkdir(parents=True, exist_ok=True)
                raw_file = raw_dir / f"{batch_id}_results.jsonl"
                with open(raw_file, 'w', encoding='utf-8') as f:
                    f.write(output_content)
                print(f"Résultats bruts sauvegardés dans {raw_file}")
            
            # Traiter les résultats
            results = {}
            lines = output_content.strip().split('\n')
            print(f"Nombre de lignes à traiter: {len(lines)}")
            
            for i, line in enumerate(lines):
                if not line.strip():
                    continue
                
                try:
                    result = json.loads(line)
                except json.JSONDecodeError as e:
                    logger.error(f"Erreur de parsing JSON ligne {i+1}: {e}")
                    print(f"Ligne problématique: {line[:100]}...")
                    continue
                
                custom_id = result.get("custom_id")
                if not custom_id:
                    logger.warning(f"Pas de custom_id trouvé ligne {i+1}")
                    continue
                
                if result.get("error"):
                    logger.error(f"Erreur pour la requête {custom_id}: {result['error']}")
                    continue
                
                # Extraire la réponse
                response_data = result.get("response")
                if not response_data:
                    logger.warning(f"Pas de réponse trouvée pour {custom_id}")
                    continue
                
                body = response_data.get("body")
                if not body:
                    logger.warning(f"Pas de body trouvé pour {custom_id}")
                    continue
                
                choices = body.get("choices")
                if not choices or len(choices) == 0:
                    logger.warning(f"Pas de choices trouvés pour {custom_id}")
                    continue
                
                first_choice = choices[0]
                message = first_choice.get("message")
                if not message:
                    logger.warning(f"Pas de message trouvé pour {custom_id}")
                    continue
                
                content = message.get("content")
                if content is None:
                    logger.warning(f"Contenu None pour {custom_id}")
                    content = ""
                
                # Nettoyer le contenu
                content = self.clean_code_response(content)
                
                # Extraction des logprobs
                alternatives = []
                logprobs_data = first_choice.get("logprobs")
                if logprobs_data and isinstance(logprobs_data, dict):
                    logprobs_content = logprobs_data.get('content')
                    if logprobs_content and len(logprobs_content) > 0:
                        first_token = logprobs_content[0]
                        if isinstance(first_token, dict):
                            top_logprobs = first_token.get('top_logprobs', [])
                            for item in top_logprobs:
                                if isinstance(item, dict):
                                    alternatives.append({
                                        "token": item.get('token', ''),
                                        "logprob": item.get('logprob', -100)
                                    })
                
                results[custom_id] = {
                    "content": content,
                    "alternatives": alternatives
                }
                
            print(f"Traitement terminé: {len(results)} résultats extraits.")
            return results
            
        except Exception as e:
            import traceback
            logger.error(f"Erreur lors du traitement des résultats: {e}")
            logger.error(f"Traceback complet: {traceback.format_exc()}")
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
        save_dir = Path(output_dir) if output_dir else self.output_dir / batch_id
        save_dir.mkdir(parents=True, exist_ok=True)
        
        saved_count = 0
        for custom_id, result in results.items():
            # Créer un nom de fichier basé sur le custom_id
            filename = f"{custom_id}.py"
            file_path = save_dir / filename
            
            # Extraire le contenu à sauvegarder
            content = result["content"] if isinstance(result, dict) and "content" in result else str(result)
            
            try:
                # Sauvegarder le contenu
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                saved_count += 1
            except Exception as e:
                logger.error(f"Erreur lors de la sauvegarde de {custom_id}: {e}")
        
        print(f"Sauvegarde terminée: {saved_count} fichiers sauvegardés dans {save_dir}")
        return saved_count

    def save_tokens_json_per_script(self, results, output_dir=None):
        """
        Sauvegarde les tokens prédits pour chaque script dans un fichier JSON unique par script.
        Le nom du fichier est nom_du_script.py__N_tokens.json et le contenu est une liste de {"token": ..., "alternatives": [...]}
        Tente de retrouver le nom du script à partir d'un mapping batch_ids.json si présent.
        """
        from collections import defaultdict
        import re
        import json as _json
        if not results:
            print("Aucun résultat à traiter pour la sauvegarde des tokens JSON.")
            return 0
        # Regrouper par script_id
        scripts = defaultdict(dict)
        for custom_id, result in results.items():
            m = re.match(r"(.+):(\d+)$", custom_id)
            if not m:
                continue
            script_id, token_index = m.group(1), int(m.group(2))
            # result peut être soit un str (token), soit un dict avec 'content' et 'alternatives'
            if isinstance(result, dict) and "content" in result:
                token = result["content"]
                alternatives = result.get("alternatives", [])
            else:
                token = result
                alternatives = []
            scripts[script_id][token_index] = {"token": token, "alternatives": alternatives}
        # Chercher un mapping script_id -> nom du script dans batch_ids.json si possible
        script_id_to_name = {}
        if output_dir:
            batch_dir = Path(output_dir)
            parent = batch_dir.parent
            batch_ids_file = parent / "batch_ids.json"
            if batch_ids_file.exists():
                try:
                    with open(batch_ids_file, "r", encoding="utf-8") as f:
                        batch_info = _json.load(f)
                    batch_scripts_info = batch_info.get("batch_scripts_info")
                    if batch_scripts_info:
                        for batch in batch_scripts_info.values():
                            for script_id, info in batch.items():
                                script_id_to_name[script_id] = info.get("script_name", script_id)
                except Exception as e:
                    print(f"Erreur lors de la lecture de batch_ids.json: {e}")
        save_dir = Path(output_dir) if output_dir else self.output_dir
        save_dir.mkdir(parents=True, exist_ok=True)
        count = 0
        for script_id, tokens_dict in scripts.items():
            # Ordonner les tokens par index
            tokens = [tokens_dict[i] for i in sorted(tokens_dict)]
            # Utiliser le mapping si possible
            script_name = script_id_to_name.get(script_id, script_id)
            filename = f"{script_name}__{len(tokens)}_tokens.json"
            file_path = save_dir / filename
            _json.dump(tokens, open(file_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print(f"Fichier JSON de tokens sauvegardé: {file_path}")
            count += 1
        return count


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
    # Sauvegarder les fichiers JSON de tokens si demandé
    if getattr(args, "save_tokens_json", False):
        n = manager.save_tokens_json_per_script(results, args.destination)
        print(f"{n} fichiers JSON de tokens générés.")

def command_fetch_range(args):
    """Commande pour récupérer les résultats de plusieurs batchs par rang"""
    manager = SimpleBatchManager(args.api_key, args.output)
    
    # Récupérer la liste des batchs
    batches = manager.list_batches(args.limit)
    
    if not batches:
        print("Aucun batch trouvé.")
        return
    
    # Vérifier que le rang est valide
    if args.rank <= 0 or args.rank > len(batches):
        print(f"Rang invalide. Doit être entre 1 et {len(batches)}.")
        return
    
    # Parcourir les batchs jusqu'au rang spécifié
    success_count = 0
    for i in range(args.rank):
        batch = batches[i]
        batch_id = batch.id
        
        print(f"\nTraitement du batch {i+1}/{args.rank}: {batch_id}")
        
        # Vérifier si le batch est terminé
        if batch.status != "completed" and not args.force:
            print(f"Le batch {batch_id} n'est pas terminé (statut: {batch.status}). Ignoré.")
            continue
        
        # Récupérer les résultats
        results = manager.get_batch_results(batch_id, args.save_raw)
        
        if not results:
            print(f"Aucun résultat n'a pu être récupéré pour le batch {batch_id}.")
            continue
        
        # Sauvegarder les résultats
        saved = manager.save_results(batch_id, results, args.destination)
        if saved > 0:
            success_count += 1
    
    print(f"\nOpération terminée: {success_count} batchs sauvegardés avec succès.")

def command_find(args):
    """Handler pour la commande 'find'."""
    manager = SimpleBatchManager(api_key=args.api_key)
    end_date = args.end_date if args.end_date else args.start_date
    batches = manager.find_by_date(args.start_date, end_date, limit=args.limit)
    
    if batches:
        print(f"\n{len(batches)} lots trouvés entre {args.start_date} et {end_date}:")
        # Tri par date de création
        sorted_batches = sorted(batches, key=lambda b: b.created_at)
        for batch in sorted_batches:
            created_time = datetime.fromtimestamp(batch.created_at).strftime('%Y-%m-%d %H:%M:%S')
            print(f"- ID: {batch.id}, Status: {batch.status}, Créé le: {created_time}")
    else:
        print("Aucun lot trouvé pour la période spécifiée.")

def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description='Gestionnaire simple pour les batchs OpenAI')
    
    # Parent parser pour les arguments communs
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--api-key', type=str, help='Clé API OpenAI')
    parent_parser.add_argument('--output', type=str, default='./data/batches', help='Répertoire de base')
    
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
    fetch_parser.add_argument('--save-tokens-json', action='store_true', help='Sauvegarde les tokens prédits dans des fichiers JSON par script')
    fetch_parser.set_defaults(func=command_fetch)
    
    # Commande 'fetch-range'
    fetch_range_parser = subparsers.add_parser('fetch-range', help='Récupère les résultats de plusieurs batchs par rang', parents=[parent_parser])
    fetch_range_parser.add_argument('rank', type=int, help='Récupérer tous les batchs jusqu\'à ce rang (1 = plus récent)')
    fetch_range_parser.add_argument('--limit', type=int, default=100, help='Nombre maximum de batchs à récupérer')
    fetch_range_parser.add_argument('--force', action='store_true', help='Force la récupération même si les batchs ne sont pas terminés')
    fetch_range_parser.add_argument('--save-raw', action='store_true', help='Sauvegarde les résultats bruts')
    fetch_range_parser.add_argument('--destination', type=str, help='Répertoire de destination pour les résultats')
    fetch_range_parser.set_defaults(func=command_fetch_range)
    
    # Commande 'find'
    find_parser = subparsers.add_parser('find', help='Trouver des lots par plage de dates', parents=[parent_parser])
    find_parser.add_argument('start_date', help='Date de début (YYYY-MM-DD)')
    find_parser.add_argument('end_date', nargs='?', help='Date de fin (YYYY-MM-DD). Si omis, la recherche se fait sur la date de début.')
    find_parser.add_argument('--limit', type=int, default=2000, help='Nombre maximum de lots à scanner en partant des plus récents.')
    find_parser.set_defaults(func=command_find)
    
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