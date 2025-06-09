from openai import OpenAI
import time
from tqdm import tqdm
import datetime
import tiktoken
import numpy as np
import os
import argparse
from pathlib import Path
import random
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def charger_script_depuis_fichier(nom_fichier):
    """
    Lit tout le contenu du fichier situé dans le répertoire 'data'
    et le renvoie comme une chaîne de caractères.
    """
    projet_racine = Path(__file__).resolve().parent.parent
    raw_dir       = projet_racine / "codenet" / "p00000"
    chemin_fichier  = raw_dir / nom_fichier

    if not chemin_fichier.exists():
        raise FileNotFoundError(f"Fichier introuvable : {chemin_fichier}")
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        return f.read()

# Variable globale pour le client API, sera initialisée dans main
client = None

# Dictionnaire des modèles et leur compatibilité avec les endpoints
MODELES_COMPATIBLES = {
    # Modèles compatibles avec les deux APIs (chat et completions)
    "gpt-4o-mini": "both",
    "gpt-4o": "both",
    "gpt-4.1": "both",
    "gpt-4.1-mini": "both",
    # Modèles compatibles avec chat/completions uniquement
    "gpt-3.5-turbo": "chat",
    # Modèles compatibles avec completions uniquement
    "text-davinci-003": "completions",
    "text-davinci-002": "completions",
    # Modèles compatibles avec les deux endpoints
    "gpt-3.5-turbo-instruct": "both"
}

def verifier_compatibilite_modele(modele, api_type):
    """
    Vérifie si le modèle est compatible avec le type d'API spécifié.
    
    Args:
        modele (str): Le modèle à vérifier
        api_type (str): Le type d'API ("chat" ou "completions")
        
    Returns:
        bool: True si compatible, False sinon
    """
    if modele not in MODELES_COMPATIBLES:
        logger.warning(f"Modèle {modele} non trouvé dans la liste de compatibilité, supposé compatible avec les deux endpoints.")
        return True
    
    compat = MODELES_COMPATIBLES[modele]
    return compat == "both" or compat == api_type

def tokeniser_avec_tiktoken(texte, modele="gpt-4o-mini"):
    """
    Tokenise le texte en utilisant tiktoken, la bibliothèque officielle d'OpenAI pour la tokenisation.
    Cette fonction utilise l'encodeur correspondant au modèle spécifié.
    
    Args:
        texte (str): Le texte à tokeniser
        modele (str): Le modèle GPT dont on veut utiliser l'encodeur (par défaut: "gpt-4o-mini")
        
    Returns:
        tuple: Une liste de tokens (IDs) et une liste des tokens sous forme de chaînes de caractères
    """
    try:
        # Obtenir l'encodeur correspondant au modèle
        encodeur = tiktoken.encoding_for_model(modele)
    except KeyError:
        # Si le modèle n'est pas disponible, utiliser l'encodeur cl100k_base (utilisé par gpt-4, gpt-3.5-turbo)
        logger.warning(f"Encodeur pour {modele} non trouvé, utilisation de cl100k_base à la place.")
        encodeur = tiktoken.get_encoding("cl100k_base")
    
    # Encoder le texte en tokens (IDs numériques)
    token_ids = encodeur.encode(texte)
    
    # Convertir les IDs en tokens (chaînes de caractères)
    tokens = [encodeur.decode_single_token_bytes(token_id).decode('utf-8', errors='replace') for token_id in token_ids]
    
    return token_ids, tokens

def retry_with_exponential_backoff(func, max_retries=5, initial_delay=1, max_delay=60):
    """
    Fonction utilitaire pour réessayer avec backoff exponentiel en cas d'erreur.
    
    Args:
        func: La fonction à exécuter
        max_retries: Nombre maximal de tentatives
        initial_delay: Délai initial entre les tentatives (en secondes)
        max_delay: Délai maximal entre les tentatives (en secondes)
        
    Returns:
        Le résultat de la fonction si elle réussit
        
    Raises:
        Exception: Si toutes les tentatives échouent
    """
    retries = 0
    delay = initial_delay
    
    while True:
        try:
            return func()
        except Exception as e:
            retries += 1
            if retries > max_retries:
                logger.error(f"Échec après {max_retries} tentatives: {e}")
                raise
            
            # Appliquer un jitter pour éviter les collisions
            jitter = random.uniform(0, 0.1) * delay
            sleep_time = min(delay + jitter, max_delay)
            
            logger.warning(f"Erreur: {e}. Nouvelle tentative dans {sleep_time:.2f}s (tentative {retries}/{max_retries})")
            time.sleep(sleep_time)
            
            # Augmenter le délai pour la prochaine tentative
            delay = min(delay * 2, max_delay)

def analyser_avec_chat_completions(contexte_actuel, modele="gpt-4o-mini"):
    """
    Utilise l'API chat/completions pour prédire le prochain token.
    
    Args:
        contexte_actuel (str): Contexte du code actuel
        modele (str): Modèle à utiliser pour la prédiction
        
    Returns:
        tuple: Token prédit, liste d'alternatives avec leurs logprobs
    """
    def make_request():
        messages = [
            {"role": "system", "content": "You are a code predictor that generates only the next token without any additional text. Pay attention to spaces, tabs, line breaks, and special symbols in the code."},
            {"role": "user", "content": f"Code context: {contexte_actuel}"}
        ]
        
        response = client.chat.completions.create(
            model=modele,
            messages=messages,
            temperature=0,
            max_tokens=1,
            logprobs=True,
            top_logprobs=10
        )
        
        # Extraire le token prédit
        token_predit = response.choices[0].message.content
        
        # Extraire les alternatives avec leurs logprobs
        alternatives = []
        if hasattr(response.choices[0], "logprobs") and response.choices[0].logprobs:
            for logprob_obj in response.choices[0].logprobs.content:
                for item in logprob_obj.top_logprobs:
                    alternatives.append({
                        "token": item.token,
                        "logprob": item.logprob
                    })
        
        return token_predit, alternatives
    
    return retry_with_exponential_backoff(make_request)

def analyser_avec_completions(contexte_actuel, modele):
    """
    Utilise l'API completions pour prédire le prochain token.
    
    Args:
        contexte_actuel (str): Contexte du code actuel
        modele (str): Modèle à utiliser pour la prédiction
        
    Returns:
        tuple: Token prédit, liste d'alternatives avec leurs logprobs
    """
    def make_request():
        response = client.completions.create(
            model=modele,
            prompt=contexte_actuel,
            max_tokens=1,
            temperature=0.0,
            top_p=0.1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            logprobs=10,
            echo=False
        )
        
        # Extraire le token prédit
        token_predit = response.choices[0].text
        
        # Extraction des logprobs
        alternatives = []
        if hasattr(response.choices[0], 'logprobs') and response.choices[0].logprobs and response.choices[0].logprobs.top_logprobs:
            logprobs_data = response.choices[0].logprobs.top_logprobs[0]
            alternatives = [{"token": token, "logprob": logprob} for token, logprob in logprobs_data.items()]
        
        return token_predit, alternatives
    
    return retry_with_exponential_backoff(make_request)

def analyser_predictions_token_par_token(script, modele_tokenisation="gpt-4o-mini", modele_prediction="gpt-4o-mini", api_type="completions"):
    """
    Analyse les prédictions du modèle pour chaque token du script.
    
    Args:
        script (str): Le script à analyser
        modele_tokenisation (str): Le modèle à utiliser pour la tokenisation
        modele_prediction (str): Le modèle à utiliser pour la prédiction
        api_type (str): Type d'API à utiliser ("completions" ou "chat")
    
    Returns:
        tuple: Résultats d'analyse et tokens de référence
    """
    # Vérifier la compatibilité du modèle avec le type d'API
    if not verifier_compatibilite_modele(modele_prediction, api_type):
        raise ValueError(f"Le modèle {modele_prediction} n'est pas compatible avec l'API {api_type}. "
                         f"Veuillez choisir une combinaison compatible.")
    
    # Tokeniser le script avec tiktoken
    logger.info(f"Tokenisation du script avec tiktoken ({modele_tokenisation})...")
    token_ids, tokens_reference = tokeniser_avec_tiktoken(script, modele_tokenisation)
    
    logger.info(f"Nombre de tokens dans la référence tiktoken: {len(tokens_reference)}")
    logger.info("Tokens identifiés:")
    for i, token in enumerate(tokens_reference):
        token_display = repr(token)[1:-1]  # Utiliser repr pour voir les caractères spéciaux
        logger.info(f"{i}: '{token_display}' (ID: {token_ids[i]})")
    
    # Nouvelle liste pour stocker les résultats d'analyse
    resultats_analyse = []
    
    # Ajuster dynamiquement le nombre de tokens d'amorce
    amorce_tokens = max(1, min(3, len(tokens_reference) // 3))
    
    logger.info(f"\nUtilisation de {amorce_tokens} token(s) d'amorce...")
    
    # Traitement des tokens d'amorce (sans prédiction)
    for i in range(amorce_tokens):
        resultats_analyse.append({
            "index": i,
            "token": tokens_reference[i],
            "amorce": True
        })
    
    # Barre de progression pour l'analyse
    with tqdm(total=len(tokens_reference) - amorce_tokens, desc="Analyse des tokens") as pbar:
        # Boucle sur les tokens du script à partir du premier token après l'amorce
        for i in range(amorce_tokens, len(tokens_reference)):
            # Construire le contexte pour la prédiction
            contexte = "".join(tokens_reference[:i])
            
            # Choisir la fonction d'analyse appropriée
            if api_type == "chat":
                token_predit, alternatives = analyser_avec_chat_completions(contexte, modele_prediction)
            else:
                token_predit, alternatives = analyser_avec_completions(contexte, modele_prediction)
            
            # Token de référence actuel
            token_actuel = tokens_reference[i]
            
            # Vérifier si la prédiction est correcte
            prediction_correcte = token_predit == token_actuel
            prediction_correcte_top10 = token_actuel in [alt["token"] for alt in alternatives]
            
            # Stocker les résultats
            resultats_analyse.append({
                "index": i,
                "token": token_actuel,
                "contexte": contexte,
                "prediction": token_predit,
                "correct": prediction_correcte,
                "correct_top10": prediction_correcte_top10,
                "alternatives": alternatives
            })
            
            # Mettre à jour la barre de progression
            pbar.update(1)
            
    return resultats_analyse, tokens_reference

def construire_matrice_logprob(tokens_reference, resultats_analyse, top_k=10):
    """
    Construit une matrice 2D où chaque ligne représente un token et chaque colonne
    représente un logprob.
    
    Args:
        tokens_reference: La liste des tokens du script original
        resultats_analyse: Les résultats de l'analyse token par token
        top_k: Le nombre d'alternatives à considérer pour les logprobs
        
    Returns:
        tuple: La matrice de logprobs et une liste de dictionnaires décrivant chaque token
    """
    # Filtrer les tokens d'amorce des résultats d'analyse
    resultats_filtres = [r for r in resultats_analyse if not r.get("amorce", False)]
    
    # Nombre de tokens à analyser (ceux qui ne sont pas des amorces)
    nombre_tokens = len(resultats_filtres)
    
    # Initialiser la matrice avec une valeur par défaut (ex: -100 pour log(probabilité très faible))
    matrice = np.full((nombre_tokens, top_k + 1), -100.0, dtype=np.float32)
    
    # Structure pour garder une trace des tokens
    structure_tokens = []
    
    # Dictionnaire pour mapper les tokens à leur index dans la matrice de logprobs
    token_to_index = {}
    
    # Remplir la matrice
    for i, res in enumerate(resultats_filtres):
        # Ajouter le token de référence à la structure
        structure_tokens.append({
            "index": res["index"],
            "token": res["token"],
            "prediction_correcte": res["correct"]
        })
        
        # Remplir les logprobs des alternatives
        for j, alt in enumerate(res.get("alternatives", [])[:top_k]):
            matrice[i, j] = alt["logprob"]
        
        # Ajouter la logprob du token de référence (s'il est dans les alternatives)
        token_ref_logprob = -100.0
        for alt in res.get("alternatives", []):
            if alt["token"] == res["token"]:
                token_ref_logprob = alt["logprob"]
                break
        matrice[i, top_k] = token_ref_logprob # Dernière colonne pour le token de référence
            
    return matrice, structure_tokens

def afficher_matrice_brute(matrice, structure_tokens):
    """
    Affiche la matrice brute de logprobs dans la console.
    
    Args:
        matrice: La matrice de logprobs à afficher
        structure_tokens: La structure des tokens
    """
    logger.info("\n--- Matrice de Log-Probabilités (brute) ---")
    
    # En-tête du tableau
    header = ["Token (Réf)", "Correct?"] + [f"Alt {i+1}" for i in range(matrice.shape[1] - 1)] + ["LogProb(Réf)"]
    print("\t".join(header))
    
    # Affichage de chaque ligne de la matrice
    for i in range(matrice.shape[0]):
        token_info = structure_tokens[i]
        token_display = repr(token_info['token'])[1:-1]
        
        # Limiter la longueur pour l'affichage
        if len(token_display) > 15:
            token_display = token_display[:12] + "..."
            
        is_correct = "Oui" if token_info['prediction_correcte'] else "Non"
        
        # Formatter les valeurs de logprob
        logprobs = [f"{val:.2f}" for val in matrice[i]]
        
        # Construire la ligne
        row = [token_display, is_correct] + logprobs
        
        print("\t".join(row))

def sauvegarder_resultats(resultats_analyse, script, matrice, structure_tokens, modele_tokenisation="gpt-4o-mini", nom_fichier=None):
    """
    Sauvegarde les résultats d'analyse dans un fichier texte.
    
    Args:
        resultats_analyse (list): Les résultats de l'analyse token par token.
        script (str): Le script original analysé.
        matrice (np.ndarray): La matrice de logprobs.
        structure_tokens (list): La structure des tokens.
        modele_tokenisation (str): Le modèle utilisé pour la tokenisation.
        nom_fichier (str): Le chemin du fichier où sauvegarder les résultats.
    """
    if nom_fichier is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_fichier = f"resultats_analyse_{timestamp}.txt"
        
    logger.info(f"Sauvegarde des résultats dans {nom_fichier}...")
    
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"--- Rapport d'analyse du {datetime.datetime.now()} ---\n\n")
        f.write(f"Modèle de tokenisation: {modele_tokenisation}\n")
        
        total_tokens = len([r for r in resultats_analyse if not r.get("amorce", False)])
        correct_tokens = len([r for r in resultats_analyse if r.get("correct", False) and not r.get("amorce", False)])
        
        if total_tokens > 0:
            precision = (correct_tokens / total_tokens) * 100
            f.write(f"Précision du modèle: {precision:.2f}% ({correct_tokens}/{total_tokens} tokens corrects)\n")
        
        f.write("\n--- Script analysé ---\n")
        f.write(script)
        f.write("\n\n--- Analyse détaillée token par token ---\n")
        
        for res in resultats_analyse:
            if res.get("amorce", True):
                f.write(f"Token {res['index']} (amorce): {repr(res['token'])}\n")
            else:
                f.write(f"\nToken {res['index']}: {repr(res['token'])}\n")
                f.write(f"  Contexte: {repr(res['contexte'])}\n")
                f.write(f"  Prédiction: {repr(res['prediction'])}\n")
                f.write(f"  Correct: {'Oui' if res['correct'] else 'Non'}\n")
                f.write("  Top 10 Alternatives (logprobs):\n")
                for alt in res.get("alternatives", []):
                    f.write(f"    - {repr(alt['token'])}: {alt['logprob']:.4f}\n")
        
        f.write("\n\n--- Matrice de log-probabilités ---\n")
        f.write("Index\tToken\tCorrect?\t" + "\t".join([f"Alt {i+1}" for i in range(matrice.shape[1] - 1)]) + "\tLogProb(Ref)\n")
        
        for i, token_info in enumerate(structure_tokens):
            row_data = [
                str(token_info['index']),
                repr(token_info['token']),
                "Oui" if token_info['prediction_correcte'] else "Non"
            ] + [f"{val:.4f}" for val in matrice[i]]
            f.write("\t".join(row_data) + "\n")
            
    logger.info(f"Rapport d'analyse sauvegardé dans {nom_fichier}")

def sauvegarder_matrice_numpy(matrice, nom_fichier="matrice_logprob.npy"):
    """
    Sauvegarde la matrice au format numpy.
    
    Args:
        matrice: La matrice à sauvegarder.
        nom_fichier: Le chemin du fichier.
    """
    np.save(nom_fichier, matrice)
    logger.info(f"Matrice sauvegardée au format numpy dans {nom_fichier}")

def main():
    """Fonction principale qui exécute l'analyse en ligne de commande"""
    global client

    parser = argparse.ArgumentParser(
        description="Analyse des prédictions token par token pour un ou plusieurs scripts.")
    
    parser.add_argument(
        "-m", "--model",
        help="Modèle de prédiction à utiliser (ex: gpt-4o-mini)",
        type=str,
        default="gpt-4o-mini",
    )
    
    parser.add_argument(
        "-f", "--file",
        help="Nom du fichier unique à analyser (dans le dossier d'entrée). Ex: 'foo.py'",
        type=str,
        default=None,
    )
    
    parser.add_argument(
        "--all",
        help="Analyser tous les fichiers Python (*.py) du dossier d'entrée",
        action="store_true",
    )
    
    parser.add_argument(
        "-r", "--recursive",
        help="Rechercher les fichiers Python de manière récursive dans les sous-dossiers",
        action="store_true",
    )
    
    parser.add_argument(
        "-d", "--directory", "--input",
        help="Dossier contenant les scripts à analyser",
        type=str,
        default=None,
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Dossier où sauvegarder les résultats",
        type=str,
        default=None,
    )
    
    parser.add_argument(
        "--api",
        help="Type d'API à utiliser: 'completions' (par défaut) ou 'chat'",
        type=str,
        choices=["completions", "chat"],
        default="completions",
    )
    
    parser.add_argument(
        "--api_key",
        help="Clé API OpenAI. Peut aussi être définie via la variable d'environnement OPENAI_API_KEY.",
        type=str,
        default=os.environ.get("OPENAI_API_KEY")
    )
    parser.add_argument(
        "--local_api_url",
        help="URL de l'API d'un LLM local (ex: http://localhost:11434/v1). Si spécifié, --api_key est ignorée.",
        type=str,
        default=os.environ.get("LOCAL_API_URL")
    )
    
    args = parser.parse_args()

    # Initialisation du client OpenAI
    if args.local_api_url:
        logger.info(f"Utilisation de l'API locale à : {args.local_api_url}")
        client = OpenAI(base_url=args.local_api_url, api_key="ollama") # La clé pour les serveurs locaux est souvent une valeur factice
    elif args.api_key:
        logger.info("Utilisation de l'API OpenAI.")
        client = OpenAI(api_key=args.api_key)
    else:
        parser.error("Aucune clé API ou URL locale n'a été fournie. Veuillez utiliser --api_key, --local_api_url ou définir la variable d'environnement OPENAI_API_KEY.")

    # Détermination du dossier d'entrée
    if args.directory:
        input_dir = Path(args.directory)
        if not input_dir.exists() or not input_dir.is_dir():
            parser.error(f"Dossier d'entrée introuvable ou invalide: {input_dir}")
    else:
        # Dossier par défaut
        projet_racine = Path(__file__).resolve().parent.parent
        input_dir = projet_racine / "data" / "raw_scripts"
        if not input_dir.exists():
            input_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Dossier d'entrée créé: {input_dir}")

    # Détermination du dossier de sortie
    if args.output:
        output_dir = Path(args.output)
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Dossier de sortie créé: {output_dir}")
    else:
        # Dossier par défaut
        projet_racine = Path(__file__).resolve().parent.parent
        output_dir = projet_racine / "data" / "resultats"
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Dossier de sortie créé: {output_dir}")

    # Créer les sous-dossiers dans le dossier de sortie
    matrix_dir = output_dir / "matrices"
    results_dir = output_dir / "rapports"
    
    matrix_dir.mkdir(exist_ok=True)
    results_dir.mkdir(exist_ok=True)
    
    logger.info(f"Dossier d'entrée: {input_dir}")
    logger.info(f"Dossier de sortie: {output_dir}")
    logger.info(f"Dossier des matrices: {matrix_dir}")
    logger.info(f"Dossier des rapports: {results_dir}")

    # Détermination des fichiers à traiter
    if args.file:
        # Si un fichier spécifique est demandé, on ne traite que celui-là
        nom = args.file
        chemin = input_dir / nom
        if not chemin.exists():
            parser.error(f"Fichier introuvable : {chemin}")
        fichiers = [chemin]
    else:
        # Par défaut ou avec --all, on traite tous les fichiers Python du dossier
        if args.recursive:
            # Recherche récursive dans tous les sous-dossiers
            fichiers = sorted(input_dir.glob("**/*.py"))
            logger.info(f"Mode récursif activé: recherche dans tous les sous-dossiers de {input_dir}")
        else:
            # Recherche uniquement dans le dossier racine
            fichiers = sorted(input_dir.glob("*.py"))
            
        if not fichiers:
            parser.error(f"Aucun fichier Python (.py) trouvé dans {input_dir}{' ou ses sous-dossiers' if args.recursive else ''}")
        logger.info(f"Traitement de {len(fichiers)} fichiers Python trouvés dans {input_dir}{' et ses sous-dossiers' if args.recursive else ''}")

    # Boucle d'analyse
    for fpath in fichiers:
        stem = fpath.stem  # nom sans extension, ex: "gen_example"

        logger.info(f"\n--- Analyse de {fpath.name} avec API {args.api} ---")

        # Chargement et exécution de l'analyse
        script = fpath.read_text(encoding="utf-8")
        resultats_analyse, tokens_reference = analyser_predictions_token_par_token(
            script,
            modele_tokenisation=args.model,
            modele_prediction=args.model,
            api_type=args.api
        )
        matrice, structure = construire_matrice_logprob(tokens_reference, resultats_analyse)

        # Sauvegardes
        matrix_path = matrix_dir / f"matrix_{stem}.npy"
        result_path = results_dir / f"result_{stem}.txt"

        sauvegarder_matrice_numpy(matrice, nom_fichier=str(matrix_path))
        sauvegarder_resultats(
            resultats_analyse,
            script,
            matrice,
            structure,
            nom_fichier=str(result_path)
        )

        logger.info(f"→ Matrice enregistrée : {matrix_path.name}")
        logger.info(f"→ Rapport enregistré  : {result_path.name}")

        print(f"Matrice sauvegardée dans: {matrix_path}")

if __name__ == "__main__":
    main()