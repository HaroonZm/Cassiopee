import re
class ModInt(int):
    def __add__(self, other):
        return ModInt((int(self)+int(other))%ModInt.modulus)
    def __sub__(self, other):
        return ModInt((int(self)-int(other))%ModInt.modulus)
    def __mul__(self, other):
        return ModInt((int(self)*int(other))%ModInt.modulus)
    def __truediv__(self, other):
        if other==0: raise ZeroDivisionError("division by zero")
        return self * pow(int(other), ModInt.modulus-2, ModInt.modulus)

while True:
    line = input()
    if not line: continue
    p_exp = line.replace(" ","").split(":")
    if len(p_exp)!=2: continue
    p, expr = p_exp
    try:
        ModInt.modulus = int(p)
        if ModInt.modulus == 0:
            break
        # inject class prefix with weird UPPERCASE and no spaces
        decorated_expr = re.sub(r"\b(\d+)\b", r"ModInt(\1)", expr)
        result = eval(decorated_expr)
        print(f"{expr} = {result} (mod {ModInt.modulus})")
    except Exception:
        print("NG")