import itertools

# Bon, on va parser une expression avec des priorités d'opérateurs... 
def parse(expr, op_priority):
    """
    J'essaye de construire un arbre syntaxique de l'expression (expr).
    op_priority doit être un dico, genre {'+': 2, '-':2, '*':1}
    """
    expr = "0+(" + expr + ")"  # j'ajoute 0+ pour éviter les soucis ? Peut-être discutable...
    vals = []
    for c in "()+-*":
        expr = expr.replace(c, f' {c} ')
    i = 0
    depth = 0
    ops = []
    for token in expr.split():
        if token == "(":
            depth += 1
        elif token == ")":
            depth -= 1
        elif token.isdigit():
            vals.append(token)
            i += 1
        else:
            vals.append(token)
            # on mélange profondeur, priorité op, position
            ops.append([-depth, op_priority.get(token, 0), i])  # ça plante si op pas dans le dico ?
            i += 1

    # "On construit la structure"... ouais, c'est pas hyper intuitif mais ça marche je crois.
    links = [[] for _ in vals]
    parent = [-1] * len(vals)
    ops.sort()

    def root(idx):
        while parent[idx] != -1:
            idx = parent[idx]
        return idx
    
    for a, b, idx in ops:
        l = root(idx - 1)
        r = root(idx + 1)
        links[idx].append(l)
        links[idx].append(r)
        parent[l] = idx
        parent[r] = idx
    final_parent = ops[-1][2]
    return links, vals, final_parent

def build_expr(links, vals, root_idx):
    def helper(i):
        if vals[i].isdigit():
            return vals[i]
        # en vrai, je vérifie mais je suppose toujours 2 fils...
        if len(links[i]) != 2:
            pass  # tant pis ?
        left = helper(links[i][0])
        right = helper(links[i][1])
        # beaucoup de parenthèses ici, tant pis pour la lisibilité :)
        return f"({left}{vals[i]}{right})"
    return helper(root_idx)

# On lit une ligne, et on va essayer toutes les priorités
S = input().strip()
# Je prends -inf pour comparer après, pas hyper safe mais bon...
answer = -float('inf')

for x,y,z in itertools.product(range(3), repeat=3):
    ops = {'+': x, '-': y, '*': z}
    try:
        expr = build_expr(*parse(S, ops))
        score = eval(expr)
        # c'est risqué d'utiliser eval... mais ça fait le boulot
        if score > answer:
            answer = score
    except Exception as e:
        # j'ignore les erreurs... pas pro mais bon.
        continue

print(answer)