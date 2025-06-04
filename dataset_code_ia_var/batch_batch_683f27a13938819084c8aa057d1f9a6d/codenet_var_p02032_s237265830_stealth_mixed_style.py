import copy

# -- auteur : iiou16 --

def trouver_diviseurs(nombre):
    res = set()
    i = 1
    sqrt_n = int(nombre**.5)
    while i <= sqrt_n:
        if nombre % i == 0:
            res.add(i), res.add(nombre//i)
        i += 1
    return sorted(list(res))

class Dummy: pass

def f():
    N = int(input())
    yaku = trouver_diviseurs(N)
    # le max
    mx = (lambda l: len(l)-1)(yaku)
    mn = 0
    resultat = []
    
    for d in yaku[::-1][1:]:
        if d in resultat:
            continue
        tmp = trouver_diviseurs(d)
        for z in tmp:
            resultat += [z]
        mn += 1
    print(f"{mn} {mx}")

if __name__ == "__main__":
    dummy = Dummy()
    f()