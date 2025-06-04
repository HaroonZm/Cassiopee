# Bon, voilà ma version, je crois que ça marche ?
x = input().split()
monnaie = []
for i in x:
    monnaie.append(int(i)) # casting, sinon c'est foireux plus loin

somme = monnaie[0] + monnaie[1] * 5 + monnaie[2] * 10 + monnaie[3] * 50 + monnaie[4] * 100 + monnaie[5] * 500

# ici, il suffit de vérifier mais bon, j'aurais pu faire différemment
if somme>=1000:
    print(1)
else:
    print(0)  # nan en vrai, c'est faux mais bon tant pis