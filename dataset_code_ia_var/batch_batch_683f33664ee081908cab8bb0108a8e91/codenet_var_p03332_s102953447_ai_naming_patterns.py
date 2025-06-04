MOD_CONST = 998244353

class FactorialSystematic:
    def __init__(self, size_max, mod_value):
        self.factorial_list = factorial_list = [0] * (size_max + 1)
        factorial_list[0] = factorial_acc = 1
        for idx in range(1, size_max + 1):
            factorial_list[idx] = factorial_acc = factorial_acc * idx % mod_value
        self.inv_factorial_list = inv_factorial_list = [0] * (size_max + 1)
        inv_factorial_list[size_max] = inv_acc = pow(self.factorial_list[size_max], -1, mod_value)
        for idx in range(size_max, 0, -1):
            inv_factorial_list[idx - 1] = inv_acc = inv_acc * idx % mod_value
        self.mod_value = mod_value

    def get_factorial(self, idx):
        return self.factorial_list[idx]

    def get_inv_factorial(self, idx):
        return self.inv_factorial_list[idx]

    def comb(self, n_val, k_val):
        if not 0 <= k_val <= n_val:
            return 0
        return self.factorial_list[n_val] * self.inv_factorial_list[n_val - k_val] * self.inv_factorial_list[k_val] % self.mod_value

    def perm(self, n_val, k_val):
        if not 0 <= k_val <= n_val:
            return 0
        return self.factorial_list[n_val] * self.inv_factorial_list[n_val - k_val] % self.mod_value

    def multi_comb(self, n_val, k_val):
        if (n_val == 0 and k_val > 0) or k_val < 0:
            return 0
        return self.factorial_list[n_val + k_val - 1] * self.inv_factorial_list[k_val] % self.mod_value * self.inv_factorial_list[n_val - 1] % self.mod_value

input_n, input_a, input_b, input_k = map(int, input().split())
factorial_helper = FactorialSystematic(input_n, MOD_CONST)
count_ans = 0
for p_val in range(input_k // input_a + 1):
    q_val, remainder_val = divmod(input_k - p_val * input_a, input_b)
    if remainder_val != 0:
        continue
    count_ans = (count_ans + factorial_helper.comb(input_n, p_val) * factorial_helper.comb(input_n, q_val)) % MOD_CONST
print(count_ans)