from openai import OpenAI
import time
from tqdm import tqdm
import datetime

# Script Fibonacci original
script = """ x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")"""

# Initialisation du client OpenAI
client = OpenAI(api_key="")

def analyser_predictions_token_par_token(script):
    """Analyse les prédictions du modèle pour chaque token du script original"""
    
    # 1. D'abord, générer la réponse complète pour avoir la tokenisation de référence
    print("Génération de la réponse complète pour référence...")
    response_complete = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Reecrit exactement sans caracteres supplementaires : \n\n{script}\n\n"}
        ],
        max_tokens=500,
        logprobs=True,
        top_logprobs=1
    )
    
    # Extraire les tokens de référence
    tokens_reference = []
    for token_info in response_complete.choices[0].logprobs.content:
        tokens_reference.append({
            "token": token_info.token,
            "logprob": token_info.logprob
        })
    
    print(f"Nombre de tokens dans la référence: {len(tokens_reference)}")
    
    # Nouvelle liste pour stocker les résultats d'analyse
    resultats_analyse = []
    
    # Ajuster dynamiquement le nombre de tokens d'amorce en fonction de la longueur totale
    amorce_tokens = max(1, min(3, len(tokens_reference) // 3))  # Au plus 1/3 du total, minimum 1
    print(f"Utilisation de {amorce_tokens} tokens comme amorce sur {len(tokens_reference)} tokens au total")
    
    # Initialiser le contexte avec les tokens d'amorce
    contexte_initial = ""
    for i in range(min(amorce_tokens, len(tokens_reference))):
        contexte_initial += tokens_reference[i]["token"]
        
        # Ajouter à notre liste de résultats (sans prédiction pour l'amorce)
        resultats_analyse.append({
            "position": i,
            "attendu": tokens_reference[i]["token"],
            "amorce": True,
            "alternatives": []
        })
    
    contexte_actuel = contexte_initial
    
    # Analyser token par token à partir du premier token après l'amorce
    print("Analyse des tokens un par un...")
    for i in tqdm(range(amorce_tokens, len(tokens_reference))):
        token_attendu = tokens_reference[i]["token"]
        
        try:
            # Demander explicitement le token suivant avec ses alternatives
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Vous êtes un prédicteur de code qui génère uniquement le prochain token sans aucun texte supplémentaire."},
                    {"role": "user", "content": f"Code incomplet:\n```\n{contexte_actuel}\n```\nPrédisez strictement le prochain token unique qui complèterait naturellement ce code . Répondez par ce token uniquement, sans guillemets ni explications."}                
                ],
                max_tokens=1,
                logprobs=True,
                top_logprobs=10  # Demander les 10 tokens les plus probables
            )
            
            # Extraire le token prédit et ses alternatives
            token_predit = response.choices[0].logprobs.content[0].token
            alternatives = [{"token": alt.token, "logprob": alt.logprob} for alt in response.choices[0].logprobs.content[0].top_logprobs]
            
            # Ajouter le résultat à notre liste
            resultats_analyse.append({
                "position": i,
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
                "attendu": token_attendu,
                "predit": "ERROR",
                "correct": False,
                "alternatives": [],
                "amorce": False
            })
            
            # Continuer avec le token attendu
            contexte_actuel += token_attendu
    
    return resultats_analyse

def sauvegarder_resultats(resultats_analyse, script, nom_fichier=None):
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
        
        # Écrire les résultats d'analyse
        f.write("ANALYSE TOKEN PAR TOKEN:\n")
        f.write("-"*80 + "\n")
        
        for resultat in resultats_analyse:
            position = resultat["position"]
            token_attendu = resultat["attendu"]
            
            # Échapper les caractères spéciaux pour une meilleure lisibilité
            token_attendu_display = token_attendu.replace('\n', '\\n').replace('\t', '\\t')
            if token_attendu == ' ':
                token_attendu_display = '␣'  # Caractère spécial pour l'espace
            
            # Si c'est un token d'amorce, afficher différemment
            if resultat.get("amorce", False):
                f.write(f"Position {position}: '{token_attendu_display}' (token d'amorce)\n")
                f.write("-"*80 + "\n\n")
                continue
            
            # Pour les tokens normaux
            token_predit = resultat.get("predit", "INCONNU")
            correct = resultat.get("correct", False)
            
            # Échapper le token prédit pour une meilleure lisibilité
            token_predit_display = token_predit.replace('\n', '\\n').replace('\t', '\\t')
            if token_predit == ' ':
                token_predit_display = '␣'  # Caractère spécial pour l'espace
            
            # En-tête pour ce token
            f.write(f"Position {position}: '{token_attendu_display}'\n")
            
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
                    
                    # Échapper pour l'affichage
                    alt_token_display = alt_token.replace('\n', '\\n').replace('\t', '\\t')
                    if alt_token == ' ':
                        alt_token_display = '␣'
                    
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

def main(script_input=None):
    """Fonction principale qui exécute l'analyse"""
    
    # Utiliser le script par défaut ou celui fourni en argument
    script_to_analyze = script_input if script_input is not None else script
    
    print("Démarrage de l'analyse token par token...")
    resultats = analyser_predictions_token_par_token(script_to_analyze)
    
    # Sauvegarder les résultats dans un fichier
    nom_fichier = "analyse_tokens_resultats.txt"
    sauvegarder_resultats(resultats, script_to_analyze, nom_fichier)
    
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
    main()