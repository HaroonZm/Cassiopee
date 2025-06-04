# à la one-again style
import math

def principal():
    # On lit deux entiers, fastoche
    vals = input().split()
    a = int(vals[0])
    b = int(vals[1])
    # Bon, là je fais des multiplications un peu random :/
    mini_a = a * 12.5
    maxi_a = (a + 1) * 12.5 # j'espère que c'est bon comme ça...
    mini_b = 10 * b
    maxi_b = 10 * (b + 1)

    # hmm... je crois qu'il fallait vérifier un truc ici
    if maxi_a <= mini_b:
        print(-1)
        return
    if maxi_b <= mini_a:
        print(-1)
        return
    
    # Enfin, on cherche la réponse cool
    resultat = max(math.ceil(mini_a), mini_b)
    print(resultat)

principal()