import sys

sys.setrecursionlimit(10**7)

def modinv(a, p):
    # Fermatの小定理による逆元計算（pは素数）
    return pow(a, p-2, p)

def tokenize(exp):
    tokens = []
    i = 0
    while i < len(exp):
        c = exp[i]
        if c.isspace():
            i += 1
            continue
        elif c in '+-*/()':
            tokens.append(c)
            i += 1
        elif c.isdigit():
            j = i
            while j < len(exp) and exp[j].isdigit():
                j += 1
            tokens.append(int(exp[i:j]))
            i = j
        else:
            # 不正文字なら無視（問題文では無いはず）
            i += 1
    return tokens

def parse_expr(tokens, p):
    # 再帰下降構文解析をする
    # expr := term { + | - term }
    # term := factor { * | / factor }
    # factor := number | ( expr )
    
    def parse_factor():
        nonlocal pos
        if pos >= len(tokens):
            return None, False
        t = tokens[pos]
        if isinstance(t, int):
            pos += 1
            return t % p, True
        elif t == '(':
            pos += 1
            val, ok = parse_expr()
            if not ok:
                return None, False
            if pos >= len(tokens) or tokens[pos] != ')':
                return None, False
            pos += 1
            return val, True
        else:
            return None, False

    def parse_term():
        nonlocal pos
        val, ok = parse_factor()
        if not ok:
            return None, False
        while pos < len(tokens) and tokens[pos] in ('*', '/'):
            op = tokens[pos]
            pos += 1
            rval, rok = parse_factor()
            if not rok:
                return None, False
            if op == '*':
                val = (val * rval) % p
            else:  # '/'
                if rval == 0:
                    return None, False
                inv = modinv(rval, p)
                val = (val * inv) % p
        return val, True

    def parse_expr():
        nonlocal pos
        val, ok = parse_term()
        if not ok:
            return None, False
        while pos < len(tokens) and tokens[pos] in ('+', '-'):
            op = tokens[pos]
            pos += 1
            rval, rok = parse_term()
            if not rok:
                return None, False
            if op == '+':
                val = (val + rval) % p
            else:  # '-'
                val = (val - rval) % p
        return val, True

    pos = 0
    val, ok = parse_expr()
    if not ok:
        return None, False
    if pos != len(tokens):
        return None, False
    return val, True

for line in sys.stdin:
    line=line.rstrip('\n')
    if line == '0:':
        break
    if ':' not in line:
        continue
    pstr, expraw = line.split(':',1)
    p = int(pstr)
    exp = expraw.strip()
    tokens = tokenize(exp)
    val, ok = parse_expr(tokens, p)
    if not ok or val is None:
        print("NG")
    else:
        # 出力はexpを空白無しで、= の前後空白1つ、(mod p) の間に空白入れる
        expnospace = ''.join(str(t) if isinstance(t,int) else t for t in tokens)
        print(f"{expnospace} = {val} (mod {p})")