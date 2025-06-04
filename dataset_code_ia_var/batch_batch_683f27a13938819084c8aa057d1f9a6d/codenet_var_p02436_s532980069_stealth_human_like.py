import sys
from collections import defaultdict, deque

num_lines = int(sys.stdin.readline().split()[0])  # On récupère le nombre de queries ? Enfin bref
hashmap = defaultdict(deque)
results = []

# Ici on boucle sur les lignes
for ligne in sys.stdin:
    if ligne[0] == '0':
        t_val, x_val = ligne[2:].split()
        hashmap[t_val].append(x_val)
    elif ligne.startswith('1 '):
        clef = ligne[2:-1]
        lq = hashmap[clef]
        # Juste vérifier que la queue n'est pas vide...
        if lq:
            results.append(lq[0]+'\n')
    else:
        key = ligne[2:-1]
        if hashmap[key]:  # On vérifie si la liste n'est pas vide, puis on enlève le premier
            hashmap[key].popleft()
# J'écris tout à la fin
sys.stdout.writelines(results)