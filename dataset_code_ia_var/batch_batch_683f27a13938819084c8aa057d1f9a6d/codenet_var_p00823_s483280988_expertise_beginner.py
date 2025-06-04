import sys

sys.setrecursionlimit(1000000)

m = {}
m2 = {}

def is_digit(ch):
    if len(ch) == 0:
        return False
    val = ord(ch)
    return ord('0') <= val <= ord('9')

# Lecture de la première partie
while True:
    line = raw_input()
    if line == 'END_OF_FIRST_PART':
        break
    parts = line.split()
    atom = parts[0]
    w = parts[1]
    if len(atom) >= 2:
        m2[atom] = w
    else:
        m[atom] = w

# Lecture de la deuxième partie
while True:
    line = raw_input()
    if line == '0':
        break
    S = line
    SS = ""
    for i in range(len(S) - 1):
        SS = SS + S[i]
        if not is_digit(S[i]) and is_digit(S[i + 1]):
            SS = SS + '*'
        if is_digit(S[i]) and not is_digit(S[i + 1]):
            SS = SS + '+'
    SS = SS + S[-1]

    S2 = '(' + SS + ')'
    # Remplacer les atomes par leur valeur avec + ajouté
    for key in m2:
        S2 = S2.replace(key, m2[key] + '+')
    for key in m:
        S2 = S2.replace(key, m[key] + '+')

    # Nettoyage des + superflus
    S2 = S2.replace('+*', '*')
    S2 = S2.replace('+)', ')')
    try:
        result = eval(S2)
    except:
        result = 'UNKNOWN'
    print result