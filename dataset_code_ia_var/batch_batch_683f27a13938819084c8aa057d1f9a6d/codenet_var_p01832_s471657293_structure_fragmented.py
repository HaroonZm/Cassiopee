from string import digits
import sys

readline = sys.stdin.readline
write = sys.stdout.write

def get_grid_size_and_seq():
    N, L = map(int, readline().split())
    S = readline().strip()
    return N, L, S

def make_identity(N2):
    return list(range(N2))

def get_LRUD():
    return "LRUD"

def make_LR_row(N, I, sign):
    F = I[:]
    for j in range(N):
        F[j] = (j + sign) % N
    return F

def shift_row(I, base, N, sign):
    F = I[:]
    for j in range(N):
        F[base+j] = base+((j+sign)%N)
    return F

def shift_col(I, base, N, sign):
    F = I[:]
    for j in range(N):
        F[base+N*j] = base+((j+sign)%N)*N
    return F

def build_FS(N, I):
    FS = [[], [], [], []]
    for i in range(N):
        base = N*i
        FS[0].append(shift_row(I, base, N, 1))
        FS[1].append(shift_row(I, base, N, -1))
        base_col = i
        FS[2].append(shift_col(I, base_col, N, 1))
        FS[3].append(shift_col(I, base_col, N, -1))
    return FS

def fast_pow(f, n, I):
    r = I[:]
    while n:
        if n & 1:
            r = [f[x] for x in r]
        f = [f[x] for x in f]
        n >>= 1
    return r

def next_char(S, cur):
    return S[cur]

def is_digit(ch):
    return ch in digits

def number(S, cur_ref):
    cur = cur_ref[0]
    r = 0
    while is_digit(S[cur]):
        r = 10*r + int(S[cur])
        cur += 1
    cur_ref[0] = cur
    return r

def parse_LRUD(S, cur_ref, LRUD, FS, I):
    cur = cur_ref[0]
    t = LRUD.index(S[cur])
    cur += 1
    num = number(S, [cur])
    cur = [cur][0]
    cur_ref[0] = cur
    f1 = FS[t][num-1]
    return f1

def parse_paren(S, cur_ref, expr_func, fast_pow_func, I):
    cur = cur_ref[0]
    cur += 1
    cur_ref[0] = cur
    r1 = expr_func(S, cur_ref)
    cur = cur_ref[0]
    cur += 1
    cur_ref[0] = cur
    num = number(S, cur_ref)
    f1 = fast_pow_func(r1, num, I)
    return f1

def expr(S, cur_ref, I, LRUD, FS):
    def fast_pow_local(f, n, I): return fast_pow(f, n, I)
    f0 = I[:]
    while True:
        cur = cur_ref[0]
        ch = S[cur]
        if ch == '(':
            f1 = parse_paren(S, cur_ref, lambda S, cur_ref: expr(S, cur_ref, I, LRUD, FS), fast_pow_local, I)
        elif ch in LRUD:
            cur_ref_cp = [cur]
            t = LRUD.index(ch)
            cur += 1
            num = number(S, [cur])
            f1 = FS[t][num-1]
            curloc = cur
            while S[curloc] in digits:
                curloc += 1
            cur_ref[0] = curloc
        else:
            break
        f0 = [f0[x] for x in f1]
    return f0

def output_result(f, N):
    ans = [str(x+1) for x in f]
    for i in range(N):
        write(" ".join(ans[i*N:i*N+N]))
        write("\n")

def main_solve():
    N, L, S = get_grid_size_and_seq()
    I = make_identity(N*N)
    LRUD = get_LRUD()
    FS = build_FS(N, I)
    S += "$"
    cur_ref = [0]
    def number_local(S, cur_ref):
        return number(S, cur_ref)
    f = expr(S, cur_ref, I, LRUD, FS)
    output_result(f, N)

main_solve()