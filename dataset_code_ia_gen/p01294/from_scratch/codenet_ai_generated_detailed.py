# Solution complète pour le problème "For the Peace"
# Cette solution vérifie si les pays peuvent disposer leurs missiles dans l'ordre inverse de la liste donnée
# tout en maintenant la différence de potentiel (somme des capacités des missiles restants) entre le maximum
# et le minimum inférieure ou égale à d à chaque étape.

def main():
    import sys

    for line in sys.stdin:
        # Lecture de n (nombre de pays) et d (différence tolérée)
        n_d = line.strip()
        if not n_d:
            continue
        n, d = map(int, n_d.split())
        if n == 0 and d == 0:
            break  # Fin de la saisie

        countries = []
        total_missiles = 0
        # Lecture des données pour chaque pays
        for _ in range(n):
            data = sys.stdin.readline().strip().split()
            m = int(data[0])
            missiles = list(map(int, data[1:] ))
            # On stocke la liste dans l'ordre donné (du plus récent au plus ancien),
            # mais comme la destruction se fait du plus ancien au plus récent, on
            # inversera cette liste lors de traitement, ou on travaille directement en ordre inverse.
            # Pour simplification, on inverse la liste ici pour avoir la destruction dans l'ordre d'accès
            missiles.reverse()
            countries.append(missiles)
            total_missiles += m

        # Initialisation des potentiels : somme totale des missiles pour chaque pays
        potentials = [sum(c) for c in countries]

        # On itère le nombre maximal de missiles à détruire (maximum des mi)
        # Dans chaque étape, chaque pays est censé détruire un missile (si possible),
        # dans l'ordre du plus ancien (car la liste est inversée on prend en premier)
        # Après chaque étape, on vérifie la différence max-min des potentiels
        # Si elle > d, on imprime "No", sinon "Yes" si toutes les étapes passent.

        # On va détruire missile par missile pour chaque pays dans l'ordre inverse de production

        # La condition nous dit que la différence max-min ne dépasse pas d à aucun moment,
        # on vérifie donc à chaque étape.

        # Il faut gérer que certains pays ont moins de missiles que d'autres.
        # Le processus s'arrête quand tous les missiles sont détruits.

        # Pour simuler la destruction missile par missile dans l'ordre le plus ancien vers plus récent,
        # on détruit la première (index 0) valeur de la liste missiles[i] si possible.

        # Algorithme:
        # à chaque étape:
        #   pour chaque pays:
        #       si missiles restants:
        #           retirer le missile le plus ancien (le premier)
        #           diminuer le potentiel en conséquence
        #   calculer max et min de potentials
        #   si diff > d => print No et passer au dataset suivant

        max_missiles = max(len(c) for c in countries)
        possible = True

        for step in range(max_missiles):
            for i in range(n):
                if len(countries[i]) > 0:
                    missile_to_destroy = countries[i].pop(0)  # plus ancien missile
                    potentials[i] -= missile_to_destroy
            if max(potentials) - min(potentials) > d:
                possible = False
                break

        print("Yes" if possible else "No")

if __name__ == "__main__":
    main()