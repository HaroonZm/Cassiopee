import math
import string
import sys

# Augmenter la limite de récursion pour éviter les erreurs dans les appels récursifs profonds
sys.setrecursionlimit(10**7)

INFINITY_LARGE_NUMBER = 10**20
FLOATING_POINT_EPSILON = 1.0 / 10**10
MODULAR_BASE = 10**9 + 7

# Déplacements pour les grilles (haut, droite, bas, gauche)
FOUR_DIRECTION_VECTORS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
EIGHT_DIRECTION_VECTORS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_integers_from_input_line():
    return [int(value) for value in sys.stdin.readline().split()]

def read_integers_from_input_line_zero_indexed():
    return [int(value) - 1 for value in sys.stdin.readline().split()]

def read_floats_from_input_line():
    return [float(value) for value in sys.stdin.readline().split()]

def read_strings_from_input_line():
    return sys.stdin.readline().split()

def read_single_integer():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_single_string():
    return input()

def print_and_flush(output_value):
    print(output_value, flush=True)

def _do_line_segments_intersect_first_stage(point_a1, point_a2, point_b1, point_b2):
    a1_x, a1_y, _ = point_a1
    a2_x, a2_y, _ = point_a2
    b1_x, b1_y, _ = point_b1
    b2_x, b2_y, _ = point_b2

    temp_calculation_1 = (a1_x - a2_x) * (b1_y - a1_y) + (a1_y - a2_y) * (a1_x - b1_x)
    temp_calculation_2 = (a1_x - a2_x) * (b2_y - a1_y) + (a1_y - a2_y) * (a1_x - b2_x)
    return temp_calculation_1 * temp_calculation_2 < 0

def do_line_segments_properly_intersect(point_a1, point_a2, point_b1, point_b2):
    return (_do_line_segments_intersect_first_stage(point_a1, point_a2, point_b1, point_b2)
            and _do_line_segments_intersect_first_stage(point_b1, point_b2, point_a1, point_a2))

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def compute_point_to_segment_distance(point_start, point_end, point_target):
    start_x, start_y, _ = point_start
    end_x, end_y, _ = point_end
    target_x, target_y, _ = point_target

    segment_vector_x = end_x - start_x
    segment_vector_y = end_y - start_y
    target_vector_x = target_x - start_x
    target_vector_y = target_y - start_y

    projection_parameter = ((segment_vector_x * target_vector_x + segment_vector_y * target_vector_y) /
                           (segment_vector_x ** 2 + segment_vector_y ** 2))

    if projection_parameter <= 0:
        return compute_euclidean_distance(start_x, start_y, target_x, target_y)
    if projection_parameter >= 1:
        return compute_euclidean_distance(end_x, end_y, target_x, target_y)
    projected_x = start_x + projection_parameter * segment_vector_x
    projected_y = start_y + projection_parameter * segment_vector_y
    return compute_euclidean_distance(projected_x, projected_y, target_x, target_y)

def main():
    result_lines = []

    symbol_value_dictionary = {}

    # Lire la première séquence de paires clé/valeur jusqu'à un séparateur spécifique
    while True:
        input_line = read_single_string()
        if input_line == 'END_OF_FIRST_PART':
            break
        symbol, value_string = input_line.split()
        symbol_value_dictionary[symbol] = int(value_string)

    def evaluate_expression(expression_string):
        parsed_tokens = []
        for character in expression_string:
            if "0" <= character <= "9":
                if len(parsed_tokens) > 0 and isinstance(parsed_tokens[-1], int):
                    parsed_tokens[-1] *= 10
                    parsed_tokens[-1] += int(character)
                else:
                    parsed_tokens.append(int(character))
            elif character in string.ascii_lowercase:
                if len(parsed_tokens) < 1 or isinstance(parsed_tokens[-1], int):
                    return 'UNKNOWN'
                parsed_tokens[-1] = str(parsed_tokens[-1]) + character
            else:
                parsed_tokens.append(character)

        for token in parsed_tokens:
            if isinstance(token, int) or token == '(' or token == ')':
                continue
            if token not in symbol_value_dictionary:
                return 'UNKNOWN'

        def recursively_evaluate(parsed_token_list):
            if '(' in parsed_token_list:
                open_parenthesis_index = parsed_token_list.index('(')
                parenthesis_level_counter = 1
                for token_index in range(open_parenthesis_index + 1, len(parsed_token_list)):
                    if parsed_token_list[token_index] == '(':
                        parenthesis_level_counter += 1
                    elif parsed_token_list[token_index] == ')':
                        parenthesis_level_counter -= 1
                        if parenthesis_level_counter == 0:
                            inner_value = recursively_evaluate(parsed_token_list[open_parenthesis_index + 1: token_index])
                            if len(parsed_token_list) > token_index + 1 and isinstance(parsed_token_list[token_index + 1], int):
                                inner_value *= parsed_token_list[token_index + 1]
                                return recursively_evaluate(parsed_token_list[:open_parenthesis_index] + [-inner_value] + parsed_token_list[token_index + 2:])
                            return recursively_evaluate(parsed_token_list[:open_parenthesis_index] + [-inner_value] + parsed_token_list[token_index + 1:])
                return None
            accumulated_result = 0
            index = 0
            while index < len(parsed_token_list):
                token = parsed_token_list[index]
                if isinstance(token, int):
                    accumulated_result += abs(token)
                    index += 1
                    continue
                if index + 1 < len(parsed_token_list) and isinstance(parsed_token_list[index + 1], int) and parsed_token_list[index + 1] >= 0:
                    accumulated_result += (symbol_value_dictionary[token] - 1) * parsed_token_list[index + 1]
                    index += 2
                else:
                    accumulated_result += symbol_value_dictionary[token]
                    index += 1
            return accumulated_result

        return recursively_evaluate(parsed_tokens)

    # Lire les lignes suivantes, traiter les expressions, s'arrêter à '0'
    while True:
        input_expression_line = read_single_string()
        if input_expression_line == '0':
            break
        evaluation_result = evaluate_expression(input_expression_line)
        result_lines.append(evaluation_result)

    return '\n'.join(map(str, result_lines))

print(main())