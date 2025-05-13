from openai import OpenAI
import time
from tqdm import tqdm
import datetime
import tiktoken

# Script Fibonacci original
script = """x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")"""

# Initialisation du client OpenAI
client = OpenAI(api_key="")

def tokeniser_avec_tiktoken(texte, modele="gpt-4o-mini"):
    """
    Tokenise le texte en utilisant tiktoken, la bibliothèque officielle d'OpenAI pour la tokenisation.
    Cette fonction utilise l'encodeur correspondant au modèle spécifié.
    
    Args:
        texte (str): Le texte à tokeniser
        modele (str): Le modèle GPT dont on veut utiliser l'encodeur (par défaut: "gpt-4o")
        
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

def analyser_predictions_token_par_token(script, modele_tokenisation="gpt-4o", modele_prediction="gpt-4o"):
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
        
        try:
            # Demander explicitement le token suivant avec ses alternatives
            # Inclure l'information sur la tokenisation tiktoken dans le prompt système
            response = client.chat.completions.create(
                model=modele_prediction,
                messages=[
                    {"role": "system", "content": """Vous êtes un prédicteur de code qui génère uniquement le prochain token sans aucun texte supplémentaire. Attention aux espaces."""},
                    {"role": "user", "content": f""" complete ce script : {contexte_actuel}"""}                
                ],
                max_tokens=1,
                logprobs=True,
                top_logprobs=10,  
                temperature=0.1,
                top_p = 0.1
            )
            
            # Extraire le token prédit et ses alternatives
            token_predit = response.choices[0].logprobs.content[0].token
            alternatives = [{"token": alt.token, "logprob": alt.logprob} for alt in response.choices[0].logprobs.content[0].top_logprobs]
            # Ajouter le résultat à notre liste
            resultats_analyse.append({
                "position": i,
                "token_id": token_id_attendu,
                "attendu": token_attendu,
                "predit": token_predit,
                "correct": token_predit == token_attendu,
                "alternatives": alternatives,
                "amorce": False
            })
            
            # Mettre à jour le contexte pour la prochaine itération
            # Note: on utilise le token attendu pour le contexte pour que
            # le modèle continue sur le texte correct
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
                "alternatives": [],
                "amorce": False
            })
            
            # Continuer avec le token attendu
            contexte_actuel += token_attendu
    print(contexte_actuel)
    return resultats_analyse

def sauvegarder_resultats(resultats_analyse, script, modele_tokenisation="gpt-4o", nom_fichier=None):
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
            
            # Utiliser repr pour une représentation claire des caractères spéciaux
            token_predit_display = repr(token_predit)[1:-1]
            
            # En-tête pour ce token
            f.write(f"Position {position}: '{token_attendu_display}' (ID: {token_id})\n")
            
            # Afficher la prédiction principale
            prediction_status = "✓ CORRECT" if correct else "✗ INCORRECT"
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
                    
                    # Vérifier si c'est le token attendu
                    is_expected = alt_token == token_attendu
                    if is_expected:
                        token_attendu_in_alternatives = True
                        token_attendu_rank = i + 1
                    
                    # Marquer le token attendu avec un astérisque
                    marker = "* " if is_expected else "  "
                    
                    # Afficher cette alternative
                    f.write(f"{marker}{i+1}. '{alt_token_display}' (logprob: {alt_logprob:.4f})")
                    
                    # Ajouter une indication si c'est aussi la prédiction principale
                    if alt_token == token_predit:
                        f.write(" [Prédiction principale]")
                    
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
        
        f.write("\nRÉSUMÉ:\n")
        f.write("-"*80 + "\n")
        f.write(f"Total des tokens analysés: {total_tokens}\n")
        f.write(f"Tokens correctement prédits: {correct_tokens}\n")
        
        if total_tokens > 0:
            precision = (correct_tokens / total_tokens) * 100
            f.write(f"Précision: {precision:.2f}%\n")
        
        f.write("="*80 + "\n")
    
    print(f"Résultats sauvegardés dans le fichier: {nom_fichier}")
    return nom_fichier

def main(script_input=None, modele_tokenisation="gpt-4o", modele_prediction="gpt-4o"):
    """Fonction principale qui exécute l'analyse"""
    
    # Utiliser le script par défaut ou celui fourni en argument
    script_to_analyze = script_input if script_input is not None else script
    
    print(f"Démarrage de l'analyse token par token avec tokenisation tiktoken ({modele_tokenisation})...")
    resultats = analyser_predictions_token_par_token(script_to_analyze, modele_tokenisation, modele_prediction)
    
    # Sauvegarder les résultats dans un fichier
    nom_fichier = f"analyse_tokens_tiktoken_{modele_tokenisation}_resultats.txt"
    sauvegarder_resultats(resultats, script_to_analyze, modele_tokenisation, nom_fichier)
    
    # Afficher un bref résumé dans la console
    total_tokens = len([r for r in resultats if not r.get("amorce", False)])
    correct_tokens = len([r for r in resultats if r.get("correct", False) and not r.get("amorce", False)])
    
    print(f"\nRésumé de l'analyse:")
    print(f"Total des tokens analysés: {total_tokens}")
    print(f"Tokens correctement prédits: {correct_tokens}")
    
    if total_tokens > 0:
        precision = (correct_tokens / total_tokens) * 100
        print(f"Précision: {precision:.2f}%")
    
    print(f"Les résultats détaillés ont été sauvegardés dans: {nom_fichier}")

# Exécuter l'analyse
if __name__ == "__main__":
    # On peut spécifier différents modèles pour la tokenisation et la prédiction
    # Par exemple: main(modele_tokenisation="gpt-4o", modele_prediction="gpt-4o")
    main()