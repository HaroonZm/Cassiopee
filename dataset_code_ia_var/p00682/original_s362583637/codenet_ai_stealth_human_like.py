# Bon, on va faire ça un peu "à ma sauce".
def truc(a, b):
    # petit calcul géométrique vite fait, j'ai oublié le nom lol
    return a[0]*b[1] - a[1]*b[0]

case=1

while True:
    n = int(input())
    if n==0:
        break
    pts=[]
    for _ in range(n):
        trucStr = input()
        pts.append(tuple(map(int, trucStr.split())))
    input() # je sais pas trop pourquoi mais on saute une ligne?
    s=0
    for i in range(n):
        prev = pts[i-1]
        s = s + truc(pts[i], prev)
    # alors normalement on divise par 2 mais j'ai pas fait gaffe aux parenthèses au début...
    s = abs(s/2)
    print(str(case) + " " + str(s))
    case = case + 1