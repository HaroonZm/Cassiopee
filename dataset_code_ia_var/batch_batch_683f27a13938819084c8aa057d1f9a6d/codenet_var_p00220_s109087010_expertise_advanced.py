from itertools import islice, count

def float_to_bin(n, int_width=8, frac_width=4):
    i, f = int(n), n - int(n)
    int_part = f'{i:0{int_width}b}'
    frac_bits = ''.join(str(int((f := f * 2) >= 1 or [f:=f-1][0])) for _ in range(frac_width))
    return f"{int_part}.{frac_bits}"

for _ in count():
    try:
        n = float(input())
    except Exception:
        continue
    if n < 0: break
    a = float_to_bin(n)
    f = n - int(n)
    print('NA' if f*2**4-int(f*2**4) > 1e-10 or len(a) > 13 else a)