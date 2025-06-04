import sys

def check_string_format():
    """
    Vérifie si une chaîne saisie respecte les règles suivantes :
    1. Le premier caractère est 'A'.
    2. La chaîne contient exactement un 'C' dans la partie entre le deuxième et l'avant-dernier caractère.
    3. Tous les autres caractères sont en minuscules.
    Affiche 'AC' si la chaîne respecte ces règles, sinon affiche 'WA'.
    """
    s = list(input())  # Convertit la chaîne d'entrée en une liste de caractères pour manipulation

    # Vérifie que le premier caractère est 'A'
    if s[0] == 'A':
        del s[0]  # Supprime le 'A' pour traiter le reste de la chaîne

        # Compte le nombre de fois où 'C' apparaît dans la sous-liste sans le premier ni le dernier caractère
        if s[1:-1].count('C') == 1:
            s.remove('C')  # Enlève la première occurrence de 'C' pour valider les minuscules ensuite

            # Vérifie que tous les autres caractères sont en minuscules
            for i in range(len(s)):
                if s[i].isupper():
                    print('WA')  # Si une majuscule est trouvée, la chaîne est incorrecte
                    sys.exit()

            print('AC')  # La chaîne respecte toutes les règles
        else:
            print('WA')  # 'C' n'apparaît pas exactement une fois au bon endroit
    else:
        print('WA')  # Le premier caractère n'est pas 'A'

if __name__ == "__main__":
    check_string_format()