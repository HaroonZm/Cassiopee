import sys

# Augmenter la limite de récursion pour éviter les erreurs lors de grandes profondeurs d'appels récursifs
sys.setrecursionlimit(2147483647)

INFINITY_NUMBER = float("inf")
MODULO_FOR_COMPUTATIONS = 10 ** 9 + 7

# Lecture d'une ligne d'entrée standard, nettoyage des espaces superflus
custom_input = lambda: sys.stdin.readline().rstrip()

def main():
    number_of_steps, target_score = map(int, custom_input().split())

    # Dimensions : [étape][nombre de paires][score total]
    maximum_steps = 55
    maximum_pairs = 55
    maximum_score = 2700
    dp_table = [
        [
            [0 for _ in range(maximum_score)]
            for _ in range(maximum_pairs)
        ]
        for _ in range(maximum_steps)
    ]

    # État initial : 0 étape, 0 paire, score 0
    dp_table[0][0][0] = 1

    for current_step in range(number_of_steps):

        # Le nombre de paires ouvertes possibles varie de 0 à current_step inclus
        for number_of_open_pairs in range(current_step + 1):

            for accumulated_score in range(target_score + 1):

                current_ways = dp_table[current_step][number_of_open_pairs][accumulated_score]

                if current_ways == 0:
                    continue

                # 1. Réutiliser une paire déjà ouverte
                next_step = current_step + 1
                same_pairs = number_of_open_pairs
                score_increment = 2 * number_of_open_pairs
                new_score = accumulated_score + score_increment
                dp_table[next_step][same_pairs][new_score] += (2 * number_of_open_pairs + 1) * current_ways
                dp_table[next_step][same_pairs][new_score] %= MODULO_FOR_COMPUTATIONS

                # 2. Ouvrir une nouvelle paire
                more_pairs = number_of_open_pairs + 1
                new_score_for_opening = accumulated_score + 2 * more_pairs
                dp_table[next_step][more_pairs][new_score_for_opening] += current_ways
                dp_table[next_step][more_pairs][new_score_for_opening] %= MODULO_FOR_COMPUTATIONS

                # 3. Fermer une paire si possible
                if number_of_open_pairs > 0:
                    less_pairs = number_of_open_pairs - 1
                    new_score_for_closing = accumulated_score + 2 * less_pairs
                    dp_table[next_step][less_pairs][new_score_for_closing] += (number_of_open_pairs ** 2) * current_ways
                    dp_table[next_step][less_pairs][new_score_for_closing] %= MODULO_FOR_COMPUTATIONS

    print(dp_table[number_of_steps][0][target_score])

main()