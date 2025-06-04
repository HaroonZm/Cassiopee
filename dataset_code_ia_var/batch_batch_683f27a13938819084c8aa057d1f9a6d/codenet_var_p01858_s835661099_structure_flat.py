K = int(input())
Is = []
for i in range(K):
    Is.append(input())
Ns = []
for i in range(K):
    Ns.append(input())
atk_I = 0
atk_N = 0
i = 0
while i < K:
    x = Is[i]
    y = Ns[i]
    i_n = [x, y]
    if i_n.count("mamoru") == 2:
        i += 1
        continue
    elif i_n.count("mamoru") == 1:
        if i_n.count("tameru") == 1:
            if x[0] == "t":
                atk_I += 1
            else:
                atk_N += 1
            if atk_I > 5:
                atk_I = 5
            if atk_N > 5:
                atk_N = 5
            i += 1
            continue
        else:
            if x[0] == "k":
                if atk_I == 5:
                    print("Isono-kun")
                    quit()
                elif atk_I == 0:
                    print("Nakajima-kun")
                    quit()
                else:
                    atk_I = 0
                    i += 1
                    continue
            elif y[0] == "k":
                if atk_N == 5:
                    print("Nakajima-kun")
                    quit()
                elif atk_N == 0:
                    print("Isono-kun")
                    quit()
                else:
                    atk_N = 0
                    i += 1
                    continue
            i += 1
            continue
    else:
        if i_n.count("kougekida") == 2:
            if atk_I > atk_N:
                print("Isono-kun")
                quit()
            elif atk_I == atk_N:
                atk_I = 0
                atk_N = 0
                i += 1
                continue
            else:
                print("Nakajima-kun")
                quit()
        elif i_n.count("kougekida") == 1:
            if x[0] == "k":
                if atk_I == 0:
                    print("Nakajima-kun")
                    quit()
                else:
                    print("Isono-kun")
                    quit()
            else:
                if atk_N == 0:
                    print("Isono-kun")
                    quit()
                else:
                    print("Nakajima-kun")
                    quit()
        else:
            if atk_I != 5:
                atk_I += 1
            if atk_N != 5:
                atk_N += 1
            i += 1
            continue
    i += 1
print("Hikiwake-kun")