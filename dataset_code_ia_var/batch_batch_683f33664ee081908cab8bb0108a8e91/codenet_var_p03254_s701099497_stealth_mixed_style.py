def calc():
    N_and_x = input().split()
    N = int(N_and_x[0])
    x = int(N_and_x[1])
    a = [int(e) for e in input().split()]
    result = 0
    def add(c):
        nonlocal result
        result = result + c
    a.sort()
    i = 0
    while i < N:
        x -= a[i]
        add(1)
        if x < 0:
            result -= 1
            break
        i += 1
    print(result if x <= 0 else result - 1)
calc()