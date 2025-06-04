def check_sequence(s):
    """
    Analyse la chaîne de caractères s pour déterminer la présence d'un schéma particulier.
    
    Plus précisément :
    - Recherche la première occurrence du caractère 'C'
    - Si une occurrence est trouvée, vérifie si 'F' apparaît quelque part après ce 'C'
    - Affiche 'Yes' si le schéma est trouvé ('C' suivi de 'F'), sinon affiche 'No'
    
    Paramètres:
        s (str): Chaîne de caractères à analyser.
    
    Retour:
        None (affiche le résultat)
    """
    # Vérifie si la chaîne contient la lettre 'C'
    if 'C' in s:
        # Trouve l'indice de la première occurrence de 'C'
        i = s.index('C')
        # Recherche le caractère 'F' dans la sous-chaîne située après le 'C' trouvé
        found_f_after_c = 'F' in s[i+1:]
        # Affiche 'Yes' si 'F' est trouvé après 'C', sinon affiche 'No'
        print('NYoe s'[::-2][found_f_after_c])  # 'NYoe s'[::-2] donne 'Yes', 'No' selon l'index booléen
    else:
        # Si 'C' n'est pas présent, affiche 'No'
        print('No')
        
if __name__ == "__main__":
    # Demande à l'utilisateur de saisir une chaîne de caractères
    s = input()
    # Analyse la chaîne saisie
    check_sequence(s)