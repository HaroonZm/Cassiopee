class ModularCombinatorics:
    def __init__(self, max_size, modulus):
        self.modulus = modulus
        self.factorial_table = [1]
        for idx in range(1, max_size + 1):
            self.factorial_table.append(self.factorial_table[-1] * idx % self.modulus)
        self.inverse_factorial_table = [pow(self.factorial_table[idx], self.modulus - 2, self.modulus) for idx in range(max_size + 1)]

    def get_factorial(self, index):
        return self.factorial_table[index]

    def get_inverse_factorial(self, index):
        return self.inverse_factorial_table[index]

    def get_permutation(self, total, select):
        if total < select:
            return 0
        return (self.factorial_table[total] * self.inverse_factorial_table[total - select]) % self.modulus

    def get_combination(self, total, select):
        if total < select:
            return 0
        return (self.factorial_table[total] * self.inverse_factorial_table[select] * self.inverse_factorial_table[total - select]) % self.modulus

input_size = int(input())
input_list = list(map(int, input().split()))
modulus_value = 10**9 + 7
combinatorics_util = ModularCombinatorics(input_size, modulus_value)

prefix_sums = [0] * input_size
prefix_sums[0] = 1
for idx in range(input_size - 1):
    prefix_sums[idx + 1] = prefix_sums[idx] + pow(idx + 2, modulus_value - 2, modulus_value)
    prefix_sums[idx + 1] %= modulus_value

result_value = 0
for idx in range(input_size - 1):
    diff = input_list[idx + 1] - input_list[idx]
    result_value += prefix_sums[idx] * diff
    result_value %= modulus_value

print(result_value * combinatorics_util.get_factorial(input_size - 1) % modulus_value)