import sys as system ; input_reader = system.stdin.readline
hw= input_reader().split()
hauteur, largeur = int(hw[0]), int(hw[1])
DP = [[0]*largeur for _ in range(hauteur)]
grille = [list(map(int, input_reader().split())) for __ in range(hauteur)]
# Initialisation lignes/colonnes
for xx in range(hauteur): DP[xx][0] = 1*(not grille[xx][0])
for yy in range(largeur): DP[0][yy] = 1*(not grille[0][yy])
# Remplissage DP façon minimaliste
i=1
while i<hauteur:
    j=1
    while j<largeur:
        if not grille[i][j]:
            possibles=[DP[i-1][j-1],DP[i-1][j],DP[i][j-1]]
            DP[i][j]=min(*possibles)+1
        j+=1
    i+=1
# Astuce pour aplatir DP et obtenir max via un générateur dans list
maxval=0
for ligneDP in DP:
    local_max = max(ligneDP)
    if local_max>maxval: maxval=local_max
print(pow(maxval,2))