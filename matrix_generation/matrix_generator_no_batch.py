#!/usr/bin/env python3
"""
Analyseur de prédictions token par token avec OpenAI (Mode Standard uniquement)
Peut analyser un fichier unique ou tous les fichiers Python d'un dossier
"""
import os
import time
import json
import argparse
import tiktoken
import logging
import datetime
import numpy as np
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

#######################
# FONCTIONS COMMUNES #
#######################

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
        # Obtenir l'encodeur correspondant au modèle
        encodeur = tiktoken.encoding_for_model(modele)
    except KeyError:
        # Si le modèle n'est pas disponible, utiliser l'encodeur cl200k_base
        logger.warning(f"Encodeur pour {modele} non trouvé, utilisation de cl200k_base à la place.")
        encodeur = tiktoken.get_encoding("cl200k_base")
    
    # Encoder le texte en tokens (IDs numériques)
    token_ids = encodeur.encode(texte)
    
    # Convertir les IDs en tokens (chaînes de caractères)
    tokens = [encodeur.decode_single_token_bytes(token_id).decode('utf-8', errors='replace') 
              for token_id in token_ids]
    
    return token_ids, tokens

def construire_matrice_logprob(tokens_reference, resultats_analyse, top_k=10):
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
                matrice[i, j] = -50.0
            elif resultat.get("amorce", False):
                matrice[i, j] = -10.0
            else:
                attendu = resultat["attendu"]
                alternatives = resultat.get("alternatives", [])
                
                # Valeur par défaut pour anomalie
                val = -50.0
                
                # Chercher le token attendu dans les alternatives
                for alt in alternatives:
                    if alt["token"] == attendu or alt.get("token_adapte") == attendu:
                        val = alt["logprob"]
                        break
                
                # Si correct (stricte ou adaptée), prendre la logprob de la prédiction
                if resultat.get("correct", False) or resultat.get("correct_adapte", False):
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

def afficher_matrice_brute(matrice, structure_tokens):
    """
    Affiche la matrice 2D de log probabilités brute dans la console
    """
    print("\nMATRICE BRUTE DE LOG PROBABILITÉS:")
    print(f"Dimensions: {matrice.shape[0]} lignes x {matrice.shape[1]} colonnes")
    
    # Calculer la largeur maximale pour l'affichage
    max_w = 10  # Largeur par défaut pour chaque valeur
    
    # Créer une ligne de séparation
    sep = "-" * (max_w * matrice.shape[1] + 10)
    print(sep)
    
    # Afficher les indices de colonnes
    print("     ", end="")
    for j in range(matrice.shape[1]):
        print(f"{j:^{max_w}}", end="")
    print()  # Nouvelle ligne
    
    # Ligne de séparation après les indices de colonnes
    print("     " + "-" * (max_w * matrice.shape[1]))
    
    # Afficher chaque ligne avec son indice
    for i in range(matrice.shape[0]):
        print(f"{i:3d} |", end="")
        for j in range(matrice.shape[1]):
            val = matrice[i, j]
            if val == 100:
                # Padding
                cell = "PAD"
            elif val == -50:
                # Anomalie
                cell = "ANOM"
            else:
                # Log probabilité normale
                cell = f"{val:.4f}"
            print(f"{cell:^{max_w}}", end="")
        print()  # Nouvelle ligne
    
    # Ligne de séparation finale
    print(sep)
    
    # Légende
    print("Légende:")
    print("  - PAD  : Padding (valeur 100)")
    print("  - ANOM : Anomalie (valeur -50)")
    print("  - Autres valeurs : Log probabilités réelles")
    print(sep)

def sauvegarder_matrice_numpy(matrice, nom_fichier="matrice_logprob.npy"):
    """
    Sauvegarde la matrice au format numpy pour une utilisation ultérieure.
    """
    np.save(nom_fichier, matrice)
    logger.info(f"Matrice sauvegardée dans {nom_fichier}")

def sauvegarder_resultats(resultats_analyse, script, matrice, structure_tokens,
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
        f.write(script + "\n" + "-"*80 + "\n\n")
        
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
            if r.get("amorce", False):
                f.write(f"Position {pos}: amorce '{repr(r['attendu'])[1:-1]}'\n\n")
                continue
            
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
        tokens_non_amorce = [r for r in resultats_analyse if not r.get("amorce", False)]
        correct_tokens = len([r for r in tokens_non_amorce if r.get("correct", False)])
        correct_adapte = len([r for r in tokens_non_amorce if r.get("correct_adapte", False)])
        correct_top10 = len([r for r in tokens_non_amorce if r.get("correct_top10", False)])
        total_tokens = len(tokens_non_amorce)
        
        f.write("\nRÉSUMÉ:\n" + "-"*80 + "\n")
        f.write(f"Total des tokens analysés: {total_tokens}\n")
        f.write(f"Tokens correctement prédits (1ère position, stricte): {correct_tokens}\n")
        f.write(f"Tokens correctement prédits (1ère position, avec adaptation): {correct_adapte}\n")
        f.write(f"Tokens correctement prédits (top 10): {correct_top10}\n")
        
        if total_tokens > 0:
            f.write(f"Précision stricte: {(correct_tokens / total_tokens) * 100:.2f}%\n")
            f.write(f"Précision adaptée: {(correct_adapte / total_tokens) * 100:.2f}%\n")
            f.write(f"Précision top 10: {(correct_top10 / total_tokens) * 100:.2f}%\n")
        
        f.write("\n" + "="*80 + "\n")
    
    logger.info(f"Résultats sauvegardés dans {nom_fichier}")
    return nom_fichier

def analyser_sans_batch(script, modele_tokenisation="gpt-4o-mini", modele_prediction="gpt-4o-mini"):
    """
    Analyse le script token par token en mode standard.
    Fait une requête API séparée pour chaque token.
    """
    logger.info(f"Démarrage de l'analyse token par token avec tokenisation tiktoken ({modele_tokenisation})...")
    
    # Tokeniser le script avec tiktoken
    token_ids, tokens_reference = tokeniser_avec_tiktoken(script, modele_tokenisation)
    
    logger.info(f"Nombre de tokens dans la référence tiktoken: {len(tokens_reference)}")
    
    # Nouvelle liste pour stocker les résultats d'analyse
    resultats_analyse = []
    
    # Ajuster dynamiquement le nombre de tokens d'amorce
    amorce_tokens = max(1, min(3, len(tokens_reference) // 3))
    logger.info(f"Utilisation de {amorce_tokens} tokens comme amorce sur {len(tokens_reference)} tokens au total")
    
    # Initialiser le contexte avec les tokens d'amorce
    contexte_initial = ""
    for i in range(min(amorce_tokens, len(tokens_reference))):
        contexte_initial += tokens_reference[i]
        
        # Ajouter à notre liste de résultats (sans prédiction pour l'amorce)
        resultats_analyse.append({
            "position": i,
            "token_id": token_ids[i],
            "attendu": tokens_reference[i],
            "amorce": True,
            "alternatives": []
        })
    
    contexte_actuel = contexte_initial
    
    # Analyser token par token à partir du premier token après l'amorce
    logger.info("Analyse des tokens un par un...")
    for i in tqdm(range(amorce_tokens, len(tokens_reference))):
        token_attendu = tokens_reference[i]
        token_id_attendu = token_ids[i]
        
        # Vérifier si le token précédent est une tabulation
        token_precedent_est_tabulation = False
        if i > 0:
            token_precedent = tokens_reference[i-1]
            if "\n" not in token_precedent:
                token_precedent_est_tabulation = token_precedent.strip() == "" and len(token_precedent) > 1
        
        try:
            # Demander explicitement le token suivant avec ses alternatives
            response = client.chat.completions.create(
                model=modele_prediction,
                messages=[
                    {"role": "system", "content": "You are a code predictor that generates only the next token without any additional text. Pay attention to spaces, tabs, line breaks, and special symbols in the code."},
                    {"role": "user", "content": f"Code context: {contexte_actuel}"}
                ],
                max_tokens=1,
                logprobs=True,
                top_logprobs=10,  
                temperature=0.0,
                top_p=0.1
            )
            
            # Extraire le token prédit et ses alternatives
            token_predit = response.choices[0].logprobs.content[0].token
            alternatives = [{"token": alt.token, "logprob": alt.logprob} 
                           for alt in response.choices[0].logprobs.content[0].top_logprobs]
            
            # Initialiser les flags pour la correction standard et la correction adaptée
            correct = token_predit == token_attendu
            correct_adapte = correct
            
            # Appliquer la règle spéciale pour les tokens après tabulation
            if token_precedent_est_tabulation and token_attendu.startswith(" ") and token_attendu.strip():
                # Si le token sans espace correspond à la prédiction, marquer comme correct adapté
                token_sans_espace = token_attendu.lstrip(" ")
                correct_adapte = correct or token_predit == token_sans_espace
                
                # Ajouter une version adaptée aux alternatives pour affichage
                for alt in alternatives:
                    if alt["token"] == token_sans_espace:
                        alt["token_adapte"] = token_attendu
                        alt["adapte"] = True
            
            # Vérifier si le token attendu ou sa version adaptée est dans les alternatives
            token_dans_top10 = correct or correct_adapte or any(alt["token"] == token_attendu for alt in alternatives) or any(alt.get("adapte", False) for alt in alternatives)
            
            # Ajouter le résultat à notre liste
            resultats_analyse.append({
                "position": i,
                "token_id": token_id_attendu,
                "attendu": token_attendu,
                "predit": token_predit,
                "correct": correct,
                "correct_adapte": correct_adapte,
                "correct_top10": token_dans_top10,
                "alternatives": alternatives,
                "token_precedent_est_tabulation": token_precedent_est_tabulation,
                "amorce": False
            })
            
            # Mettre à jour le contexte pour la prochaine itération avec le token attendu
            contexte_actuel += token_attendu
            
            # Pause pour respecter le rate limit
            time.sleep(0.5)
            
        except Exception as e:
            logger.error(f"Erreur lors de la requête pour le token {i}: {e}")
            
            # Stocker une prédiction avec erreur
            resultats_analyse.append({
                "position": i,
                "token_id": token_id_attendu,
                "attendu": token_attendu,
                "predit": "ERROR",
                "correct": False,
                "correct_adapte": False,
                "correct_top10": False,
                "alternatives": [],
                "token_precedent_est_tabulation": token_precedent_est_tabulation,
                "amorce": False
            })
            
            # Continuer avec le token attendu
            contexte_actuel += token_attendu
    
    return resultats_analyse, tokens_reference

#######################
# FONCTION PRINCIPALE #
#######################

def analyser_script(script_path, output_dir=None, modele_tokenisation="gpt-4o-mini", 
                   modele_prediction="gpt-4o-mini"):
    """
    Fonction principale qui analyse un script token par token.
    
    Args:
        script_path (Path): Chemin vers le script à analyser
        output_dir (Path): Répertoire de sortie pour les résultats
        modele_tokenisation (str): Modèle utilisé pour la tokenisation
        modele_prediction (str): Modèle utilisé pour la prédiction
    
    Returns:
        tuple: Chemin du fichier matrice et chemin du fichier résultats
    """
    # Charger le script
    if not script_path.exists():
        raise FileNotFoundError(f"Fichier introuvable: {script_path}")
    
    script = script_path.read_text(encoding="utf-8")
    logger.info(f"Script chargé depuis {script_path} ({len(script)} caractères)")
    
    # Analyser le script
    logger.info("Utilisation du mode standard (une requête par token)")
    resultats_analyse, tokens_reference = analyser_sans_batch(
        script, 
        modele_tokenisation=modele_tokenisation,
        modele_prediction=modele_prediction
    )
    
    # Construire la matrice de log probabilités
    matrice, structure = construire_matrice_logprob(tokens_reference, resultats_analyse)
    
    # Afficher la matrice brute
    afficher_matrice_brute(matrice, structure)
    
    # Créer les répertoires de sortie si nécessaire
    if output_dir is None:
        output_dir = Path(".")
    
    # Déterminer le répertoire parent pour suivre l'arborescence demandée
    base_dir = output_dir
    
    # Créer les chemins pour les répertoires de sortie
    matrices_dir = base_dir / "matrixes"
    rapports_dir = matrices_dir / "reports"
    tokens_dir = base_dir / "tokens_info"
    matrices_dir.mkdir(exist_ok=True, parents=True)
    rapports_dir.mkdir(exist_ok=True, parents=True)
    tokens_dir.mkdir(exist_ok=True, parents=True)
    
    # Générer les noms de fichiers
    matrix_file = matrices_dir / f"matrix_{script_path.stem}.npy"
    result_file = rapports_dir / f"result_{script_path.stem}.txt"
    
    # Sauvegarder la matrice et les résultats
    sauvegarder_matrice_numpy(matrice, nom_fichier=str(matrix_file))
    sauvegarder_resultats(
        resultats_analyse,
        script,
        matrice,
        structure,
        modele_tokenisation=modele_tokenisation,
        nom_fichier=str(result_file)
    )
    # Sauvegarder le fichier JSON de tokens pour ce script
    simple_tokens = [{"token": t} for t in tokens_reference]
    simple_file = tokens_dir / f"{script_path.name}__{len(tokens_reference)}_tokens.json"
    with open(simple_file, "w", encoding="utf-8") as f:
        json.dump(simple_tokens, f, ensure_ascii=False, indent=2)
    logger.info(f"Fichier simple de tokens sauvegardé pour {script_path.name} dans {simple_file}")
    
    # Afficher le résumé
    tokens_non_amorce = [r for r in resultats_analyse if not r.get("amorce", False)]
    correct_tokens = len([r for r in tokens_non_amorce if r.get("correct", False)])
    correct_adapte = len([r for r in tokens_non_amorce if r.get("correct_adapte", False)])
    correct_top10 = len([r for r in tokens_non_amorce if r.get("correct_top10", False)])
    total_tokens = len(tokens_non_amorce)
    
    logger.info("\nRésumé de l'analyse:")
    logger.info(f"Total des tokens analysés: {total_tokens}")
    logger.info(f"Tokens correctement prédits (1ère position, stricte): {correct_tokens}")
    logger.info(f"Tokens correctement prédits (1ère position, avec adaptation): {correct_adapte}")
    logger.info(f"Tokens correctement prédits (top 10): {correct_top10}")
    
    if total_tokens > 0:
        precision = (correct_tokens / total_tokens) * 100
        precision_adapte = (correct_adapte / total_tokens) * 100
        precision_top10 = (correct_top10 / total_tokens) * 100
        logger.info(f"Précision (1ère position, stricte): {precision:.2f}%")
        logger.info(f"Précision (1ère position, avec adaptation): {precision_adapte:.2f}%")
        logger.info(f"Précision (top 10): {precision_top10:.2f}%")
    
    return matrix_file, result_file

def traiter_dossier(directory_path, output_dir=None, modele_tokenisation="gpt-4o-mini", 
                   modele_prediction="gpt-4o-mini"):
    """
    Traite tous les fichiers Python d'un dossier en cherchant dans le sous-dossier "scripts".
    
    Args:
        directory_path (Path): Chemin vers le dossier parent
        output_dir (Path): Répertoire de sortie pour les résultats
        modele_tokenisation (str): Modèle utilisé pour la tokenisation
        modele_prediction (str): Modèle utilisé pour la prédiction
    
    Returns:
        list: Liste des chemins des fichiers de résultats générés
    """
    if not directory_path.exists() or not directory_path.is_dir():
        raise NotADirectoryError(f"Le chemin spécifié n'est pas un dossier valide: {directory_path}")
    
    # Construire le chemin vers le sous-dossier "scripts"
    scripts_dir = directory_path / "scripts"
    
    if not scripts_dir.exists() or not scripts_dir.is_dir():
        raise NotADirectoryError(f"Le sous-dossier 'scripts' n'existe pas dans {directory_path}")
    
    # Créer le répertoire de sortie (si non spécifié, utiliser le répertoire parent)
    if output_dir is None:
        output_dir = directory_path
    
    # Trouver tous les fichiers Python dans le sous-dossier
    python_files = list(scripts_dir.glob("*.py"))
    if not python_files:
        logger.warning(f"Aucun fichier Python (.py) trouvé dans le dossier {scripts_dir}")
        return []
    
    logger.info(f"Trouvé {len(python_files)} fichiers Python à analyser dans {scripts_dir}")
    
    # Liste pour stocker les chemins des fichiers de résultats
    results_files = []
    
    # Traiter chaque fichier Python
    for i, file_path in enumerate(python_files):
        logger.info(f"Traitement du fichier {i+1}/{len(python_files)}: {file_path.name}")
        try:
            matrix_file, result_file = analyser_script(
                script_path=file_path,
                output_dir=output_dir,
                modele_tokenisation=modele_tokenisation,
                modele_prediction=modele_prediction
            )
            results_files.append(result_file)
            logger.info(f"Analyse terminée pour {file_path.name}")
        except Exception as e:
            logger.error(f"Erreur lors de l'analyse de {file_path.name}: {e}")
            import traceback
            logger.error(traceback.format_exc())
            
    logger.info(f"Traitement du dossier terminé. {len(results_files)}/{len(python_files)} fichiers traités avec succès.")
    return results_files

def generer_matrices_depuis_tokens_dir(tokens_dir, output_dir=None, modele_tokenisation="gpt-4o-mini"):
    """
    Pour chaque fichier *_tokens.json dans tokens_dir, reconstruit le script, génère la matrice et le rapport.
    """
    tokens_dir = Path(tokens_dir)
    if output_dir is None:
        output_dir = tokens_dir.parent
    output_dir = Path(output_dir)
    matrices_dir = output_dir / "matrixes"
    rapports_dir = matrices_dir / "reports"
    matrices_dir.mkdir(exist_ok=True, parents=True)
    rapports_dir.mkdir(exist_ok=True, parents=True)
    
    # Pour chaque fichier *_tokens.json
    for json_file in tokens_dir.glob("*__*_tokens.json"):
        script_name = json_file.name.split("__")[0]
        with open(json_file, "r", encoding="utf-8") as f:
            tokens_list = json.load(f)
        tokens = [t["token"] for t in tokens_list]
        script = ''.join(tokens)
        
        # Tokenisation déjà faite, on utilise les tokens du fichier
        # On simule une analyse "parfaite" (attendu = prédit)
        resultats_analyse = []
        for i, token in enumerate(tokens):
            resultats_analyse.append({
                "position": i,
                "attendu": token,
                "predit": token,
                "correct": True,
                "correct_top10": True,
                "alternatives": []
            })
        
        matrice, structure = construire_matrice_logprob(tokens, resultats_analyse)
        matrix_file = matrices_dir / f"matrix_{script_name}.npy"
        report_file = rapports_dir / f"report_{script_name}.txt"
        
        sauvegarder_matrice_numpy(matrice, nom_fichier=str(matrix_file))
        sauvegarder_resultats(
            resultats_analyse,
            script,
            matrice,
            structure,
            modele_tokenisation=modele_tokenisation,
            nom_fichier=str(report_file)
        )
        logger.info(f"Matrice et rapport générés pour {script_name} depuis {json_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyseur de prédictions token par token avec OpenAI (Mode Standard)"
    )
    parser.add_argument("--file", "-f", type=str, default=None,
                        help="Chemin du script à analyser")
    parser.add_argument("--directory", "-d", type=str, default=None,
                        help="Chemin vers un dossier contenant des scripts à analyser (recherche dans le sous-dossier 'scripts')")
    parser.add_argument("--token-model", "-t", type=str, default="gpt-4o-mini",
                        help="Modèle de tokenisation (par défaut: gpt-4o-mini)")
    parser.add_argument("--pred-model", "-p", type=str, default="gpt-4o-mini",
                        help="Modèle de prédiction (par défaut: gpt-4o-mini)")
    parser.add_argument("--output-dir", "-o", type=str, default=None,
                        help="Répertoire de sortie pour les résultats")
    parser.add_argument("--tokens-dir", type=str, default=None,
                        help="Dossier contenant des fichiers *_tokens.json à transformer en matrices (mode reconstruction)")
    
    args = parser.parse_args()
    
    # Vérifier qu'au moins une source est spécifiée (fichier, dossier ou tokens-dir)
    if args.file is None and args.directory is None and args.tokens_dir is None:
        parser.error("Vous devez spécifier soit un fichier (--file), un dossier (--directory), soit un dossier de tokens (--tokens-dir) à analyser.")
    
    # Vérifier qu'on ne spécifie pas plusieurs modes
    n_modes = sum([args.file is not None, args.directory is not None, args.tokens_dir is not None])
    if n_modes > 1:
        parser.error("Vous ne pouvez pas spécifier plusieurs modes en même temps. Choisissez un seul mode.")
    
    output_dir = Path(args.output_dir) if args.output_dir else None
    
    try:
        if args.tokens_dir:
            generer_matrices_depuis_tokens_dir(args.tokens_dir, output_dir=output_dir, modele_tokenisation=args.token_model)
            logger.info(f"Génération des matrices depuis tokens_dir terminée.")
        elif args.file:
            # Mode fichier unique
            script_path = Path(args.file)
            matrix_file, result_file = analyser_script(
                script_path=script_path,
                output_dir=output_dir,
                modele_tokenisation=args.token_model,
                modele_prediction=args.pred_model
            )
            logger.info(f"Analyse terminée avec succès!")
            logger.info(f"Matrice sauvegardée dans: {matrix_file}")
            logger.info(f"Résultats détaillés dans: {result_file}")
        else:
            # Mode dossier
            directory_path = Path(args.directory)
            result_files = traiter_dossier(
                directory_path=directory_path,
                output_dir=output_dir,
                modele_tokenisation=args.token_model,
                modele_prediction=args.pred_model
            )
            if result_files:
                logger.info(f"Analyse du dossier terminée avec succès!")
                logger.info(f"Nombre de fichiers traités: {len(result_files)}")
                logger.info(f"Les matrices sont disponibles dans: {directory_path}/matrixes/")
                logger.info(f"Les rapports sont disponibles dans: {directory_path}/matrixes/reports/")
            else:
                logger.warning("Aucun fichier n'a été traité avec succès.")
                
    except Exception as e:
        logger.error(f"Erreur lors de l'analyse: {e}")
        import traceback
        logger.error(traceback.format_exc())
        exit(1)