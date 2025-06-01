from typing import List, Optional, Tuple, Iterator
import sys
import bisect

class MonsterCollection:
    """
    Une collection abstraite de monstres avec des niveaux,
    permettant diverses opérations utiles pour la stratégie.
    """
    def __init__(self, levels: List[int]):
        self.levels = sorted(levels)

    def __len__(self) -> int:
        return len(self.levels)

    def get_levels(self) -> List[int]:
        return self.levels

    def count_strictly_greater_than(self, x: int) -> int:
        # Nombre d'éléments strictement plus grands que x
        idx = bisect.bisect_right(self.levels, x)
        return len(self.levels) - idx

    def can_win_at_least(self, k: int, opponent: 'MonsterCollection') -> bool:
        """
        Vérifie si on peut choisir k monstres de self et k monstres de opponent
        de façon à gagner strictement plus de k//2 combats,

        quel que soit le choix de l'adversaire.
        """
        # Pour que l'on gagne plus de la moitié,
        # on doit pouvoir associer au moins (k//2 + 1) de nos monstres
        # avec des monstres adverses plus faibles (strictement inférieurs).

        # Stratégie :
        # On sélectionne nos k meilleurs monstres (les plus forts),
        # On considère les k monstres adverses les plus faibles (le pire cas adversaire),
        # Si on peut assigner à au moins (k//2 + 1) de nos monstres un adversaire plus faible,
        # alors on peut gagner peu importe la sélection adverse.

        # Étant donné que l'adversaire choisit les monstres,
        # le pire cas est qu'il choisisse les k monstres qui minimisent nos victoires.
        # Donc on doit vérifier que quel que soit l'ordre
        # d'association, on peut remporter au moins (k//2 + 1) duels.

        # Implémentation :
        # - on sélectionne nos k plus forts monstres (self_levels[-k:])
        # - on essaie de trouver pour au moins (k//2 + 1) d'entre eux un monstre adverse plus faible
        # - on teste cela par un algorithme glouton.

        ours = self.levels[-k:]
        theirs = opponent.levels  # adversaire peut choisir n'importe quel sous-ensemble

        # On doit vérifier que, pour tout choix possible de l'adversaire,
        # on gagne. On doit considérer le pire sous-ensemble adverse
        # (celui qui nous fait perdre le plus).

        # Une solution provient d'une méthode double pointeurs sur les deux tableaux triés.
        # Mais ici, l'adversaire choisit un sous-ensemble de taille k.
        # Donc le pire cas pour nous est que l'adversaire choisisse les k monstres
        # les plus forts (car du coup il réduira nos victoires).

        # Mais l'énoncé interdit k = N, donc on sera toujours en subset strict.

        # Cependant, la solution connue pour ce problème est :

        # On veut maximiser le nombre de paires  (a_i > b_j)
        # possibles pour k monstres chacun.

        # Implémentation précise :
        # - on parcourt nos k monstres du plus faible au plus fort
        # - on essaye de leur associer le monstre adverse minimal possible qui est strictement plus faible
        # - si on atteint au moins (k//2 + 1) paires gagnantes, c'est gagné

        # On va tenter de trouver l'adversaire le plus fort possible, minimisant
        # notre nombre de victoires :
        # Il choisit ses k monstres les plus forts : opponent.levels[-k:]

        adversary_subset = opponent.levels[-k:]

        # Pointeurs pour nos monstres (depuis le plus petit) et adversaires (idem)
        i = 0  # indice chez nous
        j = 0  # indice chez adversaire
        wins = 0
        while i < k and j < k:
            if ours[i] > adversary_subset[j]:
                wins += 1
                i += 1
                j += 1
            else:
                i += 1
        return wins > k // 2


class Tournament:
    """
    Gestion complète du tournoi selon la règle donnée, avec la méthode principale
    pour déterminer la plus petite taille de combat k gagnant garantie.
    """

    def __init__(self, own_levels: List[int], opponent_levels: List[int]):
        self.own = MonsterCollection(own_levels)
        self.opp = MonsterCollection(opponent_levels)
        self.N = len(own_levels)

    def minimal_winning_k(self) -> Optional[int]:
        """
        Recherche binaire sur k de 1 à N-1 pour trouver
        le plus petit k tel que self peut garantir la victoire.
        Sinon None.
        """
        left = 1
        right = self.N - 1
        result = None
        while left <= right:
            mid = (left + right) // 2
            if self.own.can_win_at_least(mid, self.opp):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        if result is None or result == self.N:
            return None
        return result


def parse_input() -> Iterator[Tuple[int, List[int], List[int]]]:
    """
    Générateur pour lire les entrées dans le format indiqué,
    renvoyant les triplets (N, own_levels, opponent_levels)
    jusqu'à la ligne 0.
    """
    input_iter = iter(sys.stdin.read().strip().split('\n'))
    while True:
        try:
            line = next(input_iter)
            if line == '0':
                break
            N = int(line)
            own_levels = list(map(int, next(input_iter).split()))
            opponent_levels = list(map(int, next(input_iter).split()))
            yield (N, own_levels, opponent_levels)
        except StopIteration:
            break


def main() -> None:
    for N, own_levels, opponent_levels in parse_input():
        tournament = Tournament(own_levels, opponent_levels)
        k = tournament.minimal_winning_k()
        if k is None:
            print("NA")
        else:
            print(k)

if __name__ == "__main__":
    main()