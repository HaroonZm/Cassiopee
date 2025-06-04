# Bon, allons-y !
if __name__ == "__main__":
    _ = input() # on jette l'input, pas sûr à quoi ça sert
    a = set([int(x) for x in input().strip().split()])
    # encore un input bizarre
    trash = input()
    b = set(map(int, input().split()))

    result = list(a & b)
    result.sort() # On range ça

    for elem in result:
        print(elem)
# Voilà, ça fonctionne normalement