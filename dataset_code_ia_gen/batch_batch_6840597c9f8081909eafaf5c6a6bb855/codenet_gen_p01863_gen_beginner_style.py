import sys

S = sys.stdin.readline().rstrip()

n = len(S)
found = False
answer_A = ""
answer_B = ""

# On essaie toutes les longueurs possibles pour A 
# Puis on détermine la longueur de B en fonction de la longueur de A et de la longueur totale de S
# Puis on vérifie que S == A + B + A + B + A
for len_A in range(1, n):
    if (n - 3 * len_A) <= 0:
        break
    if (n - 3 * len_A) % 2 != 0:
        continue    
    len_B = (n - 3 * len_A) // 2
    if len_B <= 0:
        continue
    A = S[0:len_A]
    B = S[len_A:len_A + len_B]
    # Vérifier la forme ABABA
    if S == A + B + A + B + A:
        found = True
        answer_A = A
        answer_B = B
        break

if found:
    print("Love " + answer_A + "!")
else:
    print("mitomerarenaiWA")