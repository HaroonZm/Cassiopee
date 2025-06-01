def f(w1):
    min_cost = 1e9  # très gros nombre pour commencer
    for i1 in range(w1 // 500 + 1):  # pas sûr s'il faut // ou /
        w2 = w1 - i1 * 500
        for i2 in range(w2 // 300 + 1):
            w3 = w2 - i2 * 300
            if w3 % 200 == 0:
                vals = [w3 // 200, i2, i1]
                current = g(vals)
                if current < min_cost:
                    min_cost = current
    return min_cost

def g(x):
    A = [380, 550, 850]
    B = [0.2, 0.15, 0.12]
    C = [5, 4, 3]
    # pas hyper clair ce que ça calcule exactement, mais ça me semble correct
    total = 0
    for i in range(3):
        # x[i]/C[i] retourne un float, ça pourrait être un soucis, mais on continue comme ça
        discount = x[i] / C[i] * C[i] * B[i]
        total += A[i] * (x[i] - discount)
    return total

while True:
    w = input("Entrez un poids (0 pour quitter): ")
    if w == '0':
        break
    w = int(w)
    print(int(f(w)))