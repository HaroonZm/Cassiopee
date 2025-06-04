import sys
input = sys.stdin.readline

def medical_checkup():
    # Lecture des données d'entrée
    n, t = map(int, input().split())
    h = [int(input()) for _ in range(n)]

    # L'idée est de déterminer, pour chaque étudiant,
    # à quel item de checkup il est arrivé à l'instant t+0.5.

    # Chaque étudiant i passe les items dans l'ordre : 1, 2, 3, ...
    # Chaque item prend h[i] minutes pour lui
    # Donc le temps total pour terminer k items pour l'étudiant i est  k * h[i]

    # Tous les items sont réalisés séquentiellement par item,
    # c'est-à-dire que l'ordre des étudiants ne change pas,
    # mais les items sont "alignés" comme dans une chaîne de montage.

    # On peut voir cela comme un système où chaque étudiant passe la même séquence d'items,
    # mais le temps total pour finir k items pour un étudiant i est
    # k * h_i + temps d'attente dû au passage des étudiants précédents.

    # Le temps pour que le i-ème étudiant ait fini k items est :
    # sum_{j=1}^{i-1} (k * h_j) + k * h_i == k * (sum_{j=1}^i h_j)
    # donc le "pipeline" global avance à la vitesse cum_h = sum h_j (j=1..i)

    # Le problème se ramène à, pour chaque i,
    # trouver k tel que :
    # temps jusqu'à la fin du k-ième item pour l'étudiant i > t
    # mais pour (k-1)-ème item <= t

    # La fin du k-ième item pour l'étudiant i arrive à :
    # k * (sum_{j=1}^i h_j)

    # Nous cherchons donc k tel que :
    # k * prefix_sum[i] > t
    # k = ceil(t / prefix_sum[i])

    # L'item que l'étudiant i fait ou attend au temps t+0.5
    # est donc k = (t // prefix_sum[i]) + 1

    # Calcul des préfixes
    prefix_sum = [0] * n
    prefix_sum[0] = h[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + h[i]

    # Calcul des items en cours
    # On fait un entier divisé par prefix_sum[i], on ajoute 1 à la division entière
    for i in range(n):
        item = t // prefix_sum[i] + 1
        print(item)

if __name__ == "__main__":
    medical_checkup()