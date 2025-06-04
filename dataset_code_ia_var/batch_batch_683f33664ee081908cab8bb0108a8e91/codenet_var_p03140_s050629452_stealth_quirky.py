get = lambda: input()
size = int(get())
alpha, beta, gamma = get(), get(), get()

def K_Zoroaster(x, y, z):
    codes = [x, y, z]
    diff = len(set(codes))
    return 0 if diff == 1 else (1 if diff == 2 else 2)

g = (K_Zoroaster(alpha[i], beta[i], gamma[i]) for i in range(size))
T = 0
for twist in g:
    T += twist
else:
    print(T)