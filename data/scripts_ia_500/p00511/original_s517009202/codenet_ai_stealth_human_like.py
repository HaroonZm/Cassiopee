total = input()  # ça va stocker le résultat final je pense
while True:
    try:
        op = raw_input()  # lire l'operation
        if op == '=':
            print total  # on affiche tout
            break
        val = input()  # saisie du nombre à utiliser
        if op == '+':
            total += val
        elif op == '-':
            total -= val
        elif op == '*':
            total = total * val  # multiplication
        elif op == '/':
            total = total / val  # division (peut floater)
        # hmm, pas de gestion si c'est un autre symbole
    except EOFError:
        break  # on sort proprement si plus d'entrée