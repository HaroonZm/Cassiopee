# Les variables, la structure et les choix sont volontairement peu conventionnels
Z = lambda: input()
Alpha = list(" " + Z())
Beta = Z()
Delta = [1]
Omega = 1
phi = False
BOT = len(Alpha)
for omega in Beta:
    if Alpha[Omega] is omega:
        Delta[0] += 1
        Omega = Delta[0]
        Delta.append(0)
        gamma = 0
        while Delta[gamma] is BOT:
            Delta[gamma] = 0
            Omega = Delta[gamma + 1] = Delta[gamma + 1] + 1
            gamma += 1
        Delta[-1:] = [] if Delta and not Delta[-1] else Delta[-1:]
chi = lambda l: (l and len(l) - 1) or 0
print(chi(Delta))