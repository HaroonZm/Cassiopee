#!/usr/bin/env python3
"""
Générateur de matrices utilisant l'API Batch d'OpenAI avec chat/completions
Ce script permet de générer des matrices de log-probabilités pour analyser
les prédictions de tokens sur du code source, en utilisant l'API Batch pour
réduire les coûts et augmenter les limites de débit.
"""
from openai import OpenAI
import time
from tqdm import tqdm
import datetime
import tiktoken
import numpy as np
import os
import json
import argparse
import uuid
import tempfile
import shutil
from pathlib import Path
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Initialisation du client OpenAI avec clé API depuis variable d'environnement
client = OpenAI(api_key="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")

def tokeniser_avec_tiktoken(texte, modele="gpt-4o-mini"):
    """
    Tokenise le texte en utilisant tiktoken, la bibliothèque officielle d'OpenAI pour la tokenisation.
    
    Args:
        texte (str): Le texte à tokeniser
        modele (str): Le modèle GPT dont on veut utiliser l'encodeur
        
    Returns:
        tuple: Une liste de tokens (IDs) et une liste des tokens sous forme de chaînes
    """
    try:
        # Obtenir l'encodeur correspondant au modèle
        encodeur = tiktoken.encoding_for_model(modele)
    except KeyError:
        # Si le modèle n'est pas disponible, utiliser l'encodeur cl100k_base
        logger.warning(f"Encodeur pour {modele} non trouvé, utilisation de cl100k_base à la place.")
        encodeur = tiktoken.get_encoding("cl100k_base")
    
    # Encoder le texte en tokens (IDs numériques)
    token_ids = encodeur.encode(texte)
    
    # Convertir les IDs en tokens (chaînes de caractères)
    tokens = [encodeur.decode_single_token_bytes(token_id).decode('utf-8', errors='replace') 
              for token_id in token_ids]
    
    return token_ids, tokens

def prepare_batch_file(tokens, token_ids, modele, amorce_tokens=3, file_prefix="batch_input"):
    """
    Prépare un fichier JSONL pour l'API Batch avec les requêtes chat/completions.
    
    Args:
        tokens (list): Liste des tokens du script
        token_ids (list): Liste des IDs des tokens
        modele (str): Modèle à utiliser pour la prédiction
        amorce_tokens (int): Nombre de tokens d'amorce à utiliser
        file_prefix (str): Préfixe pour le nom du fichier
    
    Returns:
        tuple: Chemin du fichier JSONL, amorce utilisée, contexte initial
    """
    # Créer un dossier temporaire pour éviter les problèmes d'encodage
    temp_dir = tempfile.mkdtemp(prefix="matrix_batch_")
    
    # Initialiser le contexte avec les tokens d'amorce
    contexte_initial = ""
    for i in range(min(amorce_tokens, len(tokens))):
        contexte_initial += tokens[i]
    
    # Créer un fichier JSONL avec un nom unique
    batch_file = os.path.join(temp_dir, f"{file_prefix}_{uuid.uuid4().hex}.jsonl")
    
    with open(batch_file, 'w', encoding='utf-8') as f:
        # Pour chaque token après l'amorce, créer une requête API
        for i in range(amorce_tokens, len(tokens)):
            # Le contexte pour cette prédiction
            contexte = contexte_initial + ''.join(tokens[amorce_tokens:i])
            
            # Identifiant unique pour cette requête
            custom_id = f"token_{i}"
            
            # Créer la requête au format de l'API Batch
            request = {
                "custom_id": custom_id,
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": {
                    "model": modele,
                    "messages": [
                        {"role": "system", "content": "You are a code predictor that generates only the next token without any additional text. Pay attention to spaces, tabs, line breaks, and special symbols in the code."},
                        {"role": "user", "content": f"Code context: {contexte}"}
                    ],
                    "max_tokens": 1,
                    "temperature": 0.0,
                    "logprobs": True,
                    "top_logprobs": 10
                }
            }
            
            # Écrire la requête au format JSONL
            f.write(json.dumps(request) + "\n")
    
    logger.info(f"Fichier batch créé: {batch_file}")
    logger.info(f"Nombre de requêtes: {len(tokens) - amorce_tokens}")
    
    return batch_file, amorce_tokens, contexte_initial, temp_dir

def upload_batch_file(batch_file):
    """
    Upload le fichier batch à l'API OpenAI.
    
    Args:
        batch_file (str): Chemin vers le fichier JSONL
    
    Returns:
        str: ID du fichier uploadé
    """
    with open(batch_file, 'rb') as f:
        response = client.files.create(
            file=f,
            purpose="batch"
        )
    
    logger.info(f"Fichier uploadé avec ID: {response.id}")
    return response.id

def create_batch(file_id):
    """
    Crée un batch job avec le fichier uploadé.
    
    Args:
        file_id (str): ID du fichier uploadé
    
    Returns:
        str: ID du batch créé
    """
    batch = client.batches.create(
        input_file_id=file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h"
    )
    
    logger.info(f"Batch créé avec ID: {batch.id}, statut: {batch.status}")
    return batch.id

def poll_batch_status(batch_id, poll_interval=10, max_attempts=1000, wait_unlimited=True, max_connection_retries=5):
    """
    Vérifie régulièrement le statut du batch jusqu'à ce qu'il soit terminé.
    
    Args:
        batch_id (str): ID du batch
        poll_interval (int): Intervalle entre les vérifications en secondes
        max_attempts (int): Nombre maximum de tentatives (ignoré si wait_unlimited=True)
        wait_unlimited (bool): Si True, attendre indéfiniment la fin du batch
        max_connection_retries (int): Nombre maximum de tentatives en cas d'erreur de connexion
    
    Returns:
        object: L'objet batch final
    """
    attempt = 0
    
    while True:
        # Gestion des erreurs de connexion avec tentatives multiples
        connection_retries = 0
        while connection_retries < max_connection_retries:
            try:
                batch = client.batches.retrieve(batch_id)
                break  # Sortir de la boucle si la requête a réussi
            except Exception as e:
                connection_retries += 1
                if "Connection" in str(e) or "Timeout" in str(e) or "timeout" in str(e).lower():
                    retry_wait = min(30, 2 ** connection_retries)  # Attente exponentielle, max 30 secondes
                    logger.warning(f"Erreur de connexion: {str(e)}. Nouvelle tentative dans {retry_wait} secondes ({connection_retries}/{max_connection_retries})...")
                    time.sleep(retry_wait)
                    if connection_retries < max_connection_retries:
                        continue
                
                # Si on a épuisé toutes les tentatives ou ce n'est pas une erreur de connexion
                if connection_retries >= max_connection_retries:
                    logger.error(f"Nombre maximum de tentatives atteint après erreurs de connexion répétées")
                
                # Propager l'erreur après les tentatives
                raise
        
        status = batch.status
        
        # Afficher le statut actuel et les compteurs
        completed = getattr(batch.request_counts, "completed", 0) if hasattr(batch, "request_counts") else 0
        total = getattr(batch.request_counts, "total", 0) if hasattr(batch, "request_counts") else 0
        failed = getattr(batch.request_counts, "failed", 0) if hasattr(batch, "request_counts") else 0
        
        logger.info(f"Batch {batch_id} - Statut: {status}, Complété: {completed}/{total}, Échoué: {failed}")
        
        if status == "completed":
            logger.info(f"Batch terminé avec succès!")
            return batch
        
        if status in ["failed", "expired", "cancelled"]:
            error_msg = f"Batch a échoué avec le statut: {status}"
            logger.error(error_msg)
            if hasattr(batch, 'error_file_id') and batch.error_file_id:
                try:
                    error_content = client.files.content(batch.error_file_id).text
                    logger.error(f"Détails de l'erreur: {error_content[:500]}...")
                except Exception as e:
                    logger.error(f"Impossible de récupérer le fichier d'erreur: {e}")
            raise RuntimeError(error_msg)
        
        # Vérifier si on a atteint le nombre maximum de tentatives
        attempt += 1
        if not wait_unlimited and attempt >= max_attempts:
            raise TimeoutError(f"Dépassement du nombre maximum de tentatives ({max_attempts})")
        
        # Calculer le temps d'attente écoulé
        elapsed_time = attempt * poll_interval
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
        
        logger.info(f"En attente depuis {time_str}... Prochaine vérification dans {poll_interval} secondes")
        time.sleep(poll_interval)

def retrieve_batch_results(batch, max_connection_retries=5):
    """
    Récupère les résultats du batch terminé.
    
    Args:
        batch: L'objet batch final
        max_connection_retries (int): Nombre maximum de tentatives en cas d'erreur de connexion
    
    Returns:
        dict: Dictionnaire des résultats par custom_id
    """
    if not batch.output_file_id:
        raise ValueError("Le batch n'a pas de fichier de sortie")
    
    # Télécharger le fichier de résultats avec gestion des erreurs de connexion
    connection_retries = 0
    while connection_retries < max_connection_retries:
        try:
            output_content = client.files.content(batch.output_file_id).text
            break  # Sortir de la boucle si la requête a réussi
        except Exception as e:
            connection_retries += 1
            if "Connection" in str(e) or "Timeout" in str(e) or "timeout" in str(e).lower():
                retry_wait = min(30, 2 ** connection_retries)  # Attente exponentielle
                logger.warning(f"Erreur de connexion lors de la récupération des résultats: {str(e)}. Nouvelle tentative dans {retry_wait} secondes ({connection_retries}/{max_connection_retries})...")
                time.sleep(retry_wait)
                if connection_retries < max_connection_retries:
                    continue
            
            # Si on a épuisé toutes les tentatives ou ce n'est pas une erreur de connexion
            logger.error(f"Échec de la récupération des résultats après {connection_retries} tentatives: {str(e)}")
            raise
    
    # Parser les résultats
    results = {}
    for line in output_content.strip().split("\n"):
        try:
            response = json.loads(line)
            custom_id = response.get("custom_id")
            
            if not custom_id:
                logger.warning(f"Réponse sans custom_id: {line[:100]}...")
                continue
            
            if response.get("error"):
                logger.warning(f"Erreur pour {custom_id}: {response['error']}")
                continue
            
            # Extraire les informations pertinentes
            if response.get("response") and response["response"].get("body"):
                body = response["response"]["body"]
                content = body["choices"][0]["message"]["content"]
                
                # Extraire les alternatives avec logprobs
                alternatives = []
                
                # Vérification sécurisée de la présence des logprobs
                try:
                    if "logprobs" in body["choices"][0]:
                        logprobs = body["choices"][0]["logprobs"]
                        if logprobs and "content" in logprobs and len(logprobs["content"]) > 0:
                            top_logprobs = logprobs["content"][0].get("top_logprobs", [])
                            for item in top_logprobs:
                                alternatives.append({
                                    "token": item.get("token", ""),
                                    "logprob": item.get("logprob", -100.0)
                                })
                        else:
                            logger.debug(f"Structure de logprobs incomplète pour {custom_id}")
                    else:
                        logger.debug(f"Pas de logprobs dans la réponse pour {custom_id}")
                except Exception as e:
                    logger.warning(f"Erreur lors de l'extraction des logprobs pour {custom_id}: {str(e)}")
                
                # Stocker le résultat
                results[custom_id] = {
                    "content": content,
                    "alternatives": alternatives
                }
            else:
                logger.warning(f"Structure de réponse inattendue pour {custom_id}")
        except Exception as e:
            logger.error(f"Erreur lors du parsing d'une ligne: {str(e)}")
            logger.debug(f"Contenu de la ligne: {line[:200]}...")
    
    logger.info(f"Récupération terminée: {len(results)} résultats")
    return results

def process_batch_results(results, tokens, token_ids, amorce_tokens):
    """
    Traite les résultats du batch pour créer les résultats d'analyse.
    
    Args:
        results (dict): Résultats du batch
        tokens (list): Liste des tokens
        token_ids (list): Liste des IDs des tokens
        amorce_tokens (int): Nombre de tokens d'amorce
    
    Returns:
        list: Résultats d'analyse
    """
    # Initialiser les résultats d'analyse
    resultats_analyse = []
    
    # Ajouter les tokens d'amorce
    for i in range(amorce_tokens):
        resultats_analyse.append({
            "position": i,
            "token_id": token_ids[i],
            "attendu": tokens[i],
            "amorce": True,
            "alternatives": []
        })
    
    # Traiter les résultats du batch
    for i in range(amorce_tokens, len(tokens)):
        token_attendu = tokens[i]
        token_id_attendu = token_ids[i]
        custom_id = f"token_{i}"
        
        # Vérifier si le token précédent est une tabulation
        token_precedent_est_tabulation = False
        if i > 0:
            token_precedent = tokens[i-1]
            if "/n" not in token_precedent:
                token_precedent_est_tabulation = token_precedent.strip() == "" and len(token_precedent) > 1
        
        if custom_id in results:
            result = results[custom_id]
            token_predit = result["content"]
            alternatives = result["alternatives"]
            
            # Initialiser les flags pour la correction
            correct = token_predit == token_attendu
            correct_adapte = correct
            
            # Appliquer la règle spéciale pour les tokens après tabulation
            if token_precedent_est_tabulation and token_attendu.startswith(" ") and token_attendu.strip():
                token_sans_espace = token_attendu.lstrip(" ")
                correct_adapte = correct or token_predit == token_sans_espace
                
                # Ajouter une version adaptée aux alternatives
                for alt in alternatives:
                    if alt["token"] == token_sans_espace:
                        alt["token_adapte"] = token_attendu
                        alt["adapte"] = True
            
            # Vérifier si le token attendu est dans les alternatives
            token_dans_top10 = correct or correct_adapte or any(alt["token"] == token_attendu for alt in alternatives) or any(alt.get("adapte", False) for alt in alternatives)
            
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
        else:
            # Si pas de résultat pour ce token
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
    
    return resultats_analyse

def construire_matrice_logprob(tokens_reference, resultats_analyse, top_k=10):
    """
    Construit une matrice de log probabilités avec la taille dynamique,
    en padding avec 100 et anomalies à -50.
    """
    # 1) Reconstituer le texte complet et découper en lignes
    texte_complet = ''.join(tokens_reference)
    lignes_texte  = texte_complet.split('\n')

    # 2) Parcourir les tokens pour déterminer tokens_par_ligne et positions
    tokens_par_ligne = []
    position_tokens_dans_matrice = []
    ligne_courante = 0
    position_dans_ligne = 0

    for idx, token in enumerate(tokens_reference):
        # Enregistrer la position
        position_tokens_dans_matrice.append((ligne_courante, position_dans_ligne))
        position_dans_ligne += 1

        # Si le token contient un saut de ligne, on change de ligne
        if '\n' in token:
            tokens_par_ligne.append(position_dans_ligne)
            ligne_courante += 1
            position_dans_ligne = 0
            if ligne_courante >= len(lignes_texte):
                break

    # Ajouter la dernière ligne si nécessaire
    if position_dans_ligne > 0:
        tokens_par_ligne.append(position_dans_ligne)

    # 3) Calculer les dimensions dynamiques
    n_lignes_dyn   = len(lignes_texte)
    max_tokens_dyn = max(tokens_par_ligne) if tokens_par_ligne else 0

    # 4) Utiliser les dimensions dynamiques directement (sans forcer à 244x244)
    n_lignes, max_tokens = n_lignes_dyn, max_tokens_dyn
    logger.info(f"Construction d'une matrice avec dimensions dynamiques : {n_lignes} lignes × {max_tokens} colonnes (padding=100)")

    # 5) Initialiser la matrice de padding avec les dimensions dynamiques
    matrice = np.full((n_lignes, max_tokens), 100.0)

    # 6) Remplir la matrice avec log-probabilités ou valeurs spéciales
    for idx_token, (i, j) in enumerate(position_tokens_dans_matrice):
        # Ignorer toute position hors de la matrice
        if i >= n_lignes or j >= max_tokens:
            continue

        # Chercher le résultat d'analyse correspondant
        resultat = next((r for r in resultats_analyse if r["position"] == idx_token), None)
        if not resultat:
            matrice[i, j] = -50.0
            continue

        # Tokens d'amorce
        if resultat.get("amorce", False):
            matrice[i, j] = -10.0
            continue

        # Sinon calculer la log-proba
        attendu  = resultat["attendu"]
        predit   = resultat.get("predit")
        alternatives = resultat.get("alternatives", [])

        # Valeur par défaut pour anomalie
        val_logprob = -50.0

        # Si correct (stricte ou adaptée), prendre la logprob de la prédiction
        if resultat.get("correct", False) or resultat.get("correct_adapte", False):
            for alt in alternatives:
                if alt["token"] == predit:
                    val_logprob = alt["logprob"]
                    break
        else:
            # Sinon chercher le token attendu (ou adapté) dans les alternatives
            for alt in alternatives:
                if alt["token"] == attendu or alt.get("token_adapte") == attendu:
                    val_logprob = alt["logprob"]
                    break

        matrice[i, j] = val_logprob

    # 7) Retourner la matrice et la structure complète
    structure_tokens = {
        "lignes": n_lignes,
        "max_tokens": max_tokens,
        "tokens_par_ligne": tokens_par_ligne,
        "position_tokens": position_tokens_dans_matrice
    }
    return matrice, structure_tokens

def afficher_matrice_brute(matrice, structure_tokens):
    """
    Affiche la matrice 2D de log probabilités brute dans la console
    
    Args:
        matrice (numpy.ndarray): La matrice 2D de log probabilités
        structure_tokens (dict): Informations sur la structure de la matrice
    """
    logger.info("\nMATRICE BRUTE DE LOG PROBABILITÉS:")
    logger.info(f"Dimensions: {matrice.shape[0]} lignes x {matrice.shape[1]} colonnes")
    
    # Calculer la largeur maximale pour l'affichage
    max_width = 10  # Largeur par défaut pour chaque valeur
    
    # Créer une ligne de séparation
    header_sep = "-" * (max_width * matrice.shape[1] + 10)
    logger.info(header_sep)
    
    # Afficher les indices de colonnes
    logger.info("     ", end="")
    for j in range(matrice.shape[1]):
        logger.info(f"{j:^{max_width}}", end="")
    logger.info()  # Nouvelle ligne
    
    # Ligne de séparation après les indices de colonnes
    logger.info("     " + "-" * (max_width * matrice.shape[1]))
    
    # Afficher chaque ligne avec son indice
    for i in range(matrice.shape[0]):
        logger.info(f"{i:3d} |", end="")
        for j in range(matrice.shape[1]):
            val = matrice[i, j]
            if val == 100:
                # Padding
                logger.info(f"{'PAD':^{max_width}}", end="")
            elif val == -50:
                # Anomalie
                logger.info(f"{'ANOM':^{max_width}}", end="")
            else:
                # Log probabilité normale
                logger.info(f"{val:^{max_width}.4f}", end="")
        logger.info()  # Nouvelle ligne
    
    # Ligne de séparation finale
    logger.info(header_sep)

def sauvegarder_resultats(resultats_analyse, script, matrice, structure_tokens, modele_tokenisation="gpt-4o-mini", nom_fichier=None):
    """
    Sauvegarde les résultats détaillés de l'analyse dans un fichier texte.
    
    Args:
        resultats_analyse (list): Résultats de l'analyse token par token
        script (str): Le script analysé
        matrice (numpy.ndarray): La matrice 2D de log probabilités
        structure_tokens (dict): Informations sur la structure de la matrice
        modele_tokenisation (str): Le modèle utilisé pour la tokenisation
        nom_fichier (str): Nom du fichier pour sauvegarder les résultats
    """
    if nom_fichier is None:
        nom_fichier = f"resultats_batch_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write(f"ANALYSE DE PRÉDICTION TOKEN PAR TOKEN (BATCH API)\n")
        f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Modèle de tokenisation: {modele_tokenisation}\n")
        f.write("="*80 + "\n\n")
        
        f.write("SCRIPT ANALYSÉ:\n")
        f.write("-"*80 + "\n")
        f.write(script)
        f.write("\n" + "-"*80 + "\n\n")
        
        f.write("RÉSULTATS D'ANALYSE TOKEN PAR TOKEN:\n")
        f.write("-"*80 + "\n")
        
        # Calculer des statistiques
        total_tokens = len([r for r in resultats_analyse if not r.get("amorce", False)])
        correct_tokens = len([r for r in resultats_analyse if r.get("correct", False) and not r.get("amorce", False)])
        correct_adapte_tokens = len([r for r in resultats_analyse if r.get("correct_adapte", False) and not r.get("amorce", False)])
        correct_top10_tokens = len([r for r in resultats_analyse if r.get("correct_top10", False) and not r.get("amorce", False)])
        
        # Écrire les résultats pour chaque token
        for result in resultats_analyse:
            position = result["position"]
            token = result["attendu"]
            token_id = result["token_id"]
            
            f.write(f"Token {position}: '{token}' (ID: {token_id})\n")
            
            if result.get("amorce", False):
                f.write("  → Token d'amorce (pas de prédiction)\n\n")
                continue
            
            predit = result.get("predit", "ERROR")
            correct = result.get("correct", False)
            correct_adapte = result.get("correct_adapte", False)
            correct_top10 = result.get("correct_top10", False)
            
            f.write(f"  Prédit: '{predit}'\n")
            f.write(f"  Correct (stricte): {correct}\n")
            f.write(f"  Correct (adapté): {correct_adapte}\n")
            f.write(f"  Dans le top 10: {correct_top10}\n")
            
            # Afficher les alternatives avec leurs log-probs
            alternatives = result.get("alternatives", [])
            if alternatives:
                f.write("  Alternatives (top logprobs):\n")
                for i, alt in enumerate(alternatives):
                    token_alt = alt["token"]
                    logprob = alt["logprob"]
                    adapte = alt.get("adapte", False)
                    if adapte:
                        f.write(f"    {i+1}. '{token_alt}' (adapté à '{alt['token_adapte']}') → logprob: {logprob}\n")
                    else:
                        f.write(f"    {i+1}. '{token_alt}' → logprob: {logprob}\n")
            
            f.write("\n")
        
        # Écrire les statistiques globales
        f.write("\nRÉSUMÉ:\n")
        f.write("-"*80 + "\n")
        f.write(f"Total des tokens analysés: {total_tokens}\n")
        f.write(f"Tokens correctement prédits (1ère position, stricte): {correct_tokens}\n")
        f.write(f"Tokens correctement prédits (1ère position, avec adaptation): {correct_adapte_tokens}\n")
        f.write(f"Tokens correctement prédits (top 10): {correct_top10_tokens}\n")
        
        if total_tokens > 0:
            precision = (correct_tokens / total_tokens) * 100
            precision_adaptee = (correct_adapte_tokens / total_tokens) * 100
            precision_top10 = (correct_top10_tokens / total_tokens) * 100
            f.write(f"Précision stricte (1ère position): {precision:.2f}%\n")
            f.write(f"Précision adaptée (1ère position): {precision_adaptee:.2f}%\n")
            f.write(f"Précision (top 10): {precision_top10:.2f}%\n")
        
        f.write("="*80 + "\n")
    
    logger.info(f"Résultats sauvegardés dans le fichier: {nom_fichier}")
    return nom_fichier

def sauvegarder_matrice_numpy(matrice, nom_fichier="matrice_logprob.npy"):
    """
    Sauvegarde la matrice au format numpy pour une utilisation ultérieure.
    
    Args:
        matrice (numpy.ndarray): La matrice 2D de log probabilités
        nom_fichier (str): Nom du fichier pour sauvegarder la matrice
    """
    np.save(nom_fichier, matrice)
    logger.info(f"Matrice sauvegardée au format numpy dans {nom_fichier}")

def analyze_with_batch_api(script, modele_tokenisation="gpt-4o-mini", modele_prediction="gpt-4o-mini", 
                      poll_interval=10, max_attempts=1000, wait_unlimited=True, max_connection_retries=5):
    """
    Analyse un script en utilisant l'API Batch d'OpenAI.
    
    Args:
        script (str): Le script à analyser
        modele_tokenisation (str): Modèle à utiliser pour la tokenisation
        modele_prediction (str): Modèle à utiliser pour la prédiction
        poll_interval (int): Intervalle entre les vérifications de statut en secondes
        max_attempts (int): Nombre maximum de tentatives (ignoré si wait_unlimited=True)
        wait_unlimited (bool): Si True, attendre indéfiniment la fin du batch
        max_connection_retries (int): Nombre maximum de tentatives en cas d'erreur de connexion
    
    Returns:
        tuple: Résultats d'analyse, tokens, matrice, structure
    """
    # 1. Tokenisation du script
    logger.info(f"Tokenisation du script avec tiktoken ({modele_tokenisation})...")
    token_ids, tokens = tokeniser_avec_tiktoken(script, modele_tokenisation)
    logger.info(f"Script tokenisé en {len(tokens)} tokens")
    
    # 2. Préparation du fichier batch
    amorce_tokens = max(1, min(3, len(tokens) // 3))
    logger.info(f"Utilisation de {amorce_tokens} tokens comme amorce")
    
    batch_file, amorce_tokens, contexte_initial, temp_dir = prepare_batch_file(
        tokens, token_ids, modele_prediction, amorce_tokens
    )
    
    try:
        # 3. Upload du fichier batch avec gestion des erreurs de connexion
        connection_retries = 0
        while connection_retries < max_connection_retries:
            try:
                file_id = upload_batch_file(batch_file)
                break  # Sortir de la boucle si l'upload a réussi
            except Exception as e:
                connection_retries += 1
                if "Connection" in str(e) or "Timeout" in str(e) or "timeout" in str(e).lower():
                    retry_wait = min(30, 2 ** connection_retries)
                    logger.warning(f"Erreur de connexion lors de l'upload: {str(e)}. Nouvelle tentative dans {retry_wait} secondes ({connection_retries}/{max_connection_retries})...")
                    time.sleep(retry_wait)
                    if connection_retries < max_connection_retries:
                        continue
                
                # Si on a épuisé toutes les tentatives ou ce n'est pas une erreur de connexion
                logger.error(f"Échec de l'upload après {connection_retries} tentatives")
                raise
        
        # 4. Création du batch avec gestion des erreurs de connexion
        connection_retries = 0
        while connection_retries < max_connection_retries:
            try:
                batch_id = create_batch(file_id)
                break  # Sortir de la boucle si la création a réussi
            except Exception as e:
                connection_retries += 1
                if "Connection" in str(e) or "Timeout" in str(e) or "timeout" in str(e).lower():
                    retry_wait = min(30, 2 ** connection_retries)
                    logger.warning(f"Erreur de connexion lors de la création du batch: {str(e)}. Nouvelle tentative dans {retry_wait} secondes ({connection_retries}/{max_connection_retries})...")
                    time.sleep(retry_wait)
                    if connection_retries < max_connection_retries:
                        continue
                
                # Si on a épuisé toutes les tentatives ou ce n'est pas une erreur de connexion
                logger.error(f"Échec de la création du batch après {connection_retries} tentatives")
                raise
        
        # 5. Vérification périodique du statut avec gestion améliorée des erreurs de connexion
        batch = poll_batch_status(
            batch_id, 
            poll_interval, 
            max_attempts, 
            wait_unlimited,
            max_connection_retries
        )
        
        # 6. Récupération des résultats avec gestion améliorée des erreurs de connexion
        results = retrieve_batch_results(batch, max_connection_retries)
        
        # 7. Traitement des résultats
        resultats_analyse = process_batch_results(results, tokens, token_ids, amorce_tokens)
        
        # 8. Construction de la matrice
        matrice, structure = construire_matrice_logprob(tokens, resultats_analyse)
        
        return resultats_analyse, tokens, matrice, structure
    
    finally:
        # Nettoyage du dossier temporaire
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            logger.info(f"Dossier temporaire nettoyé: {temp_dir}")

def process_directory_async(directory_path, output_dir, model_prediction="gpt-4o-mini", model_tokenisation="gpt-4o-mini",
                   poll_interval=10, max_attempts=1000, wait_unlimited=True, recursive=True, max_connection_retries=5):
    """
    Traite tous les fichiers Python dans un dossier de manière asynchrone.
    Soumet tous les batchs en parallèle puis récupère les résultats lorsqu'ils sont disponibles.
    
    Args:
        directory_path (str): Chemin du dossier à analyser
        output_dir (str): Dossier où sauvegarder les résultats
        model_prediction (str): Modèle à utiliser pour la prédiction
        model_tokenisation (str): Modèle à utiliser pour la tokenisation
        poll_interval (int): Intervalle entre les vérifications de statut en secondes
        max_attempts (int): Nombre maximum de tentatives
        wait_unlimited (bool): Si True, attendre indéfiniment la fin du batch
        recursive (bool): Si True, analyser également les sous-dossiers
        max_connection_retries (int): Nombre maximum de tentatives en cas d'erreur de connexion
    
    Returns:
        int: Nombre de fichiers traités
    """
    directory_path = Path(directory_path)
    output_dir = Path(output_dir)
    
    if not directory_path.exists() or not directory_path.is_dir():
        raise ValueError(f"Le dossier {directory_path} n'existe pas ou n'est pas un dossier")
    
    # Créer les sous-dossiers dans le dossier de sortie
    matrix_dir = output_dir / "matrices"
    results_dir = output_dir / "rapports"
    
    matrix_dir.mkdir(exist_ok=True, parents=True)
    results_dir.mkdir(exist_ok=True, parents=True)
    
    logger.info(f"Traitement asynchrone du dossier: {directory_path}")
    logger.info(f"Dossier de sortie: {output_dir}")
    
    # Trouver tous les fichiers Python
    pattern = "**/*.py" if recursive else "*.py"
    python_files = list(directory_path.glob(pattern))
    
    if not python_files:
        logger.warning(f"Aucun fichier Python trouvé dans {directory_path}")
        return 0
    
    logger.info(f"Nombre de fichiers Python trouvés: {len(python_files)}")
    
    # Structure pour stocker les informations sur les batchs en cours
    pending_batches = []
    files_processed = 0
    
    # Phase 1: Soumettre tous les batchs
    logger.info("Phase 1: Soumission de tous les batchs...")
    
    for py_file in python_files:
        try:
            # Obtenir le chemin relatif pour organiser la sortie
            rel_path = py_file.relative_to(directory_path)
            
            # Conserver le nom complet du fichier (sans l'extension .py)
            file_name = py_file.name
            file_name_no_ext = file_name[:-3] if file_name.lower().endswith('.py') else file_name
            
            # Créer des sous-dossiers dans le dossier de sortie si nécessaire
            if py_file.parent != directory_path:
                parent_dir = matrix_dir / rel_path.parent
                parent_dir.mkdir(exist_ok=True, parents=True)
                
                parent_results_dir = results_dir / rel_path.parent
                parent_results_dir.mkdir(exist_ok=True, parents=True)
                
                matrix_output = parent_dir / f"mat_{file_name_no_ext}.npy"
                result_output = parent_results_dir / f"result_{file_name_no_ext}.txt"
            else:
                matrix_output = matrix_dir / f"mat_{file_name_no_ext}.npy"
                result_output = results_dir / f"result_{file_name_no_ext}.txt"
            
            # Vérifier si le fichier existe déjà (reprise après erreur)
            if matrix_output.exists() and result_output.exists():
                logger.info(f"Le fichier {py_file} a déjà été traité (matrices et rapports existants). Passage au suivant.")
                files_processed += 1
                continue
            
            logger.info(f"Préparation du batch pour {file_name}...")
            
            # Lire le contenu du fichier Python
            try:
                script = py_file.read_text(encoding='utf-8')
                
                # Tokenisation du script
                token_ids, tokens = tokeniser_avec_tiktoken(script, model_tokenisation)
                
                # Préparation du fichier batch
                amorce_tokens = max(1, min(3, len(tokens) // 3))
                batch_file, amorce_tokens, contexte_initial, temp_dir = prepare_batch_file(
                    tokens, token_ids, model_prediction, amorce_tokens
                )
                
                # Upload du fichier batch
                connection_retries = 0
                file_id = None
                while connection_retries < max_connection_retries:
                    try:
                        file_id = upload_batch_file(batch_file)
                        break
                    except Exception as e:
                        connection_retries += 1
                        if "Connection" in str(e) or "Timeout" in str(e) or "timeout" in str(e).lower():
                            retry_wait = min(30, 2 ** connection_retries)
                            logger.warning(f"Erreur de connexion lors de l'upload: {str(e)}. Nouvelle tentative dans {retry_wait} secondes...")
                            time.sleep(retry_wait)
                            if connection_retries < max_connection_retries:
                                continue
                        logger.error(f"Échec de l'upload après {connection_retries} tentatives")
                        raise
                
                if not file_id:
                    continue
                
                # Création du batch
                connection_retries = 0
                batch_id = None
                while connection_retries < max_connection_retries:
                    try:
                        batch_id = create_batch(file_id)
                        break
                    except Exception as e:
                        connection_retries += 1
                        if "Connection" in str(e) or "Timeout" in str(e) or "timeout" in str(e).lower():
                            retry_wait = min(30, 2 ** connection_retries)
                            logger.warning(f"Erreur de connexion lors de la création du batch: {str(e)}. Nouvelle tentative...")
                            time.sleep(retry_wait)
                            if connection_retries < max_connection_retries:
                                continue
                        logger.error(f"Échec de la création du batch après {connection_retries} tentatives")
                        raise
                
                if not batch_id:
                    continue
                
                # Stocker les informations sur ce batch
                pending_batches.append({
                    "batch_id": batch_id,
                    "file_id": file_id,
                    "py_file": py_file,
                    "file_name": file_name,
                    "matrix_output": matrix_output,
                    "result_output": result_output,
                    "script": script,
                    "tokens": tokens,
                    "token_ids": token_ids,
                    "amorce_tokens": amorce_tokens,
                    "temp_dir": temp_dir,
                    "status": "pending"
                })
                
                logger.info(f"Batch {batch_id} soumis pour {file_name}")
                
            except Exception as e:
                logger.error(f"Erreur lors de la préparation du batch pour {py_file}: {str(e)}")
                # Créer un fichier d'erreur pour traçabilité
                error_file = results_dir / f"error_{file_name_no_ext}.txt"
                try:
                    with open(error_file, 'w', encoding='utf-8') as f:
                        f.write(f"Erreur lors de la préparation du batch pour {py_file}:\n{str(e)}")
                except Exception as write_err:
                    logger.error(f"Impossible d'écrire le fichier d'erreur: {str(write_err)}")
        
        except Exception as e:
            logger.error(f"Erreur lors du traitement initial de {py_file}: {str(e)}")
    
    logger.info(f"Tous les batchs ont été soumis. {len(pending_batches)} batchs en attente.")
    
    # Phase 2: Vérifier régulièrement l'état des batchs et traiter les résultats
    logger.info("Phase 2: Vérification périodique de l'état des batchs...")
    
    completed_count = 0
    failed_count = 0
    
    while pending_batches:
        # Liste des batchs à retirer de la liste des batchs en attente
        batches_to_remove = []
        
        for i, batch_info in enumerate(pending_batches):
            batch_id = batch_info["batch_id"]
            file_name = batch_info["file_name"]
            
            try:
                # Vérifier le statut du batch
                connection_retries = 0
                batch = None
                while connection_retries < max_connection_retries:
                    try:
                        batch = client.batches.retrieve(batch_id)
                        break
                    except Exception as e:
                        connection_retries += 1
                        if "Connection" in str(e) or "Timeout" in str(e) or "timeout" in str(e).lower():
                            retry_wait = min(30, 2 ** connection_retries)
                            logger.warning(f"Erreur de connexion lors de la vérification du batch {batch_id}: {str(e)}. Nouvelle tentative...")
                            time.sleep(retry_wait)
                            if connection_retries < max_connection_retries:
                                continue
                        logger.error(f"Échec de la vérification du batch après {connection_retries} tentatives")
                        raise
                
                if not batch:
                    continue
                
                status = batch.status
                completed = getattr(batch.request_counts, "completed", 0) if hasattr(batch, "request_counts") else 0
                total = getattr(batch.request_counts, "total", 0) if hasattr(batch, "request_counts") else 0
                failed = getattr(batch.request_counts, "failed", 0) if hasattr(batch, "request_counts") else 0
                
                logger.info(f"Batch {batch_id} ({file_name}) - Statut: {status}, Complété: {completed}/{total}, Échoué: {failed}")
                
                if status == "completed":
                    logger.info(f"Batch {batch_id} ({file_name}) terminé avec succès!")
                    
                    # Récupérer les résultats
                    try:
                        results = retrieve_batch_results(batch, max_connection_retries)
                        
                        # Traiter les résultats
                        resultats_analyse = process_batch_results(
                            results, 
                            batch_info["tokens"], 
                            batch_info["token_ids"], 
                            batch_info["amorce_tokens"]
                        )
                        
                        # Construction de la matrice
                        matrice, structure = construire_matrice_logprob(batch_info["tokens"], resultats_analyse)
                        
                        # Sauvegarder les résultats
                        sauvegarder_matrice_numpy(matrice, nom_fichier=str(batch_info["matrix_output"]))
                        sauvegarder_resultats(
                            resultats_analyse,
                            batch_info["script"],
                            matrice,
                            structure,
                            nom_fichier=str(batch_info["result_output"])
                        )
                        
                        logger.info(f"→ Matrice enregistrée : {batch_info['matrix_output']}")
                        logger.info(f"→ Rapport enregistré  : {batch_info['result_output']}")
                        
                        completed_count += 1
                        files_processed += 1
                        
                    except Exception as e:
                        logger.error(f"Erreur lors du traitement des résultats du batch {batch_id} ({file_name}): {str(e)}")
                        failed_count += 1
                    
                    # Marquer ce batch pour suppression de la liste d'attente
                    batches_to_remove.append(i)
                    
                    # Nettoyer le dossier temporaire
                    if os.path.exists(batch_info["temp_dir"]):
                        shutil.rmtree(batch_info["temp_dir"])
                
                elif status in ["failed", "expired", "cancelled"]:
                    logger.error(f"Batch {batch_id} ({file_name}) a échoué avec le statut: {status}")
                    if hasattr(batch, 'error_file_id') and batch.error_file_id:
                        try:
                            error_content = client.files.content(batch.error_file_id).text
                            logger.error(f"Détails de l'erreur: {error_content[:500]}...")
                        except Exception as e:
                            logger.error(f"Impossible de récupérer le fichier d'erreur: {e}")
                    
                    failed_count += 1
                    batches_to_remove.append(i)
                    
                    # Nettoyer le dossier temporaire
                    if os.path.exists(batch_info["temp_dir"]):
                        shutil.rmtree(batch_info["temp_dir"])
                
            except Exception as e:
                logger.error(f"Erreur lors de la gestion du batch {batch_id} ({file_name}): {str(e)}")
        
        # Supprimer les batchs terminés ou échoués de la liste d'attente (en commençant par la fin)
        for i in sorted(batches_to_remove, reverse=True):
            del pending_batches[i]
        
        # Afficher l'état d'avancement
        if pending_batches:
            logger.info(f"Progression: {completed_count} terminés, {failed_count} échoués, {len(pending_batches)} en attente")
            logger.info(f"Prochaine vérification dans {poll_interval} secondes...")
            time.sleep(poll_interval)
        else:
            logger.info("Tous les batchs ont été traités!")
    
    logger.info(f"\nTraitement asynchrone du dossier terminé. {files_processed}/{len(python_files)} fichiers traités.")
    logger.info(f"Réussis: {completed_count}, Échoués: {failed_count}")
    
    return files_processed

def process_directory(directory_path, output_dir, model_prediction="gpt-4o-mini", model_tokenisation="gpt-4o-mini",
                   poll_interval=10, max_attempts=1000, wait_unlimited=True, recursive=True, max_connection_retries=5,
                   async_mode=False):
    """
    Traite tous les fichiers Python dans un dossier (et ses sous-dossiers si recursive=True).
    
    Args:
        directory_path (str): Chemin du dossier à analyser
        output_dir (str): Dossier où sauvegarder les résultats
        model_prediction (str): Modèle à utiliser pour la prédiction
        model_tokenisation (str): Modèle à utiliser pour la tokenisation
        poll_interval (int): Intervalle entre les vérifications de statut en secondes
        max_attempts (int): Nombre maximum de tentatives
        wait_unlimited (bool): Si True, attendre indéfiniment la fin du batch
        recursive (bool): Si True, analyser également les sous-dossiers
        max_connection_retries (int): Nombre maximum de tentatives en cas d'erreur de connexion
        async_mode (bool): Si True, utiliser le mode asynchrone pour traiter les fichiers en parallèle
    
    Returns:
        int: Nombre de fichiers traités
    """
    # Utiliser le mode asynchrone si demandé
    if async_mode:
        return process_directory_async(
            directory_path,
            output_dir,
            model_prediction,
            model_tokenisation,
            poll_interval,
            max_attempts,
            wait_unlimited,
            recursive,
            max_connection_retries
        )
    
    # Sinon, continuer avec le traitement synchrone original
    directory_path = Path(directory_path)
    output_dir = Path(output_dir)
    
    if not directory_path.exists() or not directory_path.is_dir():
        raise ValueError(f"Le dossier {directory_path} n'existe pas ou n'est pas un dossier")
    
    # Créer les sous-dossiers dans le dossier de sortie
    matrix_dir = output_dir / "matrices"
    results_dir = output_dir / "rapports"
    
    matrix_dir.mkdir(exist_ok=True, parents=True)
    results_dir.mkdir(exist_ok=True, parents=True)
    
    logger.info(f"Traitement du dossier: {directory_path}")
    logger.info(f"Dossier de sortie: {output_dir}")
    
    # Trouver tous les fichiers Python
    pattern = "**/*.py" if recursive else "*.py"
    python_files = list(directory_path.glob(pattern))
    
    if not python_files:
        logger.warning(f"Aucun fichier Python trouvé dans {directory_path}")
        return 0
    
    logger.info(f"Nombre de fichiers Python trouvés: {len(python_files)}")
    
    # Traiter chaque fichier
    files_processed = 0
    
    for py_file in python_files:
        try:
            # Obtenir le chemin relatif pour organiser la sortie
            rel_path = py_file.relative_to(directory_path)
            
            # Conserver le nom complet du fichier (sans l'extension .py) au lieu de juste le stem
            file_name = py_file.name
            file_name_no_ext = file_name[:-3] if file_name.lower().endswith('.py') else file_name
            
            # Créer des sous-dossiers dans le dossier de sortie si nécessaire
            if py_file.parent != directory_path:
                parent_dir = matrix_dir / rel_path.parent
                parent_dir.mkdir(exist_ok=True, parents=True)
                
                parent_results_dir = results_dir / rel_path.parent
                parent_results_dir.mkdir(exist_ok=True, parents=True)
                
                # Utiliser "mat_" comme préfixe et le nom complet du fichier
                matrix_output = parent_dir / f"mat_{file_name_no_ext}.npy"
                result_output = parent_results_dir / f"result_{file_name_no_ext}.txt"
            else:
                # Utiliser "mat_" comme préfixe et le nom complet du fichier
                matrix_output = matrix_dir / f"mat_{file_name_no_ext}.npy"
                result_output = results_dir / f"result_{file_name_no_ext}.txt"
            
            # Vérifier si le fichier existe déjà (reprise après erreur)
            if matrix_output.exists() and result_output.exists():
                logger.info(f"Le fichier {py_file} a déjà été traité (matrices et rapports existants). Passage au suivant.")
                files_processed += 1
                continue
            
            logger.info(f"\n--- Analyse de {file_name} avec l'API Batch et le modèle {model_prediction} ---")
            
            # Lire le contenu du fichier Python
            script = py_file.read_text(encoding='utf-8')
            
            # Analyser le fichier
            try:
                resultats_analyse, tokens, matrice, structure = analyze_with_batch_api(
                    script,
                    modele_tokenisation=model_tokenisation,
                    modele_prediction=model_prediction,
                    poll_interval=poll_interval,
                    max_attempts=max_attempts,
                    wait_unlimited=wait_unlimited,
                    max_connection_retries=max_connection_retries
                )
                
                # Sauvegarder les résultats
                sauvegarder_matrice_numpy(matrice, nom_fichier=str(matrix_output))
                sauvegarder_resultats(
                    resultats_analyse,
                    script,
                    matrice,
                    structure,
                    nom_fichier=str(result_output)
                )
                
                logger.info(f"→ Matrice enregistrée : {matrix_output}")
                logger.info(f"→ Rapport enregistré  : {result_output}")
                
                files_processed += 1
                
            except Exception as e:
                logger.error(f"Erreur lors de l'analyse de {py_file}: {str(e)}")
                # Créer un fichier d'erreur pour traçabilité
                error_file = results_dir / f"error_{file_name_no_ext}.txt"
                try:
                    with open(error_file, 'w', encoding='utf-8') as f:
                        f.write(f"Erreur lors de l'analyse de {py_file}:\n{str(e)}")
                    logger.info(f"Détails de l'erreur enregistrés dans: {error_file}")
                except Exception as write_err:
                    logger.error(f"Impossible d'écrire le fichier d'erreur: {str(write_err)}")
        
        except Exception as e:
            logger.error(f"Erreur lors du traitement de {py_file}: {str(e)}")
    
    logger.info(f"\nTraitement du dossier terminé. {files_processed}/{len(python_files)} fichiers traités.")
    return files_processed

def main():
    parser = argparse.ArgumentParser(
        description="Analyse des prédictions token par token pour un script en utilisant l'API Batch d'OpenAI.")
    parser.add_argument(
        "-f", "--file",
        help="Nom du fichier à analyser (chemin relatif ou absolu). Ex: 'foo.py'",
        type=str,
        required=False,
    )
    parser.add_argument(
        "-d", "--directory",
        help="Dossier contenant des scripts Python à analyser",
        type=str,
        required=False,
    )
    parser.add_argument(
        "--recursive",
        help="Analyser également les sous-dossiers (avec --directory)",
        action="store_true",
    )
    parser.add_argument(
        "-o", "--output",
        help="Dossier où sauvegarder les résultats",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--model",
        help="Modèle à utiliser pour la prédiction",
        type=str,
        default="gpt-4o-mini",
    )
    parser.add_argument(
        "--poll-interval",
        help="Intervalle entre les vérifications de statut en secondes",
        type=int,
        default=10,
    )
    parser.add_argument(
        "--max-attempts",
        help="Nombre maximum de tentatives de vérification du statut",
        type=int,
        default=1000,
    )
    parser.add_argument(
        "--no-wait-unlimited",
        help="Arrêter après le nombre maximum de tentatives au lieu d'attendre indéfiniment",
        action="store_true",
    )
    parser.add_argument(
        "--batch-id",
        help="ID d'un batch existant à traiter (permet de reprendre une analyse interrompue)",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--max-connection-retries",
        help="Nombre maximum de tentatives en cas d'erreur de connexion",
        type=int,
        default=5,
    )
    parser.add_argument(
        "--continue-on-error",
        help="Continuer le traitement même en cas d'erreur sur un fichier",
        action="store_true",
    )
    parser.add_argument(
        "--async",
        help="Traiter les fichiers de manière asynchrone (avec --directory)",
        action="store_true",
    )
    args = parser.parse_args()
    
    # Vérifier qu'au moins un des arguments file, directory ou batch-id est fourni
    if not args.file and not args.directory and not args.batch_id:
        parser.error("Vous devez spécifier soit un fichier avec -f, soit un dossier avec -d, soit un batch existant avec --batch-id")
    
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
    
    logger.info(f"Dossier de sortie: {output_dir}")
    logger.info(f"Dossier des matrices: {matrix_dir}")
    logger.info(f"Dossier des rapports: {results_dir}")
    
    # Traitement d'un batch existant
    if args.batch_id:
        logger.info(f"\n--- Traitement du batch existant {args.batch_id} ---")
        
        try:
            # Récupérer le batch avec gestion des erreurs de connexion
            connection_retries = 0
            while connection_retries < args.max_connection_retries:
                try:
                    batch = client.batches.retrieve(args.batch_id)
                    break  # Sortir de la boucle si la requête a réussi
                except Exception as e:
                    connection_retries += 1
                    if "Connection" in str(e) or "Timeout" in str(e) or "timeout" in str(e).lower():
                        retry_wait = min(30, 2 ** connection_retries)
                        logger.warning(f"Erreur de connexion: {str(e)}. Nouvelle tentative dans {retry_wait} secondes ({connection_retries}/{args.max_connection_retries})...")
                        time.sleep(retry_wait)
                        if connection_retries < args.max_connection_retries:
                            continue
                    
                    # Si on a épuisé toutes les tentatives ou ce n'est pas une erreur de connexion
                    logger.error(f"Impossible de récupérer le batch {args.batch_id}: {str(e)}")
                    raise
            
            # Vérifier périodiquement le statut si le batch n'est pas terminé
            if batch.status != "completed":
                logger.info(f"Le batch a le statut '{batch.status}'. Attente de la fin du traitement...")
                batch = poll_batch_status(
                    args.batch_id,
                    poll_interval=args.poll_interval,
                    max_attempts=args.max_attempts,
                    wait_unlimited=not args.no_wait_unlimited,
                    max_connection_retries=args.max_connection_retries
                )
            
            # Demander le nom du fichier source pour créer les fichiers de sortie
            script_name = input("Entrez le nom du script source (sans extension) pour nommer les fichiers de sortie: ")
            if not script_name:
                script_name = f"batch_{args.batch_id[:8]}"
            
            # Récupérer les résultats
            logger.info("Récupération des résultats...")
            results = retrieve_batch_results(batch, args.max_connection_retries)
            
            # Demander la tokenisation du script source pour reconstruire la matrice
            script_content = None
            tokenize_source = input("Voulez-vous tokeniser un fichier source pour reconstruire la matrice complète? (y/n): ")
            if tokenize_source.lower() == 'y':
                source_path = input("Chemin vers le fichier source: ")
                if os.path.exists(source_path):
                    with open(source_path, 'r', encoding='utf-8') as f:
                        script_content = f.read()
                else:
                    logger.warning(f"Fichier non trouvé: {source_path}")
                    script_content = ""
            else:
                # Créer un script vide pour générer un rapport minimal
                script_content = ""
            
            # Tokeniser le script
            token_ids, tokens = tokeniser_avec_tiktoken(script_content, "gpt-4o-mini")
            
            # Reconstruire les résultats d'analyse
            amorce_tokens = max(1, min(3, len(tokens) // 3)) if tokens else 0
            resultats_analyse = process_batch_results(results, tokens, token_ids, amorce_tokens)
            
            # Construire la matrice
            matrice, structure = construire_matrice_logprob(tokens, resultats_analyse)
            
            # Sauvegarder les résultats
            matrix_path = matrix_dir / f"matrix_batch_{script_name}.npy"
            result_path = results_dir / f"result_batch_{script_name}.txt"
            
            sauvegarder_matrice_numpy(matrice, nom_fichier=str(matrix_path))
            sauvegarder_resultats(
                resultats_analyse,
                script_content,
                matrice,
                structure,
                nom_fichier=str(result_path)
            )
            
            logger.info(f"→ Matrice enregistrée : {matrix_path}")
            logger.info(f"→ Rapport enregistré  : {result_path}")
            
        except Exception as e:
            logger.error(f"Erreur lors du traitement du batch {args.batch_id}: {str(e)}")
            return
    
    # Analyse d'un dossier complet
    elif args.directory:
        # Traiter un dossier complet
        directory_path = Path(args.directory)
        if not directory_path.exists() or not directory_path.is_dir():
            parser.error(f"Dossier d'entrée introuvable ou invalide: {directory_path}")
        
        process_directory(
            directory_path, 
            output_dir,
            model_prediction=args.model,
            model_tokenisation="gpt-4o-mini",
            poll_interval=args.poll_interval,
            max_attempts=args.max_attempts,
            wait_unlimited=not args.no_wait_unlimited,
            recursive=args.recursive,
            max_connection_retries=args.max_connection_retries,
            async_mode=getattr(args, 'async', False)  # Utiliser getattr pour éviter les erreurs avec 'async'
        )
    
    # Analyse d'un nouveau fichier
    elif args.file:
        # Détermination du fichier d'entrée
        file_path = Path(args.file)
        if not file_path.exists() or not file_path.is_file():
            parser.error(f"Fichier d'entrée introuvable ou invalide: {file_path}")
        
        logger.info(f"Fichier d'entrée: {file_path}")
        
        # Chargement du script
        script = file_path.read_text(encoding='utf-8')
        
        # Lancement de l'analyse avec l'API Batch
        logger.info(f"\n--- Analyse de {file_path.name} avec l'API Batch et le modèle {args.model} ---")
        
        try:
            resultats_analyse, tokens, matrice, structure = analyze_with_batch_api(
                script,
                modele_tokenisation="gpt-4o-mini",
                modele_prediction=args.model,
                poll_interval=args.poll_interval,
                max_attempts=args.max_attempts,
                wait_unlimited=not args.no_wait_unlimited,
                max_connection_retries=args.max_connection_retries
            )
            
            # Sauvegardes
            stem = file_path.stem
            matrix_path = matrix_dir / f"matrix_batch_{stem}.npy"
            result_path = results_dir / f"result_batch_{stem}.txt"
            
            sauvegarder_matrice_numpy(matrice, nom_fichier=str(matrix_path))
            sauvegarder_resultats(
                resultats_analyse,
                script,
                matrice,
                structure,
                nom_fichier=str(result_path)
            )
            
            # Afficher un bref résumé dans la console
            total_tokens = len([r for r in resultats_analyse if not r.get("amorce", False)])
            correct_tokens = len([r for r in resultats_analyse if r.get("correct", False) and not r.get("amorce", False)])
            correct_top10_tokens = len([r for r in resultats_analyse if r.get("correct_top10", False) and not r.get("amorce", False)])
            
            logger.info(f"\nRésumé de l'analyse (Batch API):")
            logger.info(f"Total des tokens analysés: {total_tokens}")
            logger.info(f"Tokens correctement prédits (1ère position): {correct_tokens}")
            logger.info(f"Tokens correctement prédits (top 10): {correct_top10_tokens}")
            
            if total_tokens > 0:
                precision = (correct_tokens / total_tokens) * 100
                precision_top10 = (correct_top10_tokens / total_tokens) * 100
                logger.info(f"Précision (1ère position): {precision:.2f}%")
                logger.info(f"Précision (top 10): {precision_top10:.2f}%")
            
            logger.info(f"→ Matrice enregistrée : {matrix_path}")
            logger.info(f"→ Rapport enregistré  : {result_path}")
            
        except Exception as e:
            logger.error(f"Erreur lors de l'analyse du fichier {file_path}: {str(e)}")

if __name__ == "__main__":
    main() 