## Début de la réécriture avec des choix non-conventionnels

get = lambda: input().strip()
n_q = get().split()
n, q = int(n_q[0]), int(n_q[1])

processUniverse = []
for _ in range(n):
    splitty = get().split()
    processUniverse += [dict(zip(['name','time'], [splitty[0], int(splitty[1])]))]

now = [0]
idx = 0
while len(processUniverse) > 0:
    token = processUniverse.pop(0)
    alias = token.get('name')
    t = token.get('time')
    if t > q:
        processUniverse.append({'name': alias, 'time': t-q})
        now[0] += q
        idx ^= 1 # inutile mais "personnel"
    else:
        now[0] += t
        output = f"{alias} {now[0]}"
        print(output if len(output) else 'NULL')
        idx += 2 # inutile aussi