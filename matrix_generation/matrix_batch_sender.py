#!/usr/bin/env python3
"""
Script d'envoi de batches d'analyse token par token avec OpenAI
Format d'ID optimisé pour faciliter la récupération et le traitement des résultats.
S'arrête immédiatement après la validation des batches et déplace les scripts traités.
"""
import os
import sys  # Ajout de sys pour forcer l'arrêt du script
import time
import json
import argparse
import tempfile
import tiktoken
import logging
import datetime
import shutil
import base64
from pathlib import Path
from tqdm import tqdm
from openai import OpenAI

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Initialisation du client OpenAI
client = OpenAI(api_key="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")

def tokeniser_avec_tiktoken(texte, modele="gpt-4o-mini"):
    """
    Tokenise le texte en utilisant tiktoken, la bibliothèque officielle d'OpenAI pour la tokenisation.
    
    Args:
        texte (str): Le texte à tokeniser
        modele (str): Le modèle GPT dont on veut utiliser l'encodeur (par défaut: "gpt-4o-mini")
        
    Returns:
        tuple: Une liste de tokens (IDs) et une liste des tokens sous forme de chaînes de caractères
    """
    try:
        encodeur = tiktoken.encoding_for_model(modele)
    except KeyError:
        logger.warning(f"Encodeur pour {modele} non trouvé, utilisation de cl200k_base à la place.")
        encodeur = tiktoken.get_encoding("cl200k_base")
    
    token_ids = encodeur.encode(texte)
    tokens = [encodeur.decode_single_token_bytes(token_id).decode('utf-8', errors='replace') 
              for token_id in token_ids]
    
    return token_ids, tokens

class BatchRequestItem:
    """Représente un élément de requête batch pour l'API OpenAI avec ID informatif."""
    
    def __init__(self, script_name, token_index, token_content, context, model):
        """
        Initialise un élément de requête batch avec un ID informatif.
        
        Args:
            script_name (str): Nom du script d'origine
            token_index (int): Index du token dans le script
            token_content (str): Contenu du token
            context (str): Contexte actuel (jusqu'au token précédent)
            model (str): Modèle de prédiction
        """
        # Nouveau format d'ID: script_name:token_index
        # Cela permet de regrouper les résultats par nom de script d'origine
        self.custom_id = f"{script_name}:{token_index}"
        self.context = context
        self.model = model
        self.token_content = token_content  # Stocké mais pas inclus dans l'ID

    def to_jsonl(self):
        """Convertit la requête en format JSONL attendu par l'API batch."""
        system_msg = (
            "You are a code predictor that generates only the next token without any additional text."
            " Pay attention to spaces, tabs, line breaks, and special symbols in the code."
        )
        user_msg = f"Code context: {self.context}"
        req = {
            "custom_id": self.custom_id,
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_msg}
                ],
                "max_tokens": 1,
                "logprobs": True,
                "top_logprobs": 5,
                "temperature": 0.0,
                "top_p": 0.1
            }
        }
        return json.dumps(req)

class BatchAnalyzer:
    """Classe pour gérer les analyses en mode batch avec l'API OpenAI."""
    
    def __init__(self, batch_size=5000, poll_interval=20):
        self.batch_size = batch_size
        self.poll_interval = poll_interval

    def create_batch_file(self, items):
        """Crée un fichier JSONL temporaire avec les requêtes batch."""
        fd, path = tempfile.mkstemp(suffix='.jsonl')
        os.close(fd)
        with open(path, 'w', encoding='utf-8') as f:
            for item in items:
                f.write(item.to_jsonl() + "\n")
        return path

    def submit_batch(self, items):
        """Soumet un lot de requêtes à l'API batch d'OpenAI."""
        file_path = self.create_batch_file(items)
        with open(file_path, 'rb') as f:
            uploaded = client.files.create(file=f, purpose="batch")
        batch = client.batches.create(
            input_file_id=uploaded.id,
            endpoint="/v1/chat/completions",
            completion_window="24h"
        )
        os.unlink(file_path)
        return batch.id

    def is_batch_validated(self, batch_id):
        """
        Vérifie si le batch est validé (statut différent de 'queued').
        Retourne True dès que le batch est validé par l'API.
        
        Args:
            batch_id (str): ID du batch à vérifier
            
        Returns:
            bool: True si le batch est validé, False sinon
        """
        try:
            batch = client.batches.retrieve(batch_id)
            status = batch.status
            completed = batch.request_counts.completed
            total = batch.request_counts.total
            
            logger.info(f"Batch {batch_id} status: {status} ({completed}/{total})")
            
            # Si le statut n'est pas 'queued', le batch est considéré comme validé
            if status != 'queued':
                if status in ['pending', 'processing', 'completed']:
                    logger.info(f"Batch {batch_id} validé par l'API (statut: {status}).")
                    return True
                elif status in ['failed', 'cancelled', 'expired']:
                    logger.error(f"Batch {batch_id} a échoué avec le statut {status}")
                    raise RuntimeError(f"Batch {batch_id} a échoué avec le statut {status}")
            
            # Le batch est toujours en file d'attente
            return False
            
        except Exception as e:
            logger.error(f"Erreur lors de la vérification du batch {batch_id}: {e}")
            raise

    def poll_until_validation(self, batch_id, max_attempts=30):
        """
        Attend que le batch soit validé (statut différent de 'queued').
        S'arrête dès que le batch est validé ou après un nombre maximal de tentatives.
        
        Args:
            batch_id (str): ID du batch à surveiller
            max_attempts (int): Nombre maximal de tentatives
            
        Returns:
            bool: True si le batch est validé, False si le nombre maximal de tentatives est atteint
        """
        attempts = 0
        while attempts < max_attempts:
            # Vérifier si le batch est validé
            if self.is_batch_validated(batch_id):
                return True
                
            # Attendre avant la prochaine vérification
            logger.info(f"Batch {batch_id} toujours en file d'attente, nouvelle vérification dans {self.poll_interval} secondes...")
            time.sleep(self.poll_interval)
            attempts += 1
        
        logger.warning(f"Nombre maximal de tentatives atteint ({max_attempts}) pour le batch {batch_id}")
        return False

def deplacer_scripts(scripts_paths, archive_dir):
    """
    Déplace les scripts traités vers un dossier d'archives.
    
    Args:
        scripts_paths (list): Liste des chemins des scripts à déplacer
        archive_dir (Path): Répertoire d'archives
    """
    archive_dir.mkdir(exist_ok=True, parents=True)
    
    moved_count = 0
    for script_path in scripts_paths:
        try:
            # Préserver uniquement le nom du fichier
            archive_path = archive_dir / script_path.name
            
            # En cas de conflit de nom, ajouter un suffixe
            if archive_path.exists():
                stem = archive_path.stem
                suffix = archive_path.suffix
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                archive_path = archive_dir / f"{stem}_{timestamp}{suffix}"
            
            # DÉPLACER le fichier
            shutil.move(str(script_path), str(archive_path))
            logger.info(f"Script déplacé: {script_path} → {archive_path}")
            moved_count += 1
        except Exception as e:
            logger.error(f"Erreur lors du déplacement de {script_path}: {e}")
    
    logger.info(f"{moved_count}/{len(scripts_paths)} scripts déplacés avec succès")
    return moved_count

def trouver_scripts_python(directory_path):
    """Trouve tous les fichiers Python dans un répertoire et ses sous-dossiers."""
    if not directory_path.exists() or not directory_path.is_dir():
        raise NotADirectoryError(f"Le chemin spécifié n'est pas un dossier valide: {directory_path}")
    
    python_files = list(directory_path.glob("**/*.py"))
    logger.info(f"Trouvé {len(python_files)} fichiers Python dans {directory_path} et ses sous-dossiers")
    return python_files

def sauvegarder_information_tokens(scripts_info, output_dir):
    """
    Sauvegarde les informations sur les tokens et les scripts pour permettre 
    la reconstruction des matrices après récupération des résultats de l'API.
    
    Args:
        scripts_info (dict): Dictionnaire contenant les informations sur les scripts et leurs tokens
        output_dir (Path): Répertoire de sortie
    """
    tokens_dir = output_dir / "tokens_info"
    tokens_dir.mkdir(exist_ok=True, parents=True)
    
    # Créer un fichier d'information simple par script
    for script_id, info in scripts_info.items():
        script_name = info["script_name"]
        tokens = info["tokens"]
        # Sauvegarder au format simple : liste de tokens {token: "valeur"}
        simple_tokens = [{"token": t} for t in tokens]
        simple_file = tokens_dir / f"{script_name}__{len(tokens)}_tokens.json"
        with open(simple_file, "w", encoding="utf-8") as f:
            json.dump(path_to_str(simple_tokens), f, ensure_ascii=False, indent=2)
        logger.info(f"Fichier simple de tokens sauvegardé pour {script_name} dans {simple_file}")

def preparer_batch_items(scripts, modele_tokenisation, modele_prediction, batch_size=5000):
    """
    Prépare les items de batch à partir de plusieurs scripts.
    Utilise un format d'ID optimisé pour faciliter le traitement des résultats.
    Ajoute la gestion de la tabulation (token_precedent_est_tabulation).
    
    Args:
        scripts (list): Liste de tuples (chemin_script, contenu_script)
        modele_tokenisation (str): Modèle de tokenisation
        modele_prediction (str): Modèle de prédiction
        batch_size (int): Taille maximale du batch
        
    Returns:
        tuple: Liste des items de batch, dictionnaire d'informations sur les scripts
    """
    all_items = []
    scripts_info = {}
    
    # Générer un identifiant unique pour chaque batch
    batch_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for script_index, (script_path, script_content) in enumerate(scripts):
        # Créer un ID unique pour ce script
        script_id = f"script_{batch_timestamp}_{script_index}"
        script_name = script_path.name
        
        # Tokeniser le script
        token_ids, tokens = tokeniser_avec_tiktoken(script_content, modele_tokenisation)
        logger.info(f"Script {script_name} tokenisé en {len(tokens)} tokens")
        
        # Stocker les informations sur ce script
        scripts_info[script_id] = {
            "script_path": script_path,
            "script_name": script_name,
            "tokens": tokens,
            "token_ids": token_ids
        }
        
        # Traiter chaque token
        for token_index, token in enumerate(tokens):
            # Le contexte pour ce token est tous les tokens précédents
            context = ''.join(tokens[:token_index])
            # Gestion de la tabulation :
            token_precedent_est_tabulation = False
            if token_index > 0:
                token_precedent = tokens[token_index-1]
                if "\n" not in token_precedent:
                    token_precedent_est_tabulation = token_precedent.strip() == "" and len(token_precedent) > 1
            # Créer l'item de batch avec ID informatif basé sur le nom du script
            item = BatchRequestItem(
                script_name=script_name,
                token_index=token_index,
                token_content=token,
                context=context,
                model=modele_prediction
            )
            # Ajoute l'info tabulation dans l'item (pour la reconstruction)
            item.token_precedent_est_tabulation = token_precedent_est_tabulation
            all_items.append(item)
    
    # Limiter au batch_size
    batch_items = all_items[:batch_size]
    logger.info(f"Batch préparé avec {len(batch_items)}/{len(all_items)} items")
    
    return batch_items, scripts_info

def envoyer_batches(directory_path, output_dir, archive_dir=None, modele_tokenisation="gpt-4o-mini", 
                   modele_prediction="gpt-4o-mini", batch_size=5000, poll_interval=20, 
                   max_batches=1):
    """
    Traite les fichiers Python d'un répertoire en mode batch.
    Crée un sous-dossier "matrixes" pour stocker les matrices générées,
    et un dossier "archive" pour déplacer les scripts traités.
    
    Args:
        directory_path (Path): Chemin du répertoire contenant les scripts Python
        output_dir (Path): Chemin du répertoire de sortie pour les matrices
        archive_dir (Path, optional): Chemin du répertoire d'archives pour les scripts traités
        modele_tokenisation (str): Modèle à utiliser pour la tokenisation
        modele_prediction (str): Modèle à utiliser pour la prédiction
        batch_size (int): Taille des batches
        poll_interval (int): Intervalle en secondes entre deux vérifications de l'état des batches
        max_batches (int): Nombre maximum de batches à envoyer (None pour illimité)
        
    Returns:
        list: Liste des IDs des batches soumis
    """
    logger.info(f"Traitement des fichiers Python dans {directory_path}")
    logger.info(f"Modèle de tokenisation: {modele_tokenisation}")
    logger.info(f"Modèle de prédiction: {modele_prediction}")
    logger.info(f"Taille des batches: {batch_size}")
    
    # Créer les répertoires de sortie
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    
    if archive_dir:
        archive_dir = Path(archive_dir)
    else:
        archive_dir = output_dir / "processed_scripts"
    
    try:
        # Trouver tous les fichiers Python dans le répertoire
        directory_path = Path(directory_path)
        scripts_paths = trouver_scripts_python(directory_path)
        
        if not scripts_paths:
            logger.error(f"Aucun fichier Python trouvé dans {directory_path}")
            return []
            
        # Lire le contenu des scripts
        scripts = []
        for script_path in scripts_paths:
            try:
                with open(script_path, "r", encoding="utf-8") as f:
                    content = f.read()
                scripts.append((script_path, content))
            except Exception as e:
                logger.error(f"Erreur lors de la lecture de {script_path}: {e}")
        
        # Préparer les items de batch
        logger.info(f"Préparation des batches pour {len(scripts)} scripts")
        batch_items, scripts_info = preparer_batch_items(scripts, modele_tokenisation, modele_prediction, batch_size)
        
        # Sauvegarder les informations sur les tokens
        sauvegarder_information_tokens(scripts_info, output_dir)
        
        # Diviser en batches de taille maximale batch_size
        batches = []
        for i in range(0, len(batch_items), batch_size):
            batches.append(batch_items[i:i + batch_size])
        
        logger.info(f"Préparation terminée: {len(batches)} batches, {len(batch_items)} requêtes au total")
        
        # Limiter le nombre de batches si demandé
        if max_batches and len(batches) > max_batches:
            logger.info(f"Limitation à {max_batches} batches sur {len(batches)}")
            batches = batches[:max_batches]
        
        # Soumettre les batches
        analyzer = BatchAnalyzer(batch_size, poll_interval)
        submitted_batches = []
        
        for i, batch in enumerate(batches):
            try:
                logger.info(f"Soumission du batch {i+1}/{len(batches)} ({len(batch)} requêtes)...")
                batch_id = analyzer.submit_batch(batch)
                # Préfixer l'ID du batch avec "tbatch_"
                prefixed_batch_id = f"tbatch_{batch_id[6:]}" if batch_id.startswith("batch_") else batch_id
                
                # Stocker l'information sur le batch dans un fichier JSON
                batch_info = {
                    "original_batch_id": batch_id,
                    "prefixed_batch_id": prefixed_batch_id,
                    "status": "submitted",
                    "timestamp": datetime.datetime.now().isoformat(),
                    "model_tokenisation": modele_tokenisation,
                    "model_prediction": modele_prediction,
                    "request_count": len(batch),
                    "scripts": list(scripts_info.keys())
                }
                
                batch_info_file = output_dir / f"tbatch_info_{batch_id}.json"
                with open(batch_info_file, "w", encoding="utf-8") as f:
                    json.dump(batch_info, f, ensure_ascii=False, indent=2)
                
                logger.info(f"Batch {i+1} soumis avec l'ID: {prefixed_batch_id}")
                submitted_batches.append(prefixed_batch_id)
                
                # Attendre que le batch soit validé par l'API avant de continuer
                logger.info(f"Vérification que le batch {prefixed_batch_id} est validé par l'API...")
                analyzer.poll_until_validation(batch_id)
                
            except Exception as e:
                logger.error(f"Erreur lors de la soumission du batch {i+1}: {e}")
        
        # Déplacer les scripts traités vers le dossier d'archives
        if submitted_batches and archive_dir:
            logger.info(f"Déplacement des scripts traités vers {archive_dir}")
            deplacer_scripts(scripts_paths, archive_dir)
        
        # Écrire un fichier README dans le dossier de sortie
        if submitted_batches:
            readme_path = output_dir / "README_NEXT_STEPS.txt"
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write("Instructions pour récupérer les résultats des batches\n")
                f.write("==============================================\n\n")
                f.write("1. Récupérez les résultats des batches depuis l'API OpenAI avec les IDs suivants:\n")
                for batch_id in submitted_batches:
                    f.write(f"   - {batch_id}\n")
                f.write("\n2. Utilisez le script matrix_constructor.py pour générer les matrices finales.\n")
        
        logger.info(f"IMPORTANT: Veuillez récupérer les résultats manuellement depuis l'API OpenAI.")
        return submitted_batches
        
    except Exception as e:
        logger.error(f"Erreur lors du traitement des batches: {e}")
        return []

# Fonction utilitaire pour convertir récursivement les Path en str
def path_to_str(obj):
    if isinstance(obj, dict):
        return {k: path_to_str(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [path_to_str(i) for i in obj]
    elif isinstance(obj, Path):
        return str(obj)
    else:
        return obj

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script d'envoi de batches d'analyse token par token avec OpenAI"
    )
    parser.add_argument("--directory", "-d", type=str, required=True,
                        help="Chemin vers un dossier contenant des scripts à analyser (recherche récursive)")
    parser.add_argument("--output-dir", "-o", type=str, required=True,
                        help="Répertoire de sortie pour les résultats")
    parser.add_argument("--archive-dir", "-a", type=str, default=None,
                        help="Répertoire d'archivage pour les scripts traités (par défaut: output-dir/archives/scripts)")
    parser.add_argument("--token-model", "-t", type=str, default="gpt-4o-mini",
                        help="Modèle de tokenisation (par défaut: gpt-4o-mini)")
    parser.add_argument("--pred-model", "-p", type=str, default="gpt-4o-mini",
                        help="Modèle de prédiction (par défaut: gpt-4o-mini)")
    parser.add_argument("--batch-size", "-b", type=int, default=5000,
                        help="Taille du batch (par défaut: 5000)")
    parser.add_argument("--poll-interval", "-i", type=int, default=20,
                        help="Intervalle de sondage en secondes (par défaut: 20)")
    parser.add_argument("--max-batches", "-m", type=int, default=1,
                        help="Nombre maximum de batches à envoyer (par défaut: 1)")
    
    args = parser.parse_args()
    
    # Convertir les chemins en objets Path
    directory_path = Path(args.directory)
    output_dir = Path(args.output_dir)
    archive_dir = Path(args.archive_dir) if args.archive_dir else None
    
    try:
        # Envoyer les batches
        submitted_batches = envoyer_batches(
            directory_path=directory_path,
            output_dir=output_dir,
            archive_dir=archive_dir,
            modele_tokenisation=args.token_model,
            modele_prediction=args.pred_model,
            batch_size=args.batch_size,
            poll_interval=args.poll_interval,
            max_batches=args.max_batches
        )
        
        logger.info(f"Envoi des batches terminé avec succès!")
        logger.info(f"IDs de batch: {submitted_batches}")
        logger.info(f"Les scripts traités ont été déplacés vers: {archive_dir or (output_dir/'processed_scripts')}")
        logger.info(f"IMPORTANT: Veuillez récupérer les résultats manuellement depuis l'API OpenAI.")
        
        # Arrêt forcé du script
        logger.info("Arrêt forcé du script...")
        sys.exit(0)
        
    except Exception as e:
        logger.error(f"Erreur lors de l'envoi des batches: {e}")
        import traceback
        logger.error(traceback.format_exc())
        sys.exit(1)  # Sortie avec code d'erreur