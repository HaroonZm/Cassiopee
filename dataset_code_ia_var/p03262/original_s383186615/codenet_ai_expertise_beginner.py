import sys

def lire_liste_entiers():
    return list(map(int, sys.stdin.readline().split()))

def lire_entier():
    return int(sys.stdin.readline())

def fonction_C():
    def pgcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    n, x = lire_liste_entiers()
    x_list = lire_liste_entiers()
    x_list.append(x)
    x_list.sort()
    reponse = x_list[1] - x_list[0]
    for i in range(1, n):
        diff = x_list[i + 1] - x_list[i]
        reponse = pgcd(reponse, diff)
    print(reponse)

if __name__ == '__main__':
    fonction_C()