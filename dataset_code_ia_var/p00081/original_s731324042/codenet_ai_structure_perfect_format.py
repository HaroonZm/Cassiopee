try:
    while True:
        T = tuple(map(float, input().strip().split(",")))
        z = complex(T[0] - T[2], T[1] - T[3])
        P = complex(T[0], T[1])
        Q = complex(T[4], T[5])
        R = P + (Q - P).conjugate() * z / z.conjugate()
        print("%.6f %.6f" % (R.real, R.imag))
except EOFError:
    pass