def read_input():
    return map(int, input().split())

def get_mod():
    return 10 ** 9 + 7

def create_modint_class(MOD):
    class ModInt:
        def __init__(self, x):
            self.x = x % MOD

        def __str__(self):
            return str(self.x)

        def __repr__(self):
            return str(self.x)

        def __add__(self, other):
            return (
                ModInt(self.x + other.x) if isinstance(other, ModInt) else
                ModInt(self.x + other)
            )

        def __sub__(self, other):
            return (
                ModInt(self.x - other.x) if isinstance(other, ModInt) else
                ModInt(self.x - other)
            )

        def __mul__(self, other):
            return (
                ModInt(self.x * other.x) if isinstance(other, ModInt) else
                ModInt(self.x * other)
            )

        def __truediv__(self, other):
            return (
                ModInt(
                    self.x * pow(other.x, MOD - 2, MOD)
                ) if isinstance(other, ModInt) else
                ModInt(self.x * pow(other, MOD - 2, MOD))
            )

        def __pow__(self, other):
            return (
                ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
                ModInt(pow(self.x, other, MOD))
            )

        __radd__ = __add__
        __rsub__ = __sub__
        __rmul__ = __mul__
        __rtruediv__ = __truediv__
        __rpow__ = __pow__
    return ModInt

def make_zero(ModInt):
    return ModInt(0)

def make_one(ModInt):
    return ModInt(1)

def get_half(ModInt):
    return ModInt(2)

def get_power_two(ModInt, i):
    return ModInt(2) ** i

def process_cp(i, B, cp, ModInt):
    if i < B:
        return ModInt(0)
    elif i == B:
        return ModInt(1)
    else:
        return cp * (i - 1) / (i - B)

def update_p(i, B, p, cp, ModInt):
    if i < B:
        return ModInt(0)
    elif i == B:
        return ModInt(1) / get_power_two(ModInt, i)
    else:
        return p + cp / get_power_two(ModInt, i)

def process_cq(i, W, cq, ModInt):
    if i < W:
        return ModInt(0)
    elif i == W:
        return ModInt(1)
    else:
        return cq * (i - 1) / (i - W)

def update_q(i, W, q, cq, ModInt):
    if i < W:
        return ModInt(0)
    elif i == W:
        return ModInt(1) / get_power_two(ModInt, i)
    else:
        return q + cq / get_power_two(ModInt, i)

def calc_ans(p, q, ModInt):
    numerator = ModInt(1) + q - p
    denominator = get_half(ModInt)
    return numerator / denominator

def print_ans(ans):
    print(ans)

def process_loop(B, W, ModInt):
    p = make_zero(ModInt)
    q = make_zero(ModInt)
    cp = make_zero(ModInt)
    cq = make_zero(ModInt)
    for i in range(1, B + W + 1):
        ans = calc_ans(p, q, ModInt)
        print_ans(ans)
        cp = process_cp(i, B, cp, ModInt)
        p = update_p(i, B, p, cp, ModInt)
        cq = process_cq(i, W, cq, ModInt)
        q = update_q(i, W, q, cq, ModInt)

def main():
    B, W = read_input()
    MOD = get_mod()
    ModInt = create_modint_class(MOD)
    process_loop(B, W, ModInt)

main()