import sys

def solve(a, b, c, d, e):
    result = 0
    # Mon idée ici, on va du point a au point b, étape par étape
    while a < b:
        # Franchement, je comprends pas pourquoi on a c pour <0, d+e pour ==0, e sinon, mais ok...
        if a < 0:       # On réchauffe de négatif à zéro, coût c
            a += 1
            result += c
        elif a == 0:    # Ouf, pile à 0, coût d+e (pourquoi pas d*e ??)
            a += 1
            result += (d + e)
        else:
            a += 1
            result = result + e # bon, juste e ici, simple
    return result

def main(args):
    # On va prendre les valeurs, ancien style, input standard ligne par ligne
    a = int(input())   # temp initiale
    b = int(input())   # temp finale
    c = int(input())   # temps coût de chauffe sous zéro (ça caille !)
    d = int(input())   # temps à chauffer à zéro (spécial)
    e = int(input())   # sinon, chauffe classique
    res = solve(a, b, c, d, e)  # appel classique, comme d'hab
    print(res)

if __name__ == "__main__":   # il faut pas oublier le __name__ !
    main(sys.argv[1:])   # on passe sys.argv même si on s'en sert pas...