def next_lexicographical_string(S):
    """
    Trouve la prochaine chaîne la plus petite dans l'ordre lexicographique
    qui est strictement supérieure à S, composée uniquement de lettres minuscules 
    sans répétition (utilisées au maximum une fois chacune). Si ce n'est pas possible,
    renvoie -1.
    
    Paramètres
    ----------
    S : str
        Chaîne composée de lettres minuscules, sans répétition.
    
    Retour
    ------
    str
        La prochaine chaîne lexicographiquement supérieure, ou "-1" si impossible.
    """
    # Si S est la permutation décroissante finale ('zyxwvutsrqponmlkjihgfedcba'), il n'y a rien après => -1
    if S == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
        return
    
    # Convertit chaque caractère en un code entier basé sur sa position dans l'alphabet (0 pour 'a', ...)
    code = list(map(lambda x: ord(x) - ord('a'), list(S)))
    done = False  # Indique si on a trouvé la solution
    
    # PREMIÈRE ÉTAPE : 
    # Cherche la plus petite lettre non utilisée.
    # Si S n'utilise pas toutes les 26 lettres, on ajoute la plus petite lettre manquante à la fin.
    for i in range(26):
        if i not in code:
            code.append(i)
            done = True
            break
    
    # DEUXIÈME ÉTAPE :
    # Si S contient déjà toutes les lettres ou si la première étape n'a pas fonctionné,
    # On cherche à permuter le suffixe pour obtenir la prochaine permutation valide.
    while len(code) > 0 and not done:
        last = code[-1]  # Dernier code du mot courant
        code = code[:-1]  # Retire le dernier caractère
        if last == 25:
            # Si c'est 'z', il faut continuer à retirer pour tenter un autre swap
            continue
        else:
            # Cherche la plus petite lettre supérieure à 'last' et qui n'était pas déjà présente
            for i in range(last+1, 26):
                if i not in code:
                    code.append(i)  # On l'ajoute à la fin
                    done = True
                    break
    
    # Reconvertit la liste des codes en lettres
    decode = list(map(lambda x: chr(x + ord('a')), code))
    # Joint les lettres en une chaîne unique et affiche le résultat
    print(''.join(decode))

if __name__ == "__main__":
    S = input()
    next_lexicographical_string(S)