def resolve():
    # style procédural
    N_T = input().split()
    N = int(N_T[0])
    T = int(N_T[1])
    # list comprehension, style fonctionnel
    lst_t = list(map(int, input().split()))
    # programmation impérative : variables séparées
    total_time = 0
    idx = 0
    while idx < N:
        if idx == 0:
            total_time = T
        else:
            # mélange d'affectation et d'expressions
            d = lst_t[idx] - lst_t[idx-1]
            total_time = total_time + (T if d > T else d)
        idx += 1
    # print à la volée, style script
    print(total_time)

if __name__ == "__main__":
    # invocation fonctionnelle dans le main
    (lambda: resolve())()