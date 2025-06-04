import sys
import heapq

def main():
    # Lecture des paramètres M, N, K
    M, N, K = map(int, sys.stdin.readline().split())
    # Lecture des poids des boules w[i] (1-indexé)
    w = [0] + [int(sys.stdin.readline()) for _ in range(N)]
    # Lecture de la séquence d'accès aux boules a[j]
    a = [int(sys.stdin.readline()) for _ in range(K)]

    # Pour chaque boule, préparer la liste des indices de ses futures apparitions
    # pour permettre la stratégie de Namazu (Belady) basée sur l'apparition la plus lointaine
    positions = [[] for _ in range(N + 1)]
    for idx, ball in enumerate(a):
        positions[ball].append(idx)
    # Ajouter une valeur sentinelle (très grande) pour indiquer "pas d'apparition future"
    INF = 10**9
    for i in range(1, N + 1):
        positions[i].append(INF)

    # Pour chaque boule, on garde un curseur sur sa prochaine apparition future
    next_idx = [0] * (N + 1)

    # Ensemble représentant les boules présentes dans le cache (au plus M)
    # On stocke aussi leur prochaine apparition future pour les décisions
    cache = set()
    # Pour accéder rapidement à la boule avec la prochaine apparition la plus lointaine,
    # on stocke dans un heap des tuples (-next_appearance, ball) (négatif car on veut max heap)
    # Python ne dispose que d'un min heap, on inverse donc le signe des clés
    heap = []

    total_cost = 0

    for i in range(K):
        ball = a[i]

        # Avancer le curseur des prochaines apparitions pour cette boule
        next_idx[ball] += 1
        # La prochaine apparition future après la position i
        future = positions[ball][next_idx[ball]]

        if ball in cache:
            # Si la boule est déjà dans le cache, pas de coût
            # On met à jour la position dans le heap en rajoutant une nouvelle entrée pour la mise à jour
            # le heap contiendra quelques entrées obsolètes, mais on les ignore à la suppression
            heapq.heappush(heap, (-future, ball))
            continue

        # Si la boule n'est pas dans le cache, on doit la charger
        total_cost += w[ball]

        if len(cache) < M:
            # Cache pas plein, insérer directement
            cache.add(ball)
            heapq.heappush(heap, (-future, ball))
        else:
            # Cache plein, on doit expulser la boule dont la prochaine apparition est la plus lointaine
            # Il s'agit de la boule associée à la valeur maximale de prochaine apparition
            while True:
                # Récupérer la boule candidate à l'expulsion
                next_appearance_neg, candidate = heapq.heappop(heap)
                # Vérifier que ce candidat est encore dans le cache et que l'entrée est valide
                # Sinon, on continue à dépiler
                if candidate in cache:
                    break
            # Enlever candidate du cache
            cache.remove(candidate)
            # Ajouter la nouvelle boule
            cache.add(ball)
            heapq.heappush(heap, (-future, ball))

    print(total_cost)

if __name__ == "__main__":
    main()