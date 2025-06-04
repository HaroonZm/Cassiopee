from collections import deque
import itertools as itertools_module
import sys

# Augmenter la limite de récursion pour éviter les débordements lors de l'évaluation d'expressions complexes
sys.setrecursionlimit(1000000)

# Dictionnaire pour les atomes d'un seul caractère
single_character_atoms = {}

# Dictionnaire pour les atomes de plusieurs caractères
multi_character_atoms = {}

def is_digit(character):
    """Vérifie si le caractère passé est un chiffre."""
    return ord('0') <= ord(character) <= ord('9')

# Lecture et traitement de la première partie : associations atomes -> valeurs
while True:
    input_line = raw_input()

    if input_line == 'END_OF_FIRST_PART':
        break

    atom_symbol, atom_value = input_line.split()

    if len(atom_symbol) >= 2:
        multi_character_atoms[atom_symbol] = atom_value
    else:
        single_character_atoms[atom_symbol] = atom_value

# Lecture et traitement de la seconde partie : calcul des expressions
while True:
    expression_input = raw_input()

    if expression_input == '0':
        break

    transformed_expression = ''

    for index in range(len(expression_input) - 1):
        current_char = expression_input[index]
        next_char = expression_input[index + 1]

        transformed_expression += current_char

        if not is_digit(current_char) and is_digit(next_char):
            transformed_expression += '*'

        if is_digit(current_char) and not is_digit(next_char):
            transformed_expression += '+'

    transformed_expression += expression_input[-1]

    full_expression = '(' + transformed_expression + ')'

    # Remplacer les atomes complexes par leur valeur suivie de '+'
    for atom_symbol in multi_character_atoms:
        full_expression = full_expression.replace(atom_symbol, multi_character_atoms[atom_symbol] + '+')

    # Remplacer les atomes simples par leur valeur suivie de '+'
    for atom_symbol in single_character_atoms:
        full_expression = full_expression.replace(atom_symbol, single_character_atoms[atom_symbol] + '+')

    # Correction syntaxique pour les expressions arithmétiques
    full_expression = full_expression.replace('+*', '*')
    full_expression = full_expression.replace('+)', ')')

    try:
        evaluation_result = eval(full_expression)
    except:
        evaluation_result = "UNKNOWN"

    print evaluation_result