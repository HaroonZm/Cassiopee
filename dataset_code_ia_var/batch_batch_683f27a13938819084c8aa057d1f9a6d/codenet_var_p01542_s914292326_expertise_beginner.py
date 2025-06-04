import itertools

def expr_valide(expr):
    if '(+' in expr or '(-' in expr or '(*' in expr:
        return False
    if '++' in expr or '+-' in expr or '-+' in expr or '--' in expr:
        return False
    if '**' in expr or '*+' in expr or '*-' in expr:
        return False

    if '(' in expr or ')' in expr:
        counts = {}
        niveau = -1
        for lettre in expr:
            if lettre == '(':
                niveau += 1
                counts[niveau] = 0
            elif lettre == ')':
                if counts[niveau] == 0:
                    return False
                niveau -= 1
            elif lettre in '+-*' and niveau in counts:
                counts[niveau] += 1
        return True
    else:
        return True

def evalue_expr(expr):
    i = 0
    resultat = ''
    tmp = []
    try:
        while i < len(expr):
            if expr[i] in '01':
                tmp.append(expr[i])
            else:
                if len(tmp) > 0:
                    nombre_bin = ''.join(tmp)
                    val = int(nombre_bin,2)
                    if val >= 1024:
                        return -99999999
                    resultat += str(val)
                resultat += expr[i]
                tmp = []
            i += 1
        if len(tmp) > 0:
            nombre_bin = ''.join(tmp)
            val = int(nombre_bin,2)
            resultat += str(val)
    except:
        return -99999999

    try:
        if expr_valide(resultat):
            val_final = eval(resultat)
            if '-' not in resultat and val_final < 1024:
                return val_final
            elif '-' in resultat and val_final < 1024:
                for i in range(len(resultat)):
                    if resultat[i] == '-':
                        milieu = i
                        gauche = milieu - 1
                        droite = milieu + 1
                        cpt = 0
                        while gauche >= 0:
                            if resultat[gauche] == ')':
                                cpt += 1
                            elif resultat[gauche] == '(':
                                cpt -= 1
                                if cpt < 0:
                                    gauche += 1
                                    break
                            if cpt == 0 and resultat[gauche] in '+-':
                                gauche += 1
                                break
                            gauche -= 1
                        gauche = max(gauche,0)
                        cpt = 0
                        while droite < len(resultat):
                            if resultat[droite] == '(':
                                cpt += 1
                            elif resultat[droite] == ')':
                                cpt -= 1
                                if cpt < 0:
                                    break
                            if cpt == 0 and resultat[droite] in '+-':
                                break
                            droite += 1
                        a = eval(resultat[gauche:milieu])
                        b = eval(resultat[milieu+1:droite])
                        if a >= 1024 or b >= 1024 or a - b < 0:
                            return -99999999
                return val_final
            else:
                return -99999999
        else:
            return -99999999
    except:
        return -99999999

ch = input()
parties = ch.split('.')
resultat_max = -1
possibles = itertools.product('01+-*()', repeat=len(parties)-1)
for tab in possibles:
    expr = parties[0]
    for i in range(len(tab)):
        expr += tab[i] + parties[i+1]
    val = evalue_expr(expr)
    if val > resultat_max:
        resultat_max = val
print(resultat_max)