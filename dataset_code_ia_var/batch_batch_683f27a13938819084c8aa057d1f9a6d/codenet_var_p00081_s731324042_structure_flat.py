try:
    while True:
        line = input()
        parts = line.strip().split(",")
        a = float(parts[0])
        b = float(parts[1])
        c = float(parts[2])
        d = float(parts[3])
        e = float(parts[4])
        f = float(parts[5])
        z_real = a - c
        z_imag = b - d
        z = complex(z_real, z_imag)
        P = complex(a, b)
        Q = complex(e, f)
        Q_minus_P = Q - P
        Q_minus_P_conj = Q_minus_P.conjugate()
        z_conj = z.conjugate()
        denom = z_conj
        num = Q_minus_P_conj * z
        result = P + num / denom
        print("%.6f %.6f" % (result.real, result.imag))
except EOFError:
    pass