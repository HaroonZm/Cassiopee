from openai import OpenAI
import time
from tqdm import tqdm
import datetime
import tiktoken
import numpy as np
import os
import argparse
from pathlib import Path

def charger_script_depuis_fichier(nom_fichier):
    """
    Lit tout le contenu du fichier situé dans le répertoire 'data'
    et le renvoie comme une chaîne de caractères.
    """
    projet_racine = Path(__file__).resolve().parent.parent
    raw_dir       = projet_racine / "data" / "raw_scripts"
    chemin_fichier  = raw_dir / nom_fichier

    if not chemin_fichier.exists():
        raise FileNotFoundError(f"Fichier introuvable : {chemin_fichier}")
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        return f.read()

# Initialisation du client OpenAI
client = OpenAI(api_key="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")

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
        print(f"Encodeur pour {modele} non trouvé, utilisation de cl100k_base à la place.")
        encodeur = tiktoken.get_encoding("cl200k_base")
    
    # Encoder le texte en tokens (IDs numériques)
    token_ids = encodeur.encode(texte)
    
    # Convertir les IDs en tokens (chaînes de caractères)
    tokens = [encodeur.decode_single_token_bytes(token_id).decode('utf-8', errors='replace') for token_id in token_ids]
    
    return token_ids, tokens

def analyser_predictions_token_par_token(script, modele_tokenisation="gpt-4o-mini", modele_prediction="gpt-4o-mini"):
    """Analyse les prédictions du modèle pour chaque token du script avec tokenisation via tiktoken"""
    
    # Tokeniser le script avec tiktoken
    print(f"Tokenisation du script avec tiktoken ({modele_tokenisation})...")
    token_ids, tokens_reference = tokeniser_avec_tiktoken(script, modele_tokenisation)
    
    print(f"Nombre de tokens dans la référence tiktoken: {len(tokens_reference)}")
    print("Tokens identifiés:")
    for i, token in enumerate(tokens_reference):
        token_display = repr(token)[1:-1]  # Utiliser repr pour voir les caractères spéciaux
        print(f"{i}: '{token_display}' (ID: {token_ids[i]})")
    
    # Nouvelle liste pour stocker les résultats d'analyse
    resultats_analyse = []
    
    # Ajuster dynamiquement le nombre de tokens d'amorce
    amorce_tokens = max(1, min(3, len(tokens_reference) // 3))
    print(f"Utilisation de {amorce_tokens} tokens comme amorce sur {len(tokens_reference)} tokens au total")
    
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
    print("Analyse des tokens un par un...")
    for i in tqdm(range(amorce_tokens, len(tokens_reference))):
        token_attendu = tokens_reference[i]
        token_id_attendu = token_ids[i]
        
        # Vérifier si le token précédent est une tabulation
        token_precedent_est_tabulation = False
        if i > 0:
            token_precedent = tokens_reference[i-1]
            if ("/n" not in token_precedent ):
                token_precedent_est_tabulation = token_precedent.strip() == "" and len(token_precedent) > 1
        
        try:
            # Demander explicitement le token suivant avec ses alternatives
            response = client.chat.completions.create(
                model=modele_prediction,
                messages=[
    {"role": "system", "content": """You are a code predictor that generates only the next token without any additional text. Pay attention to spaces, tabs, line breaks, and special symbols in the code."""},
    {"role": "user", "content": f"""Code context: {contexte_actuel}"""}
],
                max_tokens=1,
                logprobs=True,
                top_logprobs=10,  
                temperature=0.0,
                top_p = 0.1
            )
            
            # Extraire le token prédit et ses alternatives
            token_predit = response.choices[0].logprobs.content[0].token
            alternatives = [{"token": alt.token, "logprob": alt.logprob} for alt in response.choices[0].logprobs.content[0].top_logprobs]
            
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
            print(f"Erreur lors de la requête pour le token {i}: {e}")
            
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
    
    print(contexte_actuel)
    return resultats_analyse, tokens_reference

def construire_matrice_logprob(tokens_reference, resultats_analyse, top_k=10):
    """
    Construit une matrice 244×244 de log probabilités,
    en padding avec 100 et anomalies à -50.
    Lève une erreur si les dimensions dynamiques dépassent 244×244.
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

    # 4) Vérifier la limite 244×244
    if n_lignes_dyn > 244 or max_tokens_dyn > 244:
        raise ValueError(
            f"Dimensions dynamiques du code ({n_lignes_dyn} lignes × "
            f"{max_tokens_dyn} tokens par ligne) dépassent la limite 244×244."
        )

    # 5) Forcer la taille fixe
    n_lignes, max_tokens = 244, 244
    print(f"Construction d'une matrice FIXE : {n_lignes} lignes × {max_tokens} colonnes (padding=100)")

    # 6) Initialiser la matrice de padding
    matrice = np.full((n_lignes, max_tokens), 100.0)

    # 7) Remplir la matrice avec log-probabilités ou valeurs spéciales
    for idx_token, (i, j) in enumerate(position_tokens_dans_matrice):
        # Ignorer toute position hors de la matrice fixe
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

    # 8) Retourner la matrice fixe et la structure complète
    structure_tokens = {
        "fixed_lignes": n_lignes,
        "fixed_max_tokens": max_tokens,
        "dyn_lignes": n_lignes_dyn,
        "dyn_max_tokens": max_tokens_dyn,
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
    print("\nMATRICE BRUTE DE LOG PROBABILITÉS:")
    print(f"Dimensions: {matrice.shape[0]} lignes x {matrice.shape[1]} colonnes")
    
    # Calculer la largeur maximale pour l'affichage
    max_width = 10  # Largeur par défaut pour chaque valeur
    
    # Créer une ligne de séparation
    header_sep = "-" * (max_width * matrice.shape[1] + 10)
    print(header_sep)
    
    # Afficher les indices de colonnes
    print("     ", end="")
    for j in range(matrice.shape[1]):
        print(f"{j:^{max_width}}", end="")
    print()  # Nouvelle ligne
    
    # Ligne de séparation après les indices de colonnes
    print("     " + "-" * (max_width * matrice.shape[1]))
    
    # Afficher chaque ligne avec son indice
    for i in range(matrice.shape[0]):
        print(f"{i:3d} |", end="")
        for j in range(matrice.shape[1]):
            val = matrice[i, j]
            if val == 100:
                # Padding
                print(f"{'PAD':^{max_width}}", end="")
            elif val == -50:
                # Anomalie
                print(f"{'ANOM':^{max_width}}", end="")
            else:
                # Log probabilité normale
                print(f"{val:^{max_width}.4f}", end="")
        print()  # Nouvelle ligne
    
    # Ligne de séparation finale
    print(header_sep)
    
    # Légende (une seule fois)
    print("Légende:")
    print("  - PAD  : Padding (valeur 100)")
    print("  - ANOM : Anomalie (valeur -50)")
    print("  - Autres valeurs : Log probabilités réelles")
    print(header_sep)

def sauvegarder_resultats(resultats_analyse, script, matrice, structure_tokens, modele_tokenisation="gpt-4o-mini", nom_fichier=None):
    """Sauvegarde les résultats d'analyse dans un fichier texte bien formaté"""
    
    if nom_fichier is None:
        # Générer un nom de fichier basé sur la date et l'heure
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_fichier = f"analyse_tokens_{timestamp}.txt"
    
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        # Écrire l'en-tête
        f.write("="*80 + "\n")
        f.write("ANALYSE DES PRÉDICTIONS DE TOKENS\n")
        f.write("="*80 + "\n\n")
        
        # Écrire le script original
        f.write("SCRIPT ORIGINAL:\n")
        f.write("-"*80 + "\n")
        f.write(script + "\n")
        f.write("-"*80 + "\n\n")
        
        # Écrire l'information sur la tokenisation
        f.write("INFORMATION SUR LA TOKENISATION:\n")
        f.write("-"*80 + "\n")
        f.write(f"Tokenisation utilisée: tiktoken pour le modèle {modele_tokenisation}\n")
        f.write("Il s'agit de la tokenisation officielle utilisée par les modèles OpenAI.\n")
        f.write("-"*80 + "\n\n")
        
        # Écrire la liste des tokens identifiés
        f.write("TOKENS IDENTIFIÉS:\n")
        f.write("-"*80 + "\n")
        
        for resultat in resultats_analyse:
            i = resultat["position"]
            token = resultat["attendu"]
            token_id = resultat.get("token_id", "N/A")
            
            # Utiliser repr pour une représentation claire des caractères spéciaux
            token_display = repr(token)[1:-1]
            
            f.write(f"Token {i}: '{token_display}' (ID: {token_id})\n")
        
        f.write("-"*80 + "\n\n")
        
        # Ajouter des informations sur la matrice 2D
        f.write("INFORMATIONS SUR LA MATRICE 2D DE LOG PROBABILITÉS:\n")
        f.write("-"*80 + "\n")
        f.write(f"Dimensions de la matrice: {structure_tokens['lignes']} lignes x {structure_tokens['max_tokens']} tokens max\n")
        f.write(f"Nombre de tokens par ligne: {structure_tokens['tokens_par_ligne']}\n")
        f.write("Convention de valeurs:\n")
        f.write("  - Log probabilité normale: Valeur réelle (typiquement entre -1 et -20)\n")
        f.write("  - Anomalie (token hors top-10): -50\n")
        f.write("  - Padding (positions vides): 100\n\n")
        
        f.write("Matrice 2D (format texte simplifiée):\n")
        for i in range(matrice.shape[0]):
            f.write("[")
            for j in range(matrice.shape[1]):
                val = matrice[i, j]
                if val == 100:
                    f.write("PAD, ")
                elif val == -50:
                    f.write("ANOM, ")
                else:
                    f.write(f"{val:.2f}, ")
            f.write("]\n")
        
        f.write("\nNote: La matrice a été sauvegardée au format numpy dans 'matrice_logprob.npy'\n")
        f.write("-"*80 + "\n\n")
        
        # Écrire les résultats d'analyse
        f.write("ANALYSE TOKEN PAR TOKEN:\n")
        f.write("-"*80 + "\n")
        
        for resultat in resultats_analyse:
            position = resultat["position"]
            token_attendu = resultat["attendu"]
            token_id = resultat.get("token_id", "N/A")
            
            # Utiliser repr pour une représentation claire des caractères spéciaux
            token_attendu_display = repr(token_attendu)[1:-1]
            
            # Si c'est un token d'amorce, afficher différemment
            if resultat.get("amorce", False):
                f.write(f"Position {position}: '{token_attendu_display}' (ID: {token_id}) (token d'amorce)\n")
                f.write("-"*80 + "\n\n")
                continue
            
            # Pour les tokens normaux
            token_predit = resultat.get("predit", "INCONNU")
            correct = resultat.get("correct", False)
            correct_adapte = resultat.get("correct_adapte", False)
            correct_top10 = resultat.get("correct_top10", False)
            token_precedent_est_tabulation = resultat.get("token_precedent_est_tabulation", False)
            
            # Utiliser repr pour une représentation claire des caractères spéciaux
            token_predit_display = repr(token_predit)[1:-1]
            
            # En-tête pour ce token
            f.write(f"Position {position}: '{token_attendu_display}' (ID: {token_id})")
            
            # Mentionner si le token précédent est une tabulation
            if token_precedent_est_tabulation:
                f.write(" [Après tabulation]")
            
            f.write("\n")
            
            # Afficher la prédiction principale
            if correct:
                prediction_status = "✓ CORRECT"
            elif correct_adapte:
                prediction_status = "✓ CORRECT (avec adaptation)"
                # Si la prédiction est correcte après adaptation, afficher la forme attendue
                token_sans_espace = token_attendu.lstrip(" ")
                if token_predit == token_sans_espace:
                    f.write(f"Note: Le token prédit '{token_predit_display}' est considéré correct ")
                    f.write(f"car il correspond au token attendu sans l'espace initial.\n")
            else:
                prediction_status = "✗ INCORRECT"
            
            f.write(f"Prédiction principale: '{token_predit_display}' ({prediction_status})\n\n")
            
            # Afficher les alternatives
            f.write("Top 10 tokens les plus probables:\n")
            
            # Vérifier si nous avons des alternatives
            alternatives = resultat.get("alternatives", [])
            if alternatives:
                # Déterminer si le token attendu est dans les alternatives
                token_attendu_in_alternatives = False
                token_attendu_rank = -1
                
                for i, alt in enumerate(alternatives):
                    alt_token = alt["token"]
                    alt_logprob = alt["logprob"]
                    
                    # Utiliser repr pour une représentation claire des caractères spéciaux
                    alt_token_display = repr(alt_token)[1:-1]
                    
                    # Vérifier si c'est le token attendu (normal ou adapté)
                    is_expected = alt_token == token_attendu
                    is_expected_adapte = alt.get("adapte", False)
                    
                    if is_expected:
                        token_attendu_in_alternatives = True
                        token_attendu_rank = i + 1
                    elif is_expected_adapte and not token_attendu_in_alternatives:
                        token_attendu_in_alternatives = True
                        token_attendu_rank = i + 1
                    
                    # Marquer le token attendu avec un astérisque
                    marker = "* " if (is_expected or is_expected_adapte) else "  "
                    
                    # Afficher cette alternative
                    f.write(f"{marker}{i+1}. '{alt_token_display}' (logprob: {alt_logprob:.4f})")
                    
                    # Ajouter une indication si c'est aussi la prédiction principale
                    if alt_token == token_predit:
                        f.write(" [Prédiction principale]")
                    
                    # Ajouter une indication si c'est un token adapté
                    if is_expected_adapte:
                        token_adapte_display = repr(alt.get("token_adapte", token_attendu))[1:-1]
                        f.write(f" [Correspond à '{token_adapte_display}' avec adaptation]")
                    
                    f.write("\n")
                
                # Si le token attendu n'est pas dans les alternatives, le mentionner
                if not token_attendu_in_alternatives and token_attendu != token_predit:
                    f.write("\nLe token attendu n'est pas dans le top 10 des prédictions.\n")
                elif token_attendu_rank > 0:
                    f.write(f"\nLe token attendu est à la position {token_attendu_rank} dans les prédictions.\n")
            else:
                f.write("Aucune alternative disponible (erreur possible).\n")
            
            # Séparateur entre les tokens
            f.write("\n" + "-"*80 + "\n\n")
        
        # Écrire un résumé
        total_tokens = len([r for r in resultats_analyse if not r.get("amorce", False)])
        correct_tokens = len([r for r in resultats_analyse if r.get("correct", False) and not r.get("amorce", False)])
        correct_adapte_tokens = len([r for r in resultats_analyse if r.get("correct_adapte", False) and not r.get("amorce", False)])
        correct_top10_tokens = len([r for r in resultats_analyse if r.get("correct_top10", False) and not r.get("amorce", False)])
        
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
    
    print(f"Résultats sauvegardés dans le fichier: {nom_fichier}")
    return nom_fichier

def sauvegarder_matrice_numpy(matrice, nom_fichier="matrice_logprob.npy"):
    """
    Sauvegarde la matrice au format numpy pour une utilisation ultérieure.
    
    Args:
        matrice (numpy.ndarray): La matrice 2D de log probabilités
        nom_fichier (str): Nom du fichier pour sauvegarder la matrice
    """
    np.save(nom_fichier, matrice)
    print(f"Matrice sauvegardée au format numpy dans {nom_fichier}")

def main(script_input=None, modele_tokenisation="gpt-4o-mini", modele_prediction="gpt-4o-mini"):
    """Fonction principale qui exécute l'analyse"""
    
    # Utiliser le script par défaut ou celui fourni en argument
    script_to_analyze = script_input if script_input is not None else script
    
    print(f"Démarrage de l'analyse token par token avec tokenisation tiktoken ({modele_tokenisation})...")
    resultats_analyse, tokens_reference = analyser_predictions_token_par_token(script_to_analyze, modele_tokenisation, modele_prediction)
    
    # Construire la matrice 2D de log probabilités
    matrice, structure_tokens = construire_matrice_logprob(tokens_reference, resultats_analyse)
    
    # Afficher la matrice brute dans la console
    afficher_matrice_brute(matrice, structure_tokens)
    
    # Sauvegarder la matrice au format numpy
    sauvegarder_matrice_numpy(matrice)
    
    # Sauvegarder les résultats dans un fichier
    nom_fichier = "resultats.txt"
    sauvegarder_resultats(resultats_analyse, script_to_analyze, matrice, structure_tokens, modele_tokenisation, nom_fichier)
    
    # Afficher un bref résumé dans la console
    total_tokens = len([r for r in resultats_analyse if not r.get("amorce", False)])
    correct_tokens = len([r for r in resultats_analyse if r.get("correct", False) and not r.get("amorce", False)])
    correct_top10_tokens = len([r for r in resultats_analyse if r.get("correct_top10", False) and not r.get("amorce", False)])
    
    print(f"\nRésumé de l'analyse:")
    print(f"Total des tokens analysés: {total_tokens}")
    print(f"Tokens correctement prédits (1ère position): {correct_tokens}")
    print(f"Tokens correctement prédits (top 10): {correct_top10_tokens}")
    
    if total_tokens > 0:
        precision = (correct_tokens / total_tokens) * 100
        precision_top10 = (correct_top10_tokens / total_tokens) * 100
        print(f"Précision (1ère position): {precision:.2f}%")
        print(f"Précision (top 10): {precision_top10:.2f}%")
       
    return matrice, structure_tokens

if __name__ == "__main__":
    # Répertoires racine
    projet_racine = Path(__file__).resolve().parent.parent
    raw_dir       = projet_racine / "data" / "raw_scripts"

    # CLI
    parser = argparse.ArgumentParser(
        description="Analyse des prédictions token par token pour un ou plusieurs scripts.")
    parser.add_argument(
        "-f", "--file",
        help="Nom du fichier unique à analyser (dans data/raw_scripts/). Ex: 'foo.py'",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--all",
        help="Analyser tous les fichiers Python (*.py) du dossier data/raw_scripts/",
        action="store_true",
    )
    args = parser.parse_args()

    # Détermination des fichiers à traiter
    if args.all:
        fichiers = sorted(raw_dir.glob("*.py"))
        if not fichiers:
            parser.error(f"Aucun .py trouvé dans {raw_dir}")
    else:
        nom    = args.file or "script.py"
        chemin = raw_dir / nom
        if not chemin.exists():
            parser.error(f"Fichier introuvable : {chemin}")
        fichiers = [chemin]

    # Boucle d'analyse
    for fpath in fichiers:
        stem = fpath.stem  # nom sans extension, ex: "gen_example"

        # 1) Choix du dossier de sortie selon le préfixe
        if stem.startswith(("gen", "var")):
            base_out = projet_racine / "data" / "ia"
        else:
            base_out = projet_racine / "data" / "nia"

        matrix_dir  = base_out / "matrice"
        results_dir = base_out / "resultats"

        # Création des dossiers si nécessaire
        matrix_dir.mkdir(parents=True, exist_ok=True)
        results_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n--- Analyse de {fpath.name} ---")
        print(f"→ Résultats dans : {base_out}")

        # 2) Chargement et exécution de l'analyse
        script = fpath.read_text(encoding="utf-8")
        resultats_analyse, tokens_reference = analyser_predictions_token_par_token(
            script,
            modele_tokenisation="gpt-4o-mini",
            modele_prediction="gpt-4o-mini"
        )
        matrice, structure = construire_matrice_logprob(tokens_reference, resultats_analyse)

        # 3) Sauvegardes
        matrix_path = matrix_dir  / f"matrix_{stem}.npy"
        result_path = results_dir / f"result_{stem}.txt"

        sauvegarder_matrice_numpy(matrice, nom_fichier=str(matrix_path))
        sauvegarder_resultats(
            resultats_analyse,
            script,
            matrice,
            structure,
            nom_fichier=str(result_path)
        )

        print(f"→ Matrice enregistrée : {matrix_path.name}")
        print(f"→ Rapport enregistré  : {result_path.name}")
