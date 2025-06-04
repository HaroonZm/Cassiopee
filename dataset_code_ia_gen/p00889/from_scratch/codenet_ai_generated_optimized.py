import sys
input = sys.stdin.readline

def generate_sequence(N, S, W):
    a = [0]*N
    g = S
    for i in range(N):
        a[i] = (g // 7) % 10
        if g % 2 == 0:
            g = g // 2
        else:
            g = (g // 2) ^ W
    return a

def modexp(base, exp, mod):
    result = 1
    cur = base % mod
    while exp > 0:
        if exp & 1:
            result = (result * cur) % mod
        cur = (cur * cur) % mod
        exp >>= 1
    return result

while True:
    N,S,W,Q = map(int, input().split())
    if N==0 and S==0 and W==0 and Q==0:
        break
    a = generate_sequence(N,S,W)

    # On cherche à compter les sous-séquences valides dont la valeur est divisible par Q.
    # On considère les seuls i avec a[i]!=0 (pas de zéro initial).
    # On étudie le nombre de subarrays (i,j) tels que concat(a[i..j]) % Q == 0

    # Soit prefix_mod[k] = valeur a[0..k-1] mod Q
    prefix_mod = [0]*(N+1)
    for i in range(N):
        prefix_mod[i+1] = (prefix_mod[i]*10 + a[i]) % Q

    # On va utiliser un comptage par hashing des prefix_mod pour substring divisibles
    # Mais il faut prendre en compte les débuts valides (a[i] != 0)
    # Pour cela, on explore les indices j et utilise un dict qui stocke les prefix_mod aux indices où a[i]!=0
    # En fait, on traite les substrings qui commencent en i avec a[i]!=0
    # Les formule: substring a[i..j] mod Q = (prefix_mod[j+1]- prefix_mod[i]*pow(10,j-i+1)) mod Q = 0
    # donc prefix_mod[j+1] == prefix_mod[i]*10^{j-i+1} mod Q
    # On va inverser la relation pour compter efficacement avec préfixes et puissances.

    # Calcul des puissances de 10 modulo Q
    pow10 = [1]*(N+1)
    for i in range(1,N+1):
        pow10[i] = (pow10[i-1]*10) % Q

    # Approche: Pour chaque j, on va chercher i tel que a[i] != 0 et prefix_mod[j+1] == prefix_mod[i]*pow10[j-i+1]
    # On peut réarranger: prefix_mod[j+1] * pow10^{-(j-i+1)} == prefix_mod[i]
    # Le calcul de puissance inverse modulo Q est possible car Q premier

    # Pré-calcul de l'inverse de 10 modulo Q
    inv10 = pow(10, Q-2, Q)

    # On parcourt j de 0 à N-1, et on calcule key = prefix_mod[j+1]*inv10^{j+1} mod Q
    # On enregistre pour les indices i avec a[i]!=0, la valeur prefix_mod[i]*inv10^{i} dans un dict freq
    # Pour chaque j, on récupère freq[key] pour compter les sous-séquences terminant à j

    freq = dict()
    answer = 0
    for i in range(N+1):
        if i > 0 and a[i-1] == 0:
            # On ne stocke pas les positions i où a[i]!=0 car ici on indexe prefix_mod[i], avec i=indice fin de prefix
            # i correspond à la position après a[i-1]
            pass
        else:
            key = (prefix_mod[i] * pow(inv10, i, Q)) % Q
            freq[key] = freq.get(key,0) + 1

    # Maintenant on va parcourir j de 0 à N-1 et compter les sous séquences finissant en j
    # Pour cela, on utilise freq aux indices précédents : freq_stocke prefix_mod[i]*inv10^i avec a[i]!=0
    # Cette méthode nécessite une 2e boucle avec actualisation progressive
    freq.clear()
    answer = 0
    # On incrémente le compteur freq à chaque i où a[i]!=0 (i dans 0..N)
    # On parcourt j dans 0..N-1
    # Avant de traiter j, on ajoute prefix_mod[j]*inv10^j si a[j]!=0
    # Ensuite on calcule key = prefix_mod[j+1]*inv10^{j+1} et ajoute freq[key] au compteur
    for i in range(N+1):
        if i > 0 and a[i-1] == 0:
            key = (prefix_mod[i]*pow(inv10,i,Q))%Q
            answer += freq.get(key,0)
        else:
            key = (prefix_mod[i]*pow(inv10,i,Q))%Q
            freq[key] = freq.get(key,0)+1
            if i < N:
                key_next = (prefix_mod[i+1]*pow(inv10,i+1,Q))%Q
                answer += freq.get(key_next,0)
    print(answer)