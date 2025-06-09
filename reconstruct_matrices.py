import os
import json
import time
import pandas as pd
from datetime import datetime, timezone, timedelta
from pathlib import Path
import numpy as np
import tiktoken
import logging
import re
from openai import OpenAI
from collections import defaultdict
from dotenv import load_dotenv

# --- Configuration ---
load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")
BASE_INPUT_DIR = Path("codenet")
BASE_OUTPUT_DIR = Path("reconstructed_data")
MATRIX_DIR = BASE_OUTPUT_DIR / "matrices"
REPORTS_DIR = BASE_OUTPUT_DIR / "reports"
MODEL_FOR_TOKENIZATION = "gpt-4o-mini"
TOP_K_ALTERNATIVES = 10
BATCH_REPORT_FILE = "batch_investigation_report.csv"

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("reconstruction.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# --- Fonctions réutilisées et adaptées ---

def tokeniser_avec_tiktoken(texte, modele="gpt-4o-mini"):
    try:
        encodeur = tiktoken.encoding_for_model(modele)
    except KeyError:
        logger.warning(f"Encodeur pour {modele} non trouvé, utilisation de cl100k_base.")
        encodeur = tiktoken.get_encoding("cl100k_base")
    
    token_ids = encodeur.encode(texte)
    return token_ids, [encodeur.decode_single_token_bytes(token_id).decode('utf-8', errors='replace') for token_id in token_ids]

def construire_matrice_logprob(resultats_analyse, top_k=10):
    resultats_filtres = [r for r in resultats_analyse if not r.get("amorce", False)]
    nombre_tokens = len(resultats_filtres)
    matrice = np.full((nombre_tokens, top_k + 1), -100.0, dtype=np.float32)
    structure_tokens = []

    for i, res in enumerate(resultats_filtres):
        structure_tokens.append({
            "index": res["index"],
            "token": res["token"],
            "prediction_correcte": res["correct"]
        })
        for j, alt in enumerate(res.get("alternatives", [])[:top_k]):
            matrice[i, j] = alt["logprob"]
        
        token_ref_logprob = -100.0
        for alt in res.get("alternatives", []):
            if alt["token"] == res["token"]:
                token_ref_logprob = alt["logprob"]
                break
        matrice[i, top_k] = token_ref_logprob
            
    return matrice, structure_tokens

def sauvegarder_matrice_numpy(matrice, nom_fichier):
    nom_fichier.parent.mkdir(parents=True, exist_ok=True)
    np.save(nom_fichier, matrice)
    logger.info(f"Matrice sauvegardée au format numpy dans {nom_fichier}")

def sauvegarder_resultats_rapport(resultats_analyse, script, matrice, structure_tokens, nom_fichier):
    logger.info(f"Sauvegarde du rapport dans {nom_fichier}...")
    nom_fichier.parent.mkdir(parents=True, exist_ok=True)
    
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"--- Rapport d'analyse du {datetime.now()} ---\n\n")
        f.write(f"Modèle de tokenisation: {MODEL_FOR_TOKENIZATION}\n")
        
        total_tokens = len([r for r in resultats_analyse if not r.get("amorce", False)])
        correct_tokens = len([r for r in resultats_analyse if r.get("correct", False)])
        correct_top10_tokens = len([r for r in resultats_analyse if r.get("correct_top10", False)])

        if total_tokens > 0:
            precision = (correct_tokens / total_tokens) * 100
            precision_top10 = (correct_top10_tokens / total_tokens) * 100
            f.write(f"Précision (Top 1): {precision:.2f}% ({correct_tokens}/{total_tokens} tokens corrects)\n")
            f.write(f"Précision (Top 10): {precision_top10:.2f}% ({correct_top10_tokens}/{total_tokens} corrects)\n")

        f.write("\n--- Script analysé ---\n")
        f.write(script)
        f.write("\n\n--- Matrice de log-probabilités (résumé) ---\n")
        f.write("Index\tToken\tCorrect?\t" + "\t".join([f"Alt {i+1}" for i in range(matrice.shape[1] - 1)]) + "\tLogProb(Ref)\n")
        
        for i, token_info in enumerate(structure_tokens):
            row_data = [
                str(token_info['index']),
                repr(token_info['token']),
                "Oui" if token_info['prediction_correcte'] else "Non"
            ] + [f"{val:.4f}" for val in matrice[i]]
            f.write("\t".join(row_data) + "\n")
            
    logger.info(f"Rapport d'analyse sauvegardé dans {nom_fichier}")

def get_batch_results(client, batch_id):
    logger.info(f"Récupération des résultats pour le lot {batch_id}...")
    try:
        batch = client.batches.retrieve(batch_id)
        if not batch.output_file_id:
            logger.warning(f"Aucun fichier de sortie pour le lot {batch_id} (statut: {batch.status}).")
            return None, batch
        
        logger.info(f"Fichier de sortie trouvé ({batch.output_file_id}), téléchargement...")
        file_content = client.files.content(batch.output_file_id).text
        
        if not file_content:
            logger.warning(f"Le fichier de sortie pour {batch_id} est vide.")
            return None, batch
            
        return file_content.strip().split('\n'), batch
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des résultats pour {batch_id}: {e}")
        return None, None

def find_original_script_path(batch, client):
    logger.info(f"Attempting to find original script for batch {batch.id} by content matching.")
    
    # 1. Get input file content
    try:
        input_file_content = client.files.content(batch.input_file_id).text
    except Exception as e:
        logger.error(f"Could not download input file content for batch {batch.id}: {e}")
        return None

    # 2. Parse LAST line and get code snippet for max specificity
    try:
        # Get the last non-empty line
        last_line = [line for line in input_file_content.strip().split('\n') if line][-1]
        data = json.loads(last_line)
        messages = data['body']['messages']
        
        raw_snippet = "".join([msg.get('content', '') for msg in messages])
        
        # Isolate the actual code from the prompt
        context_marker = "Code context:"
        if context_marker in raw_snippet:
            code_snippet = raw_snippet.split(context_marker, 1)[1].strip()
        else:
            code_snippet = raw_snippet.strip() # Fallback just in case

        if not code_snippet:
            logger.warning(f"No code snippet found in last request of batch {batch.id}")
            return None
        
        logger.info(f"Extracted snippet for matching (from last request):\n---\n{code_snippet}\n---")

    except (json.JSONDecodeError, KeyError, IndexError) as e:
        logger.error(f"Could not parse code snippet from batch {batch.id}: {e}")
        return None
    
    # 3. Search for the file in codenet
    candidate_files = []
    
    # The snippet from the batch is the entire context up to a point.
    # So, the original file should start with this snippet.
    for py_file in BASE_INPUT_DIR.rglob("*.py"):
        try:
            file_content = py_file.read_text(encoding='utf-8')
            # A robust startswith check, ignoring leading/trailing whitespace on both ends.
            if file_content.strip().startswith(code_snippet):
                candidate_files.append(py_file)
        except Exception as e:
            logger.warning(f"Could not read or compare file {py_file}: {e}")

    if len(candidate_files) == 1:
        logger.info(f"Unique match found: {candidate_files[0]}")
        return candidate_files[0]
    elif len(candidate_files) > 1:
        logger.warning(f"Found {len(candidate_files)} matching files for batch {batch.id}, which is ambiguous. Files: {candidate_files}")
    else: # len is 0
        logger.warning(f"No matching file found for batch {batch.id} using content search.")

    return None

def are_tokens_equivalent(token1, token2):
    """
    Compare two tokens, treating different whitespace representations as equal.
    This also handles cases where one token is an empty string and the other is whitespace.
    """
    # Normalize by stripping all whitespace characters from the token string.
    # If both are empty after stripping, they are equivalent.
    t1_stripped = token1.strip()
    t2_stripped = token2.strip()
    
    if t1_stripped == t2_stripped:
        return True
        
    return False

def reconstruct_analysis_from_batch_results(lines, script_content):
    if not lines or not script_content:
        return None

    try:
        _, tokens_reference = tokeniser_avec_tiktoken(script_content, MODEL_FOR_TOKENIZATION)
    except Exception as e:
        logger.error(f"Impossible de tokeniser le script source: {e}")
        return None

    predictions = {}
    for line in lines:
        try:
            data = json.loads(line)
            custom_id = data.get("custom_id")
            if not custom_id or not data.get("response"):
                continue

            match = re.match(r"token_(\d+)$", custom_id)
            if not match:
                continue
            
            token_index = int(match.group(1))
            
            body = data["response"].get("body", {})
            choices = body.get("choices", [])
            if not choices: continue

            first_choice = choices[0]
            prediction = first_choice.get("message", {}).get("content", "")
            
            alternatives = []
            logprobs_data = first_choice.get("logprobs")
            if logprobs_data and logprobs_data.get('content'):
                top_logprobs = logprobs_data['content'][0].get('top_logprobs', [])
                for item in top_logprobs:
                    alternatives.append({"token": item.get('token', ''), "logprob": item.get('logprob', -100)})

            predictions[token_index] = {"prediction": prediction, "alternatives": alternatives}
        except (json.JSONDecodeError, AttributeError, ValueError) as e:
            logger.warning(f"Ligne de résultat de lot invalide ou mal formée: {e} - Ligne: {line[:100]}")
            continue

    resultats_analyse = []
    amorce_tokens = max(1, min(3, len(tokens_reference) // 3))

    for i, token_actuel in enumerate(tokens_reference):
        if i < amorce_tokens:
            resultats_analyse.append({"index": i, "token": token_actuel, "amorce": True})
            continue

        if i in predictions:
            pred_data = predictions[i]
            token_predit = pred_data["prediction"]
            alts = pred_data["alternatives"]
            
            correct = are_tokens_equivalent(token_predit, token_actuel)
            correct_top10 = correct or any(are_tokens_equivalent(a["token"], token_actuel) for a in alts)
            
            resultats_analyse.append({
                "index": i, "token": token_actuel, "prediction": token_predit,
                "correct": correct, "correct_top10": correct_top10,
                "alternatives": alts, "amorce": False
            })
        else:
            resultats_analyse.append({
                "index": i, "token": token_actuel, "prediction": "[MANQUANT]",
                "correct": False, "correct_top10": False,
                "alternatives": [], "amorce": False
            })
    
    return resultats_analyse

def main():
    global client
    logger.info("--- Début du script de reconstruction de matrices ---")
    
    if not API_KEY:
        logger.error("La clé API n'est pas configurée. Veuillez la définir dans la variable d'environnement OPENAI_API_KEY.")
        return
        
    client = OpenAI(api_key=API_KEY)
    
    BASE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    try:
        df = pd.read_csv(BATCH_REPORT_FILE)
        completed_batches = df[df['status'] == 'completed']
        logger.info(f"Trouvé {len(completed_batches)} lots complétés dans {BATCH_REPORT_FILE}.")
    except FileNotFoundError:
        logger.error(f"Le fichier {BATCH_REPORT_FILE} n'a pas été trouvé.")
        return

    total_matrices = 0
    
    for _, row in completed_batches.iterrows():
        batch_id = row['batch_id']
        logger.info(f"\n--- Traitement du lot: {batch_id} ---")

        result_lines, batch = get_batch_results(client, batch_id)
        if not result_lines or not batch:
            logger.warning(f"Impossible de récupérer les résultats pour le lot {batch_id}. Passage au suivant.")
            continue
            
        original_script_path = find_original_script_path(batch, client)

        if not original_script_path or not original_script_path.exists():
            logger.error(f"Script original non trouvé pour le lot {batch_id}. Lot ignoré.")
            continue

        logger.info(f"Association du lot {batch_id} avec le fichier {original_script_path}")
        
        try:
            script_content = original_script_path.read_text(encoding="utf-8")
        except Exception as e:
            logger.error(f"Impossible de lire le fichier source {original_script_path}: {e}")
            continue
            
        analysis_results = reconstruct_analysis_from_batch_results(result_lines, script_content)
        
        if not analysis_results:
            logger.warning(f"Aucune donnée n'a pu être reconstruite pour le lot {batch_id}.")
            continue

        logger.info(f"Génération de la matrice pour: {original_script_path.name}")
        
        script_name_parts = original_script_path.parts
        if len(script_name_parts) >= 2:
            problem_folder = script_name_parts[-2]
            matrix_output_folder = MATRIX_DIR / problem_folder
            report_output_folder = REPORTS_DIR / problem_folder
        else:
            matrix_output_folder = MATRIX_DIR
            report_output_folder = REPORTS_DIR
        
        matrice, structure_tokens = construire_matrice_logprob(
            analysis_results, top_k=TOP_K_ALTERNATIVES
        )
        
        matrix_path = matrix_output_folder / f"matrix_{original_script_path.stem}.npy"
        sauvegarder_matrice_numpy(matrice, matrix_path)
        
        report_path = report_output_folder / f"report_{original_script_path.stem}.txt"
        sauvegarder_resultats_rapport(
            analysis_results,
            script_content,
            matrice,
            structure_tokens,
            report_path
        )
        
        total_matrices += 1

    logger.info(f"--- Fin du script. {total_matrices} matrices et rapports ont été générés. ---")

if __name__ == "__main__":
    main() 