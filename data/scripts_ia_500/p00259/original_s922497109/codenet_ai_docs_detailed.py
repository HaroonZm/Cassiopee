import sys
from string import digits

# Augmente la limite maximale de récursion pour permettre une profondeur d'appel élevée
sys.setrecursionlimit(10**6)

def calc(S, MOD):
    """
    Évalue une expression arithmétique donnée en chaîne de caractères S modulo MOD.
    L'expression peut contenir les opérateurs +, -, *, / ainsi que des nombres entiers et des parenthèses.
    La division est prise modulo MOD via l'inverse multiplicatif.
    
    Args:
        S (str): L'expression arithmétique à évaluer, sans espaces.
        MOD (int): Le module pour les opérations arithmétiques.
        
    Returns:
        int: Le résultat de l'expression modulo MOD si valide,
             -1 si une erreur de division par zéro apparaît (division modulaire impossible).
    """
    L = len(S)  # Longueur de la chaîne d'expression
    S = S + "$"  # Ajout d'un marqueur de fin pour simplifier les conditions de sortie
    ok = 1       # Flag pour indiquer si l'expression est valide (pas de division par zéro)
    cur = 0      # Curseur indiquant la position actuelle dans la chaîne S

    def expr():
        """
        Analyse et calcule les expressions avec les opérateurs + et -.
        Gère la priorité en appelant la fonction term() pour les sous-expressions constituées
        des opérations * et /.
        
        Utilise un accumulateur pour appliquer successivement les additions et soustractions.
        
        Returns:
            int: Résultat partiel de l'expression modulo MOD.
        """
        nonlocal cur
        op = "+"    # Opérateur courant initialisé à addition
        res = 0     # Résultat accumulé
        while cur < L:
            val = term()  # Évalue un terme (multiplications et divisions)
            if op == "+":
                res += val
            else:  # op == "-"
                res -= val
            res %= MOD  # Réduction modulo MOD
            if S[cur] not in "+-":  # Si le caractère courant n'est pas un opérateur + ou -
                break
            op = S[cur]  # Mémorise l'opérateur pour la prochaine itération
            cur += 1     # Avance le curseur après l'opérateur
        return res % MOD

    def term():
        """
        Analyse et calcule les expressions avec les opérateurs * et /.
        Ces opérations ont une priorité plus élevée que + et -.
        
        La division est traitée comme une multiplication par l'inverse modulo MOD.
        Si une division par zéro est détectée, le flag ok est mis à 0.
        
        Returns:
            int: Résultat partiel du terme modulo MOD.
        """
        nonlocal cur, ok
        op = "*"    # Opérateur courant initialisé à multiplication
        res = 1     # Résultat accumulé pour les facteurs multipliés
        while cur < L:
            val = factor()  # Récupère un facteur (nombre ou expression entre parenthèses)
            if op == "*":
                res *= val
            else:  # op == "/"
                if val == 0:
                    ok = 0  # Division par zéro détectée
                # Multiplie par l'inverse de val modulo MOD (puissance modulaire)
                res *= pow(val, MOD-2, MOD)
            res %= MOD  # Réduction modulo MOD
            if S[cur] not in "*/":  # Si ce n'est plus un opérateur * ou /
                break
            op = S[cur]  # Mémorise l'opérateur pour la prochaine itération
            cur += 1     # Avance le curseur après l'opérateur
        return res

    def factor():
        """
        Analyse un facteur :
        - soit un nombre (suite de chiffres),
        - soit une expression entre parenthèses.
        
        Returns:
            int: Valeur évaluée du facteur modulo MOD.
        """
        nonlocal cur
        if S[cur] == '(':
            cur += 1  # Ignore la parenthèse ouvrante '('
            val = expr()  # Évalue l'expression à l'intérieur des parenthèses
            cur += 1  # Ignore la parenthèse fermante ')'
            return val
        return number()  # Sinon, récupère un nombre

    def number():
        """
        Analyse un nombre entier à partir de la position courante dans S.
        Ignore les espaces (déjà supprimés) et accumule les chiffres rencontrés.
        
        Returns:
            int: Nombre lu modulo MOD.
        """
        nonlocal cur
        val = 0
        while S[cur] in digits:
            val = (10 * val + int(S[cur])) % MOD  # Construction du nombre modulo MOD
            cur += 1  # Avance le curseur sur le chiffre lu
        return val

    res = expr()  # Lance l'analyse complète de l'expression
    return res if ok else -1  # Retourne le résultat ou -1 en cas d'erreur (division par zéro)


while True:
    S = input()  # Lecture d'une ligne d'entrée
    if S == '0:':  # Condition d'arrêt
        break
    p, S = S.split(":")   # Séparation du modulo p et de l'expression S
    p = int(p)            # Conversion de p en entier
    S = S.replace(" ", "") # Suppression des espaces dans l'expression
    res = calc(S, p)      # Calcul du résultat modulo p
    if res == -1:
        print("NG")       # Affichage NG si division par zéro détectée
    else:
        # Affiche l'expression originale et le résultat modulo p
        print("%s = %d (mod %d)" % (S, res, p))