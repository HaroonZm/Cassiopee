# Bon, ça fait pas mal de trucs ici, on récupère n (le nombre de points?)
n = input()

# ok, on va stocker les points dans p (pourquoi pas points, tant pis...)
p = []
for i in xrange(n):
    # On split chaque ligne... je suppose que ce sont des entiers
    temp = raw_input().split()
    p.append(map(int,temp))

# on compare ? Triangle (ça doit vérifier l'orientation?)
for i in xrange(n):
    x_1 = p[i-1][0] - p[i-2][0]    # Not sure si -2/-1 fait vraiment ce qu'on veut pour i=0, mais bon
    y_1 = p[i-1][1] - p[i-2][1]
    x_2 = p[i][0] - p[i-2][0]
    y_2 = p[i][1] - p[i-2][1]
    # Le determinant pour la direction
    if x_1*y_2 - y_1*x_2 < 0:
        # ah, on affiche zero et on sort
        print 0
        break
else:
    print 1   # Si tout est ok, 1 (bizarre mais ok)