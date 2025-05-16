#!/usr/bin/env python3
"""
Analyseur de prédictions token par token utilisant l'API Batch d'OpenAI
Adapté du script matrix_generator original pour soumettre les requêtes en lot.
"""
import os
import time
import json
import argparse
import tempfile
import tiktoken
import logging
import datetime
import numpy as np
from pathlib import Path
from openai import OpenAI

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

client = OpenAI(api_key="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")

class BatchRequestItem:
    def __init__(self, custom_id, context, model):
        self.custom_id = custom_id
        self.context = context
        self.model = model

    def to_jsonl(self):
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
                "logprobs": 10,
                "temperature": 0.0,
                "top_p": 0.1
            }
        }
        return json.dumps(req)

class BatchAnalyzer:
    def __init__(self, batch_size=5000, poll_interval=20):
        self.batch_size = batch_size
        self.poll_interval = poll_interval
        self.metadata_dir = Path("batch_metadata")
        self.metadata_dir.mkdir(exist_ok=True)

    def create_batch_file(self, items):
        fd, path = tempfile.mkstemp(suffix='.jsonl')
        os.close(fd)
        with open(path, 'w', encoding='utf-8') as f:
            for item in items:
                f.write(item.to_jsonl() + "\n")
        return path

    def submit_batch(self, items):
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

    def poll(self, batch_id):
        while True:
            batch = client.batches.retrieve(batch_id)
            logger.info(f"Batch {batch_id} status: {batch.status} "
                        f"{batch.request_counts.completed}/{batch.request_counts.total}")
            if batch.status == 'completed':
                return batch
            if batch.status in ['failed', 'cancelled', 'expired']:
                raise RuntimeError(f"Batch {batch_id} failed with status {batch.status}")
            time.sleep(self.poll_interval)

    def fetch_results(self, batch):
        # Préparer les répertoires de logs
        logs_dir = self.metadata_dir / "logs"
        raw_dir = self.metadata_dir / "raw_results"
        logs_dir.mkdir(exist_ok=True)
        raw_dir.mkdir(exist_ok=True)

        # Nom de base pour les fichiers liés à ce batch
        base = batch.id

        # Si pas de fichier de sortie, on regarde le fichier d'erreurs
        if not batch.output_file_id:
            if batch.error_file_id:
                err_txt = client.files.content(batch.error_file_id).text

                # Sauvegarde des erreurs brutes
                err_file = raw_dir / f"errors_{base}.jsonl"
                with open(err_file, 'w', encoding='utf-8') as f:
                    f.write(err_txt)

                # Journalisation dans un log dédié
                log_file = logs_dir / f"errors_{base}.log"
                with open(log_file, 'w', encoding='utf-8') as f:
                    f.write(f"=== Erreurs Batch {base} ===\n")
                    f.write(err_txt)

                logger.error(f"Batch {base} a échoué — erreurs enregistrées dans {err_file}")
                raise RuntimeError(f"Batch {base} completed with errors; see {err_file}")

            else:
                raise RuntimeError(f"Batch {base} n’a aucun fichier de sortie ni d’erreurs.")

        # Sinon, téléchargement du résultat brut
        output = client.files.content(batch.output_file_id).text

        # Sauvegarde du JSONL brut
        out_file = raw_dir / f"results_{base}.jsonl"
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(output)
        logger.info(f"Résultats bruts batch {base} enregistrés dans {out_file}")

        # Parse et journalisation détaillée
        results = {}
        log_file = logs_dir / f"fetch_{base}.log"
        with open(log_file, 'w', encoding='utf-8') as logf:
            logf.write(f"=== Détails du parsing Batch {base} ===\n")
            for line in output.strip().split('\n'):
                resp = json.loads(line)
                cid = resp.get('custom_id')
                if not cid:
                    logf.write(f"Ligne sans custom_id: {line}\n")
                    continue

                if resp.get('error'):
                    err = resp['error']
                    logf.write(f"[{cid}] ERREUR: {err}\n")
                    logger.error(f"[{cid}] {err}")
                    continue

                body = resp['response']['body']
                content = body['choices'][0]['message']['content']
                results[cid] = content

                # log each successful mapping
                logf.write(f"[{cid}] OK → contenu reçu (longueur {len(content)})\n")

        logger.info(f"Parsing batch {base} terminé — log détaillé dans {log_file}")
        return results


def tokeniser_avec_tiktoken(texte, modele="gpt-4o-mini"):
    try:
        encodeur = tiktoken.encoding_for_model(modele)
    except KeyError:
        encodeur = tiktoken.get_encoding("cl200k_base")
    token_ids = encodeur.encode(texte)
    tokens = [encodeur.decode_single_token_bytes(tid).decode('utf-8', errors='replace')
              for tid in token_ids]
    return token_ids, tokens

def analyser_par_batch(script,
                       modele_tokenisation="gpt-4o-mini",
                       modele_prediction="gpt-4o-mini",
                       batch_size=5000,
                       poll_interval=20):
    token_ids, tokens = tokeniser_avec_tiktoken(script, modele_tokenisation)
    amorce = max(1, min(3, len(tokens)//3))
    context = ''.join(tokens[:amorce])
    items = []
    for i in range(amorce, len(tokens)):
        cid = f"tok_{i}"
        items.append(BatchRequestItem(cid, context, modele_prediction))
        context += tokens[i]

    analyzer = BatchAnalyzer(batch_size=batch_size, poll_interval=poll_interval)
    batch_id = analyzer.submit_batch(items)
    batch = analyzer.poll(batch_id)
    raw_results = analyzer.fetch_results(batch)

    resultats = []
    # tokens d'amorce
    for i in range(amorce):
        resultats.append({"position": i, "attendu": tokens[i], "amorce": True})
    # prédictions
    for i in range(amorce, len(tokens)):
        pred = raw_results.get(f"tok_{i}", "")
        resultats.append({
            "position": i,
            "attendu": tokens[i],
            "predit": pred,
            "amorce": False
        })
    return resultats, tokens

def construire_matrice_logprob(tokens_reference, resultats_analyse, top_k=10):
    print("Construction de la matrice 2D de log probabilités...")
    texte_complet = ''.join(tokens_reference)
    lignes_texte = texte_complet.split('\n')
    if tokens_reference[-1] != '\n':
        lignes_texte[-1] = lignes_texte[-1]
    else:
        lignes_texte.append('')
    if lignes_texte[-1] == '':
        lignes_texte = lignes_texte[:-1]
    n_lignes = len(lignes_texte)
    tokens_par_ligne = []
    position_tokens = []
    ligne_courante = 0
    position_dans_ligne = 0
    for i, token in enumerate(tokens_reference):
        position_tokens.append((ligne_courante, position_dans_ligne))
        position_dans_ligne += 1
        if '\n' in token:
            tokens_par_ligne.append(position_dans_ligne)
            ligne_courante += 1
            position_dans_ligne = 0
            if ligne_courante >= n_lignes:
                break
    if ligne_courante < n_lignes and position_dans_ligne > 0:
        tokens_par_ligne.append(position_dans_ligne)
    max_tokens = max(tokens_par_ligne) if tokens_par_ligne else 0
    print(f"Structure du code: {n_lignes} lignes, {max_tokens} tokens max par ligne")
    matrice = np.full((n_lignes, max_tokens), 100.0)
    structure = {
        "lignes": n_lignes,
        "max_tokens": max_tokens,
        "tokens_par_ligne": tokens_par_ligne,
        "position_tokens": position_tokens
    }
    for idx, (i, j) in enumerate(position_tokens):
        if i < n_lignes and j < max_tokens:
            r = next((r for r in resultats_analyse if r["position"] == idx), None)
            if not r:
                matrice[i, j] = -50.0
            elif r.get("amorce", False):
                matrice[i, j] = -10.0
            else:
                att = r["attendu"]
                alts = r.get("alternatives", [])
                val = -50.0
                for alt in alts:
                    if alt["token"] == att or alt.get("token_adapte") == att:
                        val = alt["logprob"]; break
                if r.get("correct", False) or r.get("correct_adapte", False):
                    p = r["predit"]
                    for alt in alts:
                        if alt["token"] == p:
                            val = alt["logprob"]; break
                if not r.get("correct_top10", False):
                    val = -50.0
                matrice[i, j] = val
    return matrice, structure

def afficher_matrice_brute(matrice, structure_tokens):
    print("\nMATRICE BRUTE DE LOG PROBABILITÉS:")
    print(f"Dimensions: {matrice.shape[0]} lignes x {matrice.shape[1]} colonnes")
    max_w = 10
    sep = "-" * (max_w * matrice.shape[1] + 10)
    print(sep)
    print("     " + "".join(f"{j:^{max_w}}" for j in range(matrice.shape[1])))
    print("     " + "-" * (max_w * matrice.shape[1]))
    for i in range(matrice.shape[0]):
        row = ""
        for j in range(matrice.shape[1]):
            v = matrice[i, j]
            cell = "PAD" if v == 100 else ("ANOM" if v == -50 else f"{v:.4f}")
            row += f"{cell:^{max_w}}"
        print(f"{i:3d} | {row}")
    print(sep)
    print("Légende:")
    print("  - PAD  : Padding (valeur 100)")
    print("  - ANOM : Anomalie (valeur -50)")
    print("  - Autres valeurs : Log probabilités réelles")
    print(sep)

def sauvegarder_matrice_numpy(matrice, nom_fichier="matrice_logprob.npy"):
    np.save(nom_fichier, matrice)
    print(f"Matrice sauvegardée dans {nom_fichier}")

def sauvegarder_resultats(resultats_analyse, script, matrice, structure_tokens,
                          modele_tokenisation="gpt-4o-mini", nom_fichier=None):
    if nom_fichier is None:
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_fichier = f"analyse_tokens_{ts}.txt"
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\nANALYSE DES PRÉDICTIONS DE TOKENS\n" + "="*80 + "\n\n")
        f.write("SCRIPT ORIGINAL:\n" + "-"*80 + "\n")
        f.write(script + "\n" + "-"*80 + "\n\n")
        f.write("INFORMATION SUR LA TOKENISATION:\n" + "-"*80 + "\n")
        f.write(f"Tokenisation: tiktoken ({modele_tokenisation})\n" + "-"*80 + "\n\n")
        f.write("MATRICE 2D:\n" + "-"*80 + "\n")
        for i in range(matrice.shape[0]):
            row = []
            for j in range(matrice.shape[1]):
                v = matrice[i, j]
                row.append("PAD" if v == 100 else ("ANOM" if v == -50 else f"{v:.2f}"))
            f.write("[ " + ", ".join(row) + " ]\n")
        f.write("\nTOKEN-BY-TOKEN:\n" + "-"*80 + "\n")
        for r in resultats_analyse:
            pos = r["position"]
            if r.get("amorce", False):
                f.write(f"Position {pos}: amorce '{repr(r['attendu'])[1:-1]}'\n\n")
                continue
            a = repr(r['attendu'])[1:-1]
            p = repr(r.get('predit', ''))[1:-1]
            status = "✓" if r.get("correct", False) else "✗"
            f.write(f"Pos {pos}: attendu='{a}' préd='{p}' {status}\n")
        f.write("\n" + "="*80 + "\n")
    print(f"Résultats sauvegardés dans {nom_fichier}")
    return nom_fichier

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyse token par token en batch via l'API OpenAI"
    )
    parser.add_argument("--file", "-f", type=str, required=True,
                        help="Chemin du script à analyser")
    parser.add_argument("--token-model", "-t", type=str, default="gpt-4o-mini",
                        help="Modèle de tokenisation")
    parser.add_argument("--pred-model", "-p", type=str, default="gpt-4o-mini",
                        help="Modèle de prédiction")
    parser.add_argument("--batch-size", "-b", type=int, default=5000,
                        help="Taille du batch")
    parser.add_argument("--poll-interval", "-i", type=int, default=20,
                        help="Intervalle de poll (s)")
    args = parser.parse_args()

    script_path = Path(args.file)
    if not script_path.exists():
        raise FileNotFoundError(f"Fichier introuvable: {script_path}")
    script = script_path.read_text(encoding="utf-8")

    resultats_analyse, tokens_reference = analyser_par_batch(
        script,
        modele_tokenisation=args.token_model,
        modele_prediction=args.pred_model,
        batch_size=args.batch_size,
        poll_interval=args.poll_interval
    )

    matrice, structure = construire_matrice_logprob(tokens_reference, resultats_analyse)
    afficher_matrice_brute(matrice, structure)

    Path("matrix").mkdir(exist_ok=True)
    Path("results").mkdir(exist_ok=True)

    sauvegarder_matrice_numpy(
        matrice,
        nom_fichier=str(Path("matrix") / f"matrix_{script_path.stem}.npy")
    )
    sauvegarder_resultats(
        resultats_analyse,
        script,
        matrice,
        structure,
        modele_tokenisation=args.token_model,
        nom_fichier=str(Path("results") / f"result_{script_path.stem}.txt")
    )
