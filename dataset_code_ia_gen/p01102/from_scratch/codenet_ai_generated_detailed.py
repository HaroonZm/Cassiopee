def split_program(s):
    """
    Sépare un programme en une liste d'éléments alternant entre :
    - chaînes hors des guillemets
    - chaînes littérales (entre guillemets)
    Exemple : 
    'read"B1input";solve;output;'
    -> ['read', 'B1input', ';solve;output;']
    
    L'indice pair dans la liste correspond à du code hors guillemets,
    l'indice impair correspond à une chaîne entre guillemets.
    """
    parts = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '"':
            # début d'une chaîne littérale
            j = i + 1
            while j < n and s[j] != '"':
                j += 1
            # s[i+1:j] est la chaîne littérale
            parts.append(s[i+1:j])
            i = j + 1
        else:
            # code hors guillemets
            j = i
            while j < n and s[j] != '"':
                j += 1
            parts.append(s[i:j])
            i = j
    return parts

def judge_programs(s1, s2):
    """
    Compare deux programmes selon les règles énoncées :
    - IDENTICAL : s1 et s2 identiques (string exactement égales)
    - CLOSE : ils ne diffèrent que par une seule chaîne littérale
    - DIFFERENT sinon
    """
    if s1 == s2:
        return "IDENTICAL"
    
    # Séparation en parties de code et chaînes littérales
    parts1 = split_program(s1)
    parts2 = split_program(s2)
    
    # Si le découpage est différent, forcément DIFFERENT
    # Le découpage doit avoir même nombre d'éléments
    # et les zones hors guillemets (indices pairs) doivent être les mêmes
    if len(parts1) != len(parts2):
        return "DIFFERENT"
    for idx in range(0, len(parts1), 2):
        if parts1[idx] != parts2[idx]:
            return "DIFFERENT"
    
    # Compter combien de chaînes littérales diffèrent
    diff_count = 0
    for idx in range(1, len(parts1), 2):
        if parts1[idx] != parts2[idx]:
            diff_count += 1
            if diff_count > 1:
                return "DIFFERENT"
    if diff_count == 1:
        return "CLOSE"
    
    # Aucun littéral différent, mais les programmes ne sont pas égaux (car cas IDENTICAL géré)
    # Cela peut arriver si il y a zéro string literal (pas de double quotes)
    # et dans ce cas si pas égal, on renvoie DIFFERENT
    return "DIFFERENT"


def main():
    while True:
        s1 = input()
        if s1 == '.':
            break
        s2 = input()
        print(judge_programs(s1, s2))


if __name__ == "__main__":
    main()