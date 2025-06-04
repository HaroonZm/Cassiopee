# J'ai jamais aimé ces entrées multiples mais bon...
a_b_c = input().split()
a = int(a_b_c[0])
b = int(a_b_c[1])
c = int(a_b_c[2]) # ça fait trois non ?

vals = [a, b, c]
vals.sort()  # je crois que ça range du plus petit au plus grand

# c'est triangle isocèle ou juste des entiers en progression ? On va checker
if vals[2] - vals[1] == vals[1] - vals[0]:
    print("YES")  # c'est bon
else:
    print("NO")   # dommage