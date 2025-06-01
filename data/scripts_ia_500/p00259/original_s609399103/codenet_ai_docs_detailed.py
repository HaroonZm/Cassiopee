from collections import deque
import sys
import math
import re

def reverse_polish_notation(exp):
    """
    Convertit une expression arithmétique infixe en une expression en notation polonaise inversée (RPN).
    
    Args:
        exp (list of str): Liste des tokens de l'expression infixe (nombres, opérateurs, parenthèses).
        
    Returns:
        deque: Une deque représentant l'expression en notation polonaise inversée.
    
    Fonctionnement:
        Utilise l'algorithme de Shunting Yard adapté en traitant l'expression de droite à gauche,
        avec une table de priorité pour les opérateurs.
    """
    # Définition de la priorité des opérateurs : + et - (priorité 0), * et / (priorité 1)
    priority = {'+': 0, '-': 0, '/': 1, '*': 1}
    exp = deque(exp)  # Conversion en deque pour un accès efficace sur la fin
    stack = deque()   # Pile utilisée pour stocker les opérateurs
    buffer = deque()  # Buffer final pour la RPN

    while len(exp):
        token = exp.pop()  # Traiter du dernier token vers le premier
        if token.isnumeric():
            # Les nombres sont directement ajoutés au buffer RPN
            buffer.append(token)
        elif token == '(':
            # Lorsqu'on rencontre une parenthèse ouvrante dans cette lecture inversée,
            # on dépile les opérateurs jusqu'à la parenthèse fermante correspondante
            while True:
                token = stack.pop()
                if token == ')':
                    break
                buffer.append(token)
        elif token == ')':
            # Les parenthèses fermantes sont simplement empilées et serviront de marqueurs
            stack.append(token)
        else:
            # Pour un opérateur, on dépile les opérateurs de priorité supérieure strictement plus élevée
            # sauf s'il s'agit d'une parenthèse fermante
            while len(stack):
                if stack[-1] == ')' or priority[stack[-1]] <= priority[token]:
                    break
                buffer.append(stack.pop())
            stack.append(token)

    # Une fois tous les tokens traités, on ajoute les opérateurs restants dans le buffer
    while len(stack):
        buffer.append(stack.pop())

    return buffer


def power(x, n, p):
    """
    Calcule x^n modulo p en utilisant l'exponentiation rapide.
    
    Args:
        x (int): Base.
        n (int): Exposant.
        p (int): Modulo (doit être un nombre premier pour l'inverse modulaire).
        
    Returns:
        int: Résultat de (x^n) mod p.
    
    Notes:
        Cette fonction exploite la récursion et utilise la propriété que (x^n) mod p peut être calculé en divisant l'exposant par 2.
        Elle est utilisée notamment pour calculer l'inverse modulaire dans le corps fini Z_p lorsque p est premier.
    """
    if n == 0:
        return 1
    res = power(x * x % p, n // 2, p)
    if n & 1:  # Si n est impair, on multiplie par x supplémentaire
        res = res * x % p
    return res


def getval(p, exp):
    """
    Évalue une expression arithmétique donnée en notation polonaise inversée modulo un entier p.
    
    Args:
        p (int): Modulo.
        exp (list of str): Expression sous forme de liste de tokens en notation infixe (avant conversion).
        
    Returns:
        int or float: Résultat de l'expression modulo p, ou float('nan') en cas de division par zéro modulo.
        
    Fonctionnement:
        - Convertit l'expression en notation polonaise inversée (RPN).
        - Utilise une pile pour évaluer la RPN selon les opérateurs modulo p.
        - Gère la division modulo en utilisant l'inverse modulaire (en supposant que p est premier).
        - Retourne NaN si division par zéro.
    """
    exp = reverse_polish_notation(exp)  # Conversion vers RPN
    stack = deque()
    while len(exp):
        token = exp.popleft()
        if token.isnumeric():
            # Les nombres sont empilés
            stack.append(int(token))
        else:
            # On dépile deux opérandes pour appliquer l'opérateur
            a, b = stack.pop(), stack.pop()
            if token == '+':
                stack.append((a + b) % p)
            elif token == '-':
                stack.append((a - b) % p)
            elif token == '*':
                stack.append((a * b) % p)
            elif token == '/':
                # Division modulo : multiplication par l'inverse modulaire de b mod p
                if b == 0:
                    # Division par zéro détectée, retourne NaN
                    stack.append(float('nan'))
                else:
                    inv_b = power(b, p - 2, p)  # Calcul de l'inverse modulaire de b modulo p
                    stack.append((a * inv_b) % p)

    return stack.pop()


# Compilation du pattern pour découper l'expression en nombres et symboles
pattern = re.compile(r'(\d+|\D)')

# Lecture en boucle des entrées jusqu'à la condition d'arrêt (p=0)
f = sys.stdin
while True:
    line = f.readline()
    if not line:
        break
    p, exp = line.split(':')
    if p == '0':
        break
    exp = ''.join(exp.split()).strip()  # Enlève espaces inutiles
    
    # Analyse lexicale de l'expression
    tokens = pattern.findall(exp)
    val = getval(int(p), tokens)
    
    if math.isnan(val):
        print('NG')  # Affiche NG si calcul impossible (division par zéro modulaire)
    else:
        print('{} = {} (mod {})'.format(exp, val, p))  # Affiche le résultat modulo p