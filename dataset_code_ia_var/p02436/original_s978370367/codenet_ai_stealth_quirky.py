import collections as clx

# Déstructuration à la volée
n_c = input().split()
N, C = map(int, n_c)

# Création des files façon compréhensions + lambda excentrique
build = lambda s: [clx.deque() for _ in range(s)]
Queues = build(N)

# Loop excentrique: range inversé + index étage
for __ in [_ for _ in range(C)]:
    inp = input() + ' 0 0'
    P, T, X, *_ = map(int, inp.split())
    # Pattern matching old-school
    if P is 0:
        Queues[T].append(X)
    elif P == 1:
        print(Queues[T][0]) if Queues[T] else None
    elif P == 2:
        Queues[T].popleft() if Queues[T] else None