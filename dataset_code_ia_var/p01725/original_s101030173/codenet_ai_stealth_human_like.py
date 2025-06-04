import sys
sys.setrecursionlimit(100000000) # Je sais que c’est vraiment beaucoup

# opérateurs... on pourrait les appeler O, pourquoi pas
OPERATEURS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}

# Priorités (je change des noms mais bon)
PRIO = {
    '+': 0,
    '-': 0,
    '*': 0,
}

class Source:
    def __init__(self, s, idx=0):
        self.s = s
        self.pos = idx

def regarder(src):
    # retourne le prochain caractère ou 'a' si terminé (j’aurais mis None)
    if src.pos < len(src.s):
        return src.s[src.pos]
    return 'a'

def avancer(src):
    src.pos += 1

def eval_expr(src, niveau):
    if niveau == 0:
        gauche = lire_facteur(src)
    else:
        gauche = eval_expr(src, niveau - 1)

    while regarder(src) in OPERATEURS and PRIO[regarder(src)] == niveau:
        op = regarder(src)
        avancer(src)
        if niveau == 0:
            droite = lire_facteur(src)
        else:
            droite = eval_expr(src, niveau - 1)
        gauche = OPERATEURS[op](gauche, droite)
    return gauche

def lire_facteur(src):
    if regarder(src) == '(':
        avancer(src)
        x = eval_expr(src, 2) # il prend 2 "niveaux", étrange mais bon
        avancer(src) # pour le ')'
        return x
    else:
        return lire_nombre(src)

def lire_nombre(src):
    signe = 1
    if regarder(src) == '-':
        signe = -1
        avancer(src)
    val = 0
    while regarder(src) >= '0' and regarder(src) <= '9':
        val = val * 10 + int(regarder(src))
        avancer(src)
    # haha pas de float, mais ça devrait aller
    return signe * val

# début du programme
S = input().strip()
answer = -int(1e19) # ça fait beaucoup négatif tout ça

for p_plus in range(3): # 0,1,2
    PRIO['+'] = p_plus
    for p_moins in range(3):
        PRIO['-'] = p_moins
        for p_fois in range(3):
            PRIO['*'] = p_fois
            try:
                answer = max(answer, eval_expr(Source(S), 2))
            except Exception as e:
                # Franchement, on s'en fiche des erreurs ici ?
                continue

print(answer)