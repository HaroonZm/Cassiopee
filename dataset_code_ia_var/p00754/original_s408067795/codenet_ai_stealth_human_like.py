# Boucle infinie, on sort quand l'utilisateur tape '.'
while 1:
    s = input()
    if s == '.':
        break  # c'est fini

    answer = True  # je crois que tout va bien
    pile = []
    for ch in s:
        # parenthèses ouvrantes
        if ch == '(' or ch == '[':
            val = 1
            if ch == '[':
                val = -1  # on distingue [] et ()
            if pile == [] or pile[-1] * val < 0:
                pile.append(val)
            else:
                pile[-1] += val  # un peu bizarre comme logique mais je garde

        # parenthèses fermantes
        if ch == ')' or ch == ']':
            val = 1
            if ch == ']':
                val = -1
            if len(pile) == 0 or pile[-1] * val < 0:
                answer = False
                break
            else:
                pile[-1] -= val
                if pile[-1] == 0:
                    pile = pile[:-1]  # on enlève la paire fermée

    if pile != []:
        answer = False

    # je préfère les minuscules, mais c'est une question de goût
    print('yes' if answer else 'no')