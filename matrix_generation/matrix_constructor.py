#!/usr/bin/env python3
"""
Script de construction de matrices à partir des résultats de batch téléchargés depuis l'API OpenAI.
Compatible avec le nouveau format d'ID (script_id:token_index) pour un traitement optimisé.
"""
import os
import argparse
import logging
import json
import numpy as np
import datetime
import shutil
from collections import defaultdict
from pathlib import Path

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def construire_matrice_logprob(tokens_reference, resultats_analyse):
    """
    Construit une matrice 2D de log probabilités avec taille dynamique,
    en padding avec 100 et anomalies à -50.
    """
    # 1) Reconstituer le texte complet et découper en lignes
    texte_complet = ''.join(tokens_reference)
    lignes_texte = texte_complet.split('\n')
    
    # Ajuster les lignes pour gérer les cas spéciaux
    if tokens_reference[-1] != '\n':
        lignes_texte[-1] = lignes_texte[-1]
    else:
        lignes_texte.append('')
    if lignes_texte[-1] == '':
        lignes_texte = lignes_texte[:-1]
    
    n_lignes = len(lignes_texte)
    
    # 2) Parcourir les tokens pour déterminer tokens_par_ligne et positions
    tokens_par_ligne = []
    position_tokens = []
    ligne_courante = 0
    position_dans_ligne = 0
    
    for i, token in enumerate(tokens_reference):
        # Enregistrer la position
        position_tokens.append((ligne_courante, position_dans_ligne))
        position_dans_ligne += 1
        
        # Si le token contient un saut de ligne, on change de ligne
        if '\n' in token:
            tokens_par_ligne.append(position_dans_ligne)
            ligne_courante += 1
            position_dans_ligne = 0
            if ligne_courante >= n_lignes:
                break
    
    # Ajouter la dernière ligne si nécessaire
    if ligne_courante < n_lignes and position_dans_ligne > 0:
        tokens_par_ligne.append(position_dans_ligne)
    
    # 3) Calculer les dimensions de la matrice
    max_tokens = max(tokens_par_ligne) if tokens_par_ligne else 0
    
    logger.info(f"Structure du code: {n_lignes} lignes, {max_tokens} tokens max par ligne")
    
    # 4) Initialiser la matrice de padding avec les dimensions dynamiques
    matrice = np.full((n_lignes, max_tokens), 100.0)
    
    structure = {
        "lignes": n_lignes,
        "max_tokens": max_tokens,
        "tokens_par_ligne": tokens_par_ligne,
        "position_tokens": position_tokens
    }
    
    # 5) Remplir la matrice avec log-probabilités ou valeurs spéciales
    for idx, (i, j) in enumerate(position_tokens):
        if i < n_lignes and j < max_tokens:
            resultat = next((r for r in resultats_analyse if r["position"] == idx), None)
            
            if not resultat:
                matrice[i, j] = -50.0  # Pas de résultat pour ce token
            else:
                attendu = resultat["attendu"]
                alternatives = resultat.get("alternatives", [])
                
                # Valeur par défaut pour anomalie
                val = -50.0
                
                # Chercher le token attendu dans les alternatives
                for alt in alternatives:
                    if alt["token"] == attendu:
                        val = alt["logprob"]
                        break
                
                # Si correct, prendre la logprob de la prédiction
                if resultat.get("correct", False):
                    predit = resultat["predit"]
                    for alt in alternatives:
                        if alt["token"] == predit:
                            val = alt["logprob"]
                            break
                
                # Si token attendu n'est pas dans le top 10
                if not resultat.get("correct_top10", False):
                    val = -50.0
                
                matrice[i, j] = val
    
    return matrice, structure

def sauvegarder_matrice_numpy(matrice, nom_fichier="matrice_logprob.npy"):
    """
    Sauvegarde la matrice au format numpy pour une utilisation ultérieure.
    """
    np.save(nom_fichier, matrice)
    logger.info(f"Matrice sauvegardée dans {nom_fichier}")

def sauvegarder_resultats(resultats_analyse, script_content, matrice, structure_tokens,
                         modele_tokenisation="gpt-4o-mini", nom_fichier=None):
    """
    Sauvegarde les résultats d'analyse dans un fichier texte bien formaté.
    """
    if nom_fichier is None:
        # Générer un nom de fichier basé sur la date et l'heure
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_fichier = f"analyse_tokens_{ts}.txt"
    
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        # Écrire l'en-tête
        f.write("="*80 + "\nANALYSE DES PRÉDICTIONS DE TOKENS\n" + "="*80 + "\n\n")
        
        # Écrire le script original
        f.write("SCRIPT ORIGINAL:\n" + "-"*80 + "\n")
        f.write(script_content + "\n" + "-"*80 + "\n\n")
        
        # Écrire l'information sur la tokenisation
        f.write("INFORMATION SUR LA TOKENISATION:\n" + "-"*80 + "\n")
        f.write(f"Tokenisation: tiktoken ({modele_tokenisation})\n" + "-"*80 + "\n\n")
        
        # Écrire la matrice 2D
        f.write("MATRICE 2D:\n" + "-"*80 + "\n")
        for i in range(matrice.shape[0]):
            row = []
            for j in range(matrice.shape[1]):
                v = matrice[i, j]
                row.append("PAD" if v == 100 else ("ANOM" if v == -50 else f"{v:.2f}"))
            f.write("[ " + ", ".join(row) + " ]\n")
        
        # Écrire les résultats d'analyse token par token
        f.write("\nTOKEN-BY-TOKEN:\n" + "-"*80 + "\n")
        for r in resultats_analyse:
            pos = r["position"]
            a = repr(r['attendu'])[1:-1]
            p = repr(r.get('predit', ''))[1:-1]
            status = "✓" if r.get("correct", False) else "✗"
            f.write(f"Pos {pos}: attendu='{a}' préd='{p}' {status}\n")
            
            # Ajouter les alternatives si disponibles
            alts = r.get("alternatives", [])
            if alts:
                f.write("  Alternatives:\n")
                for i, alt in enumerate(alts[:10]):  # Limiter aux 10 premières alternatives
                    alt_token = repr(alt["token"])[1:-1]
                    alt_logprob = alt["logprob"]
                    f.write(f"    {i+1}. '{alt_token}' (logprob: {alt_logprob:.4f})")
                    if alt["token"] == r.get("predit", ""):
                        f.write(" [Prédiction principale]")
                    if alt["token"] == r["attendu"]:
                        f.write(" [Token attendu]")
                    f.write("\n")
                f.write("\n")
        
        # Ajouter un résumé
        correct_tokens = len([r for r in resultats_analyse if r.get("correct", False)])
        correct_top10 = len([r for r in resultats_analyse if r.get("correct_top10", False)])
        total_tokens = len(resultats_analyse)
        
        f.write("\nRÉSUMÉ:\n" + "-"*80 + "\n")
        f.write(f"Total des tokens analysés: {total_tokens}\n")
        f.write(f"Tokens correctement prédits (1ère position): {correct_tokens}\n")
        f.write(f"Tokens correctement prédits (top 10): {correct_top10}\n")
        
        if total_tokens > 0:
            f.write(f"Précision (1ère position): {(correct_tokens / total_tokens) * 100:.2f}%\n")
            f.write(f"Précision (top 10): {(correct_top10 / total_tokens) * 100:.2f}%\n")
        
        f.write("\n" + "="*80 + "\n")
    
    logger.info(f"Résultats sauvegardés dans {nom_fichier}")
    return nom_fichier

def deplacer_resultats_batch(results_files, archive_dir):
    """
    Déplace les fichiers de résultats vers le dossier d'archives après traitement.
    
    Args:
        results_files (list): Liste des chemins des fichiers de résultats
        archive_dir (Path): Répertoire d'archivage
    """
    archive_dir.mkdir(exist_ok=True, parents=True)
    
    moved_count = 0
    for file_path in results_files:
        try:
            # Préserver uniquement le nom du fichier
            archive_path = archive_dir / file_path.name
            
            # En cas de conflit de noms, ajouter un timestamp
            if archive_path.exists():
                stem = archive_path.stem
                suffix = archive_path.suffix
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                archive_path = archive_dir / f"{stem}_{timestamp}{suffix}"
            
            # Déplacer le fichier
            shutil.move(str(file_path), str(archive_path))
            logger.info(f"Fichier de résultats déplacé: {file_path} → {archive_path}")
            moved_count += 1
        except Exception as e:
            logger.error(f"Erreur lors du déplacement du fichier {file_path}: {e}")
    
    logger.info(f"{moved_count}/{len(results_files)} fichiers de résultats déplacés avec succès")

def charger_info_tokens(tokens_dir):
    """
    Charge les informations sur les tokens depuis les fichiers d'information.
    Prend en charge les fichiers simples (nom_du_script__N_tokens.json) et les anciens .tokens_info.json.
    
    Args:
        tokens_dir (Path): Répertoire contenant les fichiers d'information sur les tokens
        
    Returns:
        dict: Dictionnaire contenant les informations sur les tokens par script_id ou script_name
    """
    tokens_info = {}
    
    # Chercher tous les fichiers simples de tokens (nom explicite)
    simple_files = list(tokens_dir.glob("*__*_tokens.json"))
    if simple_files:
        for simple_file in simple_files:
            try:
                with open(simple_file, "r", encoding="utf-8") as f:
                    simple_tokens = json.load(f)
                # Récupérer le nom du script et le nombre de tokens depuis le nom du fichier
                name_part = simple_file.name.rsplit("__", 1)[0]
                script_name = name_part
                tokens = [t["token"] for t in simple_tokens]
                tokens_info[script_name] = {
                    "script_name": script_name,
                    "tokens": tokens
                }
                logger.info(f"Tokens chargés depuis {simple_file}")
            except Exception as e:
                logger.error(f"Erreur lors du chargement des tokens depuis {simple_file}: {e}")
        return tokens_info
    # Sinon, fallback sur l'ancien format
    info_files = list(tokens_dir.glob("*.tokens_info.json"))
    if not info_files:
        logger.warning(f"Aucun fichier d'information sur les tokens trouvé dans {tokens_dir}")
        return tokens_info
    for info_file in info_files:
        try:
            with open(info_file, "r", encoding="utf-8") as f:
                script_data = json.load(f)
            script_id = script_data.get("script_id", script_data.get("script_name", info_file.stem))
            tokens_info[script_id] = script_data
            logger.info(f"Informations sur les tokens chargées depuis {info_file}")
        except Exception as e:
            logger.error(f"Erreur lors du chargement des informations depuis {info_file}: {e}")
    return tokens_info

def parser_resultats_batch(results_dir):
    """
    Parse les fichiers de résultats de batch téléchargés depuis l'API OpenAI.
    
    Args:
        results_dir (Path): Répertoire contenant les fichiers de résultats
        
    Returns:
        dict: Dictionnaire contenant les résultats par script_id et token_index
    """
    # Format de résultats: {script_id: {token_index: résultat}}
    resultats_par_script = defaultdict(dict)
    
    # Chercher tous les fichiers de résultats
    results_files = []
    for ext in [".jsonl", ".json"]:
        results_files.extend(list(results_dir.glob(f"*{ext}")))
    
    if not results_files:
        logger.warning(f"Aucun fichier de résultats trouvé dans {results_dir}")
        return resultats_par_script, []
    
    # Parser chaque fichier
    for results_file in results_files:
        logger.info(f"Parsing du fichier de résultats {results_file}")
        
        try:
            with open(results_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for line in lines:
                if not line.strip():
                    continue
                
                try:
                    resp = json.loads(line)
                    custom_id = resp.get('custom_id')
                    
                    if not custom_id:
                        logger.warning(f"Ligne sans custom_id trouvée dans {results_file}, ignorée")
                        continue
                    
                    # Format du custom_id: script_id:token_index
                    parts = custom_id.split(':')
                    if len(parts) != 2:
                        logger.warning(f"ID mal formaté: {custom_id}, ignoré")
                        continue
                    
                    script_id, token_index = parts
                    token_index = int(token_index)
                    
                    # Vérifier si la réponse contient une erreur
                    if resp.get('error'):
                        logger.error(f"[{custom_id}] {resp['error']}")
                        continue
                    
                    # Extraire le contenu et les alternatives
                    body = resp['response']['body']
                    content = body['choices'][0]['message']['content']
                    
                    # Extraction des logprobs
                    top_logprobs = []
                    logprobs_data = body['choices'][0].get('logprobs', {})
                    
                    if 'content' in logprobs_data and logprobs_data['content']:
                        first_token = logprobs_data['content'][0]
                        if 'top_logprobs' in first_token:
                            top_logprobs = first_token['top_logprobs']
                    
                    # Convertir les logprobs
                    alternatives = []
                    for item in top_logprobs:
                        alternatives.append({
                            "token": item.get('token', ''),
                            "logprob": item.get('logprob', -100)
                        })
                    
                    # Stocker le résultat
                    resultats_par_script[script_id][token_index] = {
                        "content": content,
                        "alternatives": alternatives
                    }
                    
                except Exception as e:
                    logger.error(f"Erreur lors du parsing d'une ligne dans {results_file}: {e}")
            
            logger.info(f"Parsing de {results_file} terminé")
            
        except Exception as e:
            logger.error(f"Erreur lors du chargement du fichier {results_file}: {e}")
    
    return resultats_par_script, results_files

def reconstruire_resultats_analyse(tokens_info, resultats_par_script):
    """
    Reconstruit les résultats d'analyse à partir des informations sur les tokens et des résultats de batch.
    
    Args:
        tokens_info (dict): Dictionnaire contenant les informations sur les tokens par script_id
        resultats_par_script (dict): Dictionnaire contenant les résultats par script_id et token_index
        
    Returns:
        dict: Dictionnaire contenant les résultats d'analyse par script_id
    """
    resultats_analyse = {}
    
    for script_id, script_info in tokens_info.items():
        if script_id not in resultats_par_script:
            logger.warning(f"Aucun résultat trouvé pour le script {script_id}, ignoré")
            continue
        
        script_results = resultats_par_script[script_id]
        tokens = script_info["tokens"]
        
        # Créer les résultats d'analyse pour ce script
        resultats = []
        
        for i, token in enumerate(tokens):
            if i in script_results:
                # Résultat disponible pour ce token
                result = script_results[i]
                predit = result["content"]
                alternatives = result["alternatives"]
                
                # Vérifier si la prédiction est correcte
                correct = predit == token
                correct_top10 = correct or any(alt["token"] == token for alt in alternatives)
                
                resultats.append({
                    "position": i,
                    "attendu": token,
                    "predit": predit,
                    "correct": correct,
                    "correct_top10": correct_top10,
                    "alternatives": alternatives
                })
            else:
                # Pas de résultat pour ce token
                resultats.append({
                    "position": i,
                    "attendu": token,
                    "predit": "ERROR",
                    "correct": False,
                    "correct_top10": False,
                    "alternatives": []
                })
        
        resultats_analyse[script_id] = resultats
    
    return resultats_analyse

def construire_matrices(tokens_dir, results_dir, output_dir, archive_dir, modele_tokenisation="gpt-4o-mini"):
    """
    Construit des matrices à partir des informations sur les tokens et des résultats de batch.
    
    Args:
        tokens_dir (Path): Répertoire contenant les informations sur les tokens
        results_dir (Path): Répertoire contenant les résultats de batch
        output_dir (Path): Répertoire de sortie pour les matrices et rapports
        archive_dir (Path): Répertoire d'archivage pour les fichiers de résultats traités
        modele_tokenisation (str): Modèle de tokenisation utilisé
        
    Returns:
        list: Liste des chemins des fichiers de rapports générés
    """
    # Créer les répertoires de sortie
    matrices_dir = output_dir / "matrixes"
    rapports_dir = matrices_dir / "reports"
    matrices_dir.mkdir(exist_ok=True, parents=True)
    rapports_dir.mkdir(exist_ok=True, parents=True)
    
    # Charger les informations sur les tokens
    tokens_info = charger_info_tokens(tokens_dir)
    
    if not tokens_info:
        logger.error("Aucune information sur les tokens disponible, impossible de construire les matrices")
        return []
    
    # Parser les résultats de batch
    resultats_par_script, results_files = parser_resultats_batch(results_dir)
    
    if not resultats_par_script:
        logger.error("Aucun résultat de batch disponible, impossible de construire les matrices")
        return []
    
    # Reconstruire les résultats d'analyse
    resultats_analyse = reconstruire_resultats_analyse(tokens_info, resultats_par_script)
    
    # Liste pour stocker les chemins des fichiers de rapports générés
    report_files = []
    
    # Construire les matrices pour chaque script
    for script_id, resultats in resultats_analyse.items():
        try:
            script_info = tokens_info[script_id]
            script_name = script_info["script_name"]
            tokens = script_info["tokens"]
            
            logger.info(f"Construction de la matrice pour {script_name}")
            
            # Reconstruire le contenu du script à partir des tokens
            script_content = ''.join(tokens)
            
            # Construire la matrice
            matrice, structure = construire_matrice_logprob(tokens, resultats)
            
            # Sauvegarder la matrice
            matrix_file = matrices_dir / f"matrix_{script_name}.npy"
            sauvegarder_matrice_numpy(matrice, nom_fichier=str(matrix_file))
            
            # Sauvegarder les résultats
            report_file = rapports_dir / f"report_{script_name}.txt"
            sauvegarder_resultats(
                resultats,
                script_content,
                matrice,
                structure,
                modele_tokenisation=modele_tokenisation,
                nom_fichier=str(report_file)
            )
            
            report_files.append(report_file)
            
            # Afficher un résumé
            correct_tokens = len([r for r in resultats if r.get("correct", False)])
            correct_top10 = len([r for r in resultats if r.get("correct_top10", False)])
            total_tokens = len(resultats)
            
            if total_tokens > 0:
                precision = (correct_tokens / total_tokens) * 100
                precision_top10 = (correct_top10 / total_tokens) * 100
                logger.info(f"Résumé pour {script_name}: Précision = {precision:.2f}%, Précision top 10 = {precision_top10:.2f}%")
            
        except Exception as e:
            logger.error(f"Erreur lors de la construction de la matrice pour {script_id}: {e}")
            import traceback
            logger.error(traceback.format_exc())
    
    # Déplacer les fichiers de résultats si des matrices ont été générées avec succès
    if report_files and archive_dir:
        deplacer_resultats_batch(results_files, archive_dir)
    
    return report_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script de construction de matrices à partir des résultats de batch"
    )
    parser.add_argument("--tokens-dir", "-t", type=str, required=True,
                        help="Répertoire contenant les informations sur les tokens")
    parser.add_argument("--results-dir", "-r", type=str, required=True,
                        help="Répertoire contenant les résultats de batch")
    parser.add_argument("--output-dir", "-o", type=str, required=True,
                        help="Répertoire de sortie pour les matrices et rapports")
    parser.add_argument("--archive-dir", "-a", type=str, required=True,
                        help="Répertoire d'archivage pour les fichiers de résultats traités")
    parser.add_argument("--token-model", "-m", type=str, default="gpt-4o-mini",
                        help="Modèle de tokenisation utilisé (par défaut: gpt-4o-mini)")
    
    args = parser.parse_args()
    
    # Convertir les chemins en objets Path
    tokens_dir = Path(args.tokens_dir)
    results_dir = Path(args.results_dir)
    output_dir = Path(args.output_dir)
    archive_dir = Path(args.archive_dir)
    
    try:
        # Construire les matrices
        report_files = construire_matrices(
            tokens_dir=tokens_dir,
            results_dir=results_dir,
            output_dir=output_dir,
            archive_dir=archive_dir,
            modele_tokenisation=args.token_model
        )
        
        if report_files:
            logger.info(f"Construction des matrices terminée avec succès!")
            logger.info(f"Nombre de scripts traités: {len(report_files)}")
            logger.info(f"Les matrices sont disponibles dans: {output_dir}/matrixes/")
            logger.info(f"Les rapports sont disponibles dans: {output_dir}/matrixes/reports/")
            logger.info(f"Les fichiers de résultats ont été déplacés vers: {archive_dir}")
        else:
            logger.warning("Aucun fichier n'a été traité avec succès.")
        
    except Exception as e:
        logger.error(f"Erreur lors de la construction des matrices: {e}")
        import traceback
        logger.error(traceback.format_exc())
        exit(1)