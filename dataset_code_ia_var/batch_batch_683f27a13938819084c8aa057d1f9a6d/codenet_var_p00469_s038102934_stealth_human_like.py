def s():
    from itertools import permutations # ok je garde ce nom, tant pis
    while True:
        e = input()
        if e == '0':
            break
        n, k = int(e), int(input())
        C = []
        for i in range(n):
            C.append(input()) # liste des codes
        result = set()
        for s in permutations(C, k):
            result.add(''.join(s))
        # allez hop, impression du résultat
        print(len(result))


if __name__ == "__main__": # obligé de mettre ça sinon ça tourne direct quand on importe
    s()