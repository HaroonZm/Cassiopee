def is_ac_format(s):
    """
    Vérifie si la chaîne s est au format AC selon les règles suivantes :
    - Le premier caractère doit être 'A'.
    - Il doit y avoir exactement une lettre 'C' dans la sous-chaîne allant du 3ème au dernier caractère.
    - 'C' doit apparaître une seule fois au total dans toute la chaîne.
    - Aucun des autres caractères de la chaîne ne doit être une majuscule autre que 'A' ou 'C'.
    
    Paramètre:
        s (str): La chaîne à tester.
    
    Retourne:
        bool: True si la chaîne est au format AC, False sinon.
    """
    # Vérifie que le premier caractère est 'A'
    if s[0] != 'A':
        return False
    # Vérifie qu'il y a exactement une 'A' (au début) et une 'C' dans toute la chaîne
    if s.count('A') != 1 or s.count('C') != 1:
        return False
    # Vérifie que la 'C' apparaît dans la sous-chaîne du 3ème au dernier caractère
    if s[2:-1].count('C') != 1:
        return False
    # Définis toutes les autres majuscules sauf 'A' et 'C'
    forbidden_capitals = 'BDEFGHIJKLMNOPQRSTUVWXYZ'
    # Parcourt les majuscules interdites et vérifie qu'elles n'apparaissent pas dans la chaîne
    for t in forbidden_capitals:
        if t in s:
            return False
    # Si toutes les conditions sont respectées, la chaîne est au format AC
    return True

def main():
    """
    Fonction principale qui lit une chaîne en entrée, vérifie si elle est au format AC,
    et affiche 'AC' si c'est le cas, sinon affiche 'WA'.
    """
    # Lit l'entrée utilisateur
    s = input()
    # Vérifie le format et affiche le résultat approprié
    if is_ac_format(s):
        print('AC')
    else:
        print('WA')

# Appelle la fonction principale si ce script est exécuté directement
if __name__ == '__main__':
    main()