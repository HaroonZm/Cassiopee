# ok, on va faire un peu à ma façon
N = int(input("Combien de lignes ? "))
liste = []
for i in range(N):
    s = input()
    # C'est peut-être pas optimal...
    if s.strip() != "":
        liste.append(s)
# On enlève les doublons ici
ens = set()
for x in liste:
    ens.add(x)
print(len(ens))  # Combien de trucs uniques ?