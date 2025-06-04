from functools import reduce

input_ball_count = int(input())
input_ball_sequence = input()

modulo_prime = 998244353

class ModuloInteger:
    def __init__(self, value):
        self.value = value % modulo_prime

    def __str__(self):
        return str(self.value)

    __repr__ = __str__

    def __add__(self, operand):
        if isinstance(operand, ModuloInteger):
            return ModuloInteger(self.value + operand.value)
        else:
            return ModuloInteger(self.value + operand)

    def __sub__(self, operand):
        if isinstance(operand, ModuloInteger):
            return ModuloInteger(self.value - operand.value)
        else:
            return ModuloInteger(self.value - operand)

    def __mul__(self, operand):
        if isinstance(operand, ModuloInteger):
            return ModuloInteger(self.value * operand.value)
        else:
            return ModuloInteger(self.value * operand)

    def __truediv__(self, operand):
        if isinstance(operand, ModuloInteger):
            return ModuloInteger(self.value * pow(operand.value, modulo_prime - 2, modulo_prime))
        else:
            return ModuloInteger(self.value * pow(operand, modulo_prime - 2, modulo_prime))

    def __pow__(self, operand):
        if isinstance(operand, ModuloInteger):
            return ModuloInteger(pow(self.value, operand.value, modulo_prime))
        else:
            return ModuloInteger(pow(self.value, operand, modulo_prime))

    def __radd__(self, operand):
        return ModuloInteger(operand + self.value)

    def __rsub__(self, operand):
        return ModuloInteger(operand - self.value)

    def __rmul__(self, operand):
        return ModuloInteger(operand * self.value)

    def __rtruediv__(self, operand):
        return ModuloInteger(operand * pow(self.value, modulo_prime - 2, modulo_prime))

    def __rpow__(self, operand):
        return ModuloInteger(pow(operand, self.value, modulo_prime))

def update_state(ball_type, accumulator_result, free_person, red_person, green_person, blue_person, red_green_pair, green_blue_pair, blue_red_pair):
    if ball_type == 'R':
        if green_blue_pair:
            return (accumulator_result * green_blue_pair, free_person, red_person, green_person, blue_person, red_green_pair, green_blue_pair - 1, blue_red_pair)
        elif green_person:
            return (accumulator_result * green_person, free_person, red_person, green_person - 1, blue_person, red_green_pair + 1, green_blue_pair, blue_red_pair)
        elif blue_person:
            return (accumulator_result * blue_person, free_person, red_person, green_person, blue_person - 1, red_green_pair, green_blue_pair, blue_red_pair + 1)
        else:
            return (accumulator_result * free_person, free_person - 1, red_person + 1, green_person, blue_person, red_green_pair, green_blue_pair, blue_red_pair)
    elif ball_type == 'G':
        if blue_red_pair:
            return (accumulator_result * blue_red_pair, free_person, red_person, green_person, blue_person, red_green_pair, green_blue_pair, blue_red_pair - 1)
        elif red_person:
            return (accumulator_result * red_person, free_person, red_person - 1, green_person, blue_person, red_green_pair + 1, green_blue_pair, blue_red_pair)
        elif blue_person:
            return (accumulator_result * blue_person, free_person, red_person, green_person, blue_person - 1, red_green_pair, green_blue_pair + 1, blue_red_pair)
        else:
            return (accumulator_result * free_person, free_person - 1, red_person, green_person + 1, blue_person, red_green_pair, green_blue_pair, blue_red_pair)
    else: # ball_type == 'B'
        if red_green_pair:
            return (accumulator_result * red_green_pair, free_person, red_person, green_person, blue_person, red_green_pair - 1, green_blue_pair, blue_red_pair)
        elif red_person:
            return (accumulator_result * red_person, free_person, red_person - 1, green_person, blue_person, red_green_pair, green_blue_pair, blue_red_pair + 1)
        elif green_person:
            return (accumulator_result * green_person, free_person, red_person, green_person - 1, blue_person, red_green_pair, green_blue_pair + 1, blue_red_pair)
        else:
            return (accumulator_result * free_person, free_person - 1, red_person, green_person, blue_person + 1, red_green_pair, green_blue_pair, blue_red_pair)

final_result, *_ = reduce(
    lambda accumulated_state, current_ball:
        update_state(current_ball, *accumulated_state),
    input_ball_sequence,
    (ModuloInteger(1), input_ball_count, 0, 0, 0, 0, 0, 0)
)

print(final_result)