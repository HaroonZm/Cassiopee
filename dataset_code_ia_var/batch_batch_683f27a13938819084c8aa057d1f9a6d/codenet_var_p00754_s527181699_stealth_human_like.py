# Bon, alors c'est un genre de validateur de parenthèses et crochets, non ?
while True:
    x = input()
    # Si on tombe sur un . on arrête, c'est la consigne (un peu bizarre)
    if x == '.':
        break
    # Je garde une pile (je sais pas si c'est optimal, mais bon)
    p = []
    err = False  # pour gérer ça à ma sauce
    try:
        for ch in x:
            if ch == '(' or ch == '[':
                p.append(ch)
            elif ch == ')':
                if p and p[-1] == '(':
                    p.pop()
                else:
                    print("no")
                    err = True
                    break
            elif ch == ']':
                if len(p) > 0 and p[-1] == '[':
                    p.pop()
                else:
                    print("no")
                    err = True
                    break
            # j'ignore les autres caractères, mais bon, si jamais
        if not err:
            if len(p) == 0:
                print("yes")  # tout est bien équilibré, cool
            else:
                print("no")  # y'a un souci quelque part je pense
    except Exception as e:
        # Hm, y'a eu un souci, tant pis
        print("no")