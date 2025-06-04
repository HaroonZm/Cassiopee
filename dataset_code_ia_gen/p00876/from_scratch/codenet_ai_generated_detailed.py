# Solution complète pour le problème Swimming Jam

def swimming_jam():
    while True:
        n = int(input())
        if n == 0:
            break

        swimmers = []
        for _ in range(n):
            t, c = map(int, input().split())
            swimmers.append({'t': t, 'c': c})

        # Initial ordering: faster swimmers in front (smaller t in front)
        swimmers.sort(key=lambda x: x['t'])

        time = 0
        # On simule chaque segment de nage (aller ou retour), les nageurs sont toujours sur un des deux couloirs
        # Ils changent de couloir à chaque extrémité
        # Pour chaque segment demandé par tous les nageurs (2 * ci segments chacun), on calcule la durée du segment
        # en fonction des vitesses bloquantes

        # Comme tous démarrent au même bout, dans l'ordre des vitesses croissantes
        # On traite chaque segment d'un bout à l'autre, puis on trie par vitesse à la fin pour que les plus rapides
        # soient devant au début du segment suivant

        # Le nombre total de segments à nager est le maximum de (2 * ci)
        max_segments = max(sw['c'] * 2 for sw in swimmers)

        # On crée une liste de positions relative des nageurs (ordre dans la file),
        # initialement triée par leur temps naturel (vitesse)
        order = swimmers[:]  # copie pour manipulation

        for segment in range(max_segments):
            # Filtrage des nageurs encore en train de nager
            active_swimmers = [sw for sw in order if sw['c'] * 2 > segment]

            if not active_swimmers:
                break

            # Le temps de ce segment est donné par le nageur le plus lent,
            # car pas de dépassement autorisé => le dernier impose la vitesse
            # Mais en fait c'est la vitesse du nageur en tête bloquée par le plus lent devant
            # Entraînement en file = temps égal à la plus grande valeur t d'un nageur actif.

            # Dans la file, la vitesse effective du groupe est la plus lente parmi eux,
            # car personellements ils doivent suivre le plus lent si il y a blocage.

            # Mais la vitesse est la vitesse de "blocage" progressive : un nageur peut être bloqué
            # par un nageur plus lent devant, ou par un lièvre encore plus lent devant...

            # Vu l'énoncé, on considère que les nageurs sont dans l'ordre 'order'
            # donc le nageur en position i peut être bloqué par le nageur i-1
            # s'il est plus lent.

            # En pratique, la vitesse du groupe est la vitesse du nageur le plus lent dans la file
            # mais plus précisément le temps d'aller d'un bout à l'autre est le temps du nageur bloquant le plus lent.

            # Dans le sens du déplacement (ordre), on propage les temps effectifs.

            # On calcule la vitesse effective des nageurs en tenant compte des blocages en amont.
            effective_times = [0] * len(active_swimmers)
            effective_times[0] = active_swimmers[0]['t']
            for i in range(1, len(active_swimmers)):
                # un nageur ne peut pas aller plus vite que celui devant lui
                effective_times[i] = max(effective_times[i-1], active_swimmers[i]['t'])

            # La durée du segment est le temps du nageur le plus lent calculé (dernier nageur de la file)
            segment_time = effective_times[-1]
            time += segment_time

            # Arrivé à la fin de ce segment,
            # les nageurs peuvent réordonner leurs positions dans la file.
            # Selon l'énoncé, ceux arrivant simultanément changent d'ordre pour que les plus rapides soient en avant.

            # Les nageurs qui finissent simultanément sont ceux qui étaient ensemble dans ce segment.
            # Tous les nageurs concernés dans active_swimmers sont arrivés simultanément (le blocage)
            # On doit ensuite trier active_swimmers par vitesse ascendante (plus rapides devant)
            active_swimmers.sort(key=lambda x: x['t'])

            # On met à jour la liste order dans laquelle se trouvent tous les nageurs,
            # en remplaçant la partie active par la nouvelle ordre active_swimmers

            # Trouver les indices des active_swimmers dans order
            indices_active = [order.index(sw) for sw in active_swimmers]

            # Mettre à jour order avec l'ordre trié des active_swimmers
            for i, idx in enumerate(sorted(indices_active)):
                order[idx] = active_swimmers[i]

        print(time)


if __name__ == "__main__":
    swimming_jam()