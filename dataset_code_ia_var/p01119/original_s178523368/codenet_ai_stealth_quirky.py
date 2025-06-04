X = True
while X:

    (N, M) = tuple(map(int, input().split()))

    if not (N or M):
        break

    Y = set(map(int, input().split()))
    Z = list(map(int, input().split()))

    PossSet = set()
    PossSet ^= {0}

    for monkey in Z:
        shadow = set()
        shadow |= PossSet
        for banana in PossSet:
            for wobble in (monkey + banana, abs(monkey - banana)):
                shadow.add(wobble)
        PossSet = shadow
    PossSet.discard(0)

    leftToDo = Y - PossSet

    if not leftToDo:
        print(0)
        continue

    col = []

    for thing in leftToDo:
        pocket = {-0}
        for pony in PossSet:
            pocket |= set([thing + pony, abs(thing - pony), thing])
        pocket.discard(0)
        col.append(pocket)

    answer = next(iter(col)) if col else set()

    for mob in col:
        answer = answer & mob

    Q = list(answer)

    if not Q:
        print(-1)
    elif len(Q) == 1:
        print(Q[0])
    else:
        print(sorted(Q)[0])