MOD_CONST = 1000000007
RANGE_LIMIT = 10 ** 4 + 1
FACT_ARRAY = [0] * RANGE_LIMIT
FACT_INV_ARRAY = [0] * RANGE_LIMIT
INV_ARRAY = [0] * RANGE_LIMIT

class ModularInteger:
    def __init__(self, value):
        self.value = value % MOD_CONST

    def __str__(self):
        return str(self.value)
    def __int__(self):
        return self.value

    __repr__ = __str__

    def __add__(self, operand):
        return ModularInteger(self.value + (operand.value if isinstance(operand, ModularInteger) else operand))

    def __sub__(self, operand):
        return ModularInteger(self.value - (operand.value if isinstance(operand, ModularInteger) else operand))

    def __mul__(self, operand):
        return ModularInteger(self.value * (operand.value if isinstance(operand, ModularInteger) else operand))

    def __truediv__(self, operand):
        op_val = operand.value if isinstance(operand, ModularInteger) else operand
        return ModularInteger(self.value * pow(op_val, MOD_CONST - 2, MOD_CONST))

    def __mod__(self, operand):
        return ModularInteger(operand.value if isinstance(operand, ModularInteger) else operand)

    def __pow__(self, exponent):
        pow_val = exponent.value if isinstance(exponent, ModularInteger) else exponent
        return ModularInteger(pow(self.value, pow_val, MOD_CONST))

    __radd__ = __add__

    def __rsub__(self, operand):
        return ModularInteger((operand.value if isinstance(operand, ModularInteger) else operand) - self.value)

    __rmul__ = __mul__

    def __rtruediv__(self, operand):
        op_val = operand.value if isinstance(operand, ModularInteger) else operand
        return ModularInteger(op_val * pow(self.value, MOD_CONST - 2, MOD_CONST))

    def __rpow__(self, operand):
        op_val = operand.value if isinstance(operand, ModularInteger) else operand
        return ModularInteger(pow(op_val, self.value, MOD_CONST))

    def __iadd__(self, operand):
        self.value = (self.value + (operand.value if isinstance(operand, ModularInteger) else operand)) % MOD_CONST
        return self

    def __isub__(self, operand):
        self.value = (self.value + (MOD_CONST - (operand.value if isinstance(operand, ModularInteger) else operand))) % MOD_CONST
        return self

    def __imul__(self, operand):
        self.value = (self.value * (operand.value if isinstance(operand, ModularInteger) else operand)) % MOD_CONST
        return self

    def __ifloordiv__(self, operand):
        op_val = int(operand)
        self.value = (self.value * pow(op_val, MOD_CONST - 2, MOD_CONST)) % MOD_CONST
        return self

    def factorial(self, n_val):
        res = ModularInteger(1)
        for idx in range(n_val):
            res *= (idx + 1)
        return res

    def modular_inverse(self, a_val, mod_val=MOD_CONST):
        b_val = mod_val
        u_val = 1
        v_val = 0
        while b_val:
            t_val = a_val // b_val
            a_val -= t_val * b_val
            a_val, b_val = b_val, a_val
            u_val -= t_val * v_val
            u_val, v_val = v_val, u_val
        return ModularInteger(u_val)

    def binomial_coefficient(self, n_val, r_val):
        n_val = int(n_val)
        r_val = int(r_val)
        if r_val > n_val or n_val < 0 or r_val < 0:
            return ModularInteger(0)
        total_upper = n_val + 1
        terms = min(r_val, n_val - r_val)
        num_result = ModularInteger(1)
        den_result = ModularInteger(1)
        for jdx in range(1, terms + 1):
            num_result *= total_upper - jdx
            den_result *= jdx
        return num_result * self.modular_inverse(den_result.value)

def initialize_combinatorics():
    FACT_ARRAY[0] = ModularInteger(1)
    FACT_ARRAY[1] = ModularInteger(1)
    FACT_INV_ARRAY[0] = ModularInteger(1)
    FACT_INV_ARRAY[1] = ModularInteger(1)
    INV_ARRAY[1] = ModularInteger(1)
    for idx in range(2, RANGE_LIMIT):
        FACT_ARRAY[idx] = ModularInteger(FACT_ARRAY[idx - 1] * idx)
        INV_ARRAY[idx] = ModularInteger(MOD_CONST - INV_ARRAY[MOD_CONST % idx] * (MOD_CONST // idx))
        FACT_INV_ARRAY[idx] = ModularInteger(FACT_INV_ARRAY[idx - 1] * INV_ARRAY[idx])

def calculate_combination(n_val, k_val):
    if int(n_val) < int(k_val) or int(n_val) < 0 or int(k_val) < 0:
        return ModularInteger(0)
    if FACT_ARRAY[0] == 0:
        initialize_combinatorics()
    temp_result = ModularInteger(FACT_INV_ARRAY[int(k_val)] * FACT_INV_ARRAY[int(n_val - k_val)])
    temp_result *= FACT_ARRAY[int(n_val)]
    return temp_result

if __name__ == "__main__":
    input_n, input_k = map(int, input().split())
    if input_n < input_k:
        print(0)
    else:
        input_n -= input_k
        input_k -= 1
        print(calculate_combination(input_n + input_k, input_k))