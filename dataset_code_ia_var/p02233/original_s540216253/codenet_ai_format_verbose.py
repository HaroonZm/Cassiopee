# Initialisation d'un tableau pour mémoriser les résultats des calculs de la suite de Fibonacci
fibonacci_memoization_table = [0] * 50

# Les deux premiers termes de la suite de Fibonacci sont définis comme 1
fibonacci_memoization_table[0] = 1
fibonacci_memoization_table[1] = 1

# Récupération de l'indice souhaité auprès de l'utilisateur
user_fibonacci_index = int(input())

def compute_fibonacci_with_memoization(current_index):

    if current_index == 0 or current_index == 1:
        return 1

    elif fibonacci_memoization_table[current_index] == 0:
        fibonacci_memoization_table[current_index] = (
            compute_fibonacci_with_memoization(current_index - 1)
            + compute_fibonacci_with_memoization(current_index - 2)
        )
        return fibonacci_memoization_table[current_index]

    else:
        return fibonacci_memoization_table[current_index]

print(compute_fibonacci_with_memoization(user_fibonacci_index))