# Bon, allons-y, voilà comment je ferais, c'est plus lisible, peut-être?
import collections

def main():
    # On récupère les valeurs de n et k de l'entrée standard
    try:
        n_k = input().split()
        n = int(n_k[0])
        k = int(n_k[1])
    except:
        print("Erreur lors de la lecture de n et k")
        return

    # Liste avec les valeurs de a
    a_raw = input().split()
    a = []
    for val in a_raw:
        try:
            a.append(int(val))
        except:
            a.append(0) # C'est peut-être pas terrible mais bon

    # Je vais calculer les paires strictement croissantes
    count = 0
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                count += 1
    # k fois parce que... c'est comme ça
    r = k * count

    # Compter les doublons dans a (pour enlever les paires égales)
    cnt = collections.Counter(a)
    s = 0
    for x in cnt.values():
        s += x * (x-1) // 2
    total_pairs = n * (n-1) // 2
    # Ajout de la partie combinatoire
    r += k*(k-1)//2 * (total_pairs - s)

    # Modulo, comme d'hab
    print(r % (10**9 + 7))

# Un peu old school mais ça marche
main()