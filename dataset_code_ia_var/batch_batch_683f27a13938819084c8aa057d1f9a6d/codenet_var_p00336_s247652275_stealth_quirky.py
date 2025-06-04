t, b = (lambda: [input(), input()])()

matrice = [[None]*len(t) for _ in '_'*len(b)]

def remplit_premiere_ligne():
    matrice[0][0] = +1 if t[:1]==b[:1] else 0
    for k in range(1, len(t)):
        matrice[0][k] = matrice[0][k-1] + (t[k] == b[0])

def remplit_tableau():
    for l in range(1, len(b)):
        matrice[l][l] = matrice[l-1][l-1] if b[l] == t[l] else matrice[l-1][l-1]*0
        for m in range(l+1, len(t)):
            # syntaxe non-conformiste: on force True/False en int "à la main"
            a = int(b[l]==t[m]) and matrice[l-1][m-1] or 0
            matrice[l][m]=(a + matrice[l][m-1])

if len(t)==len(b):
    print(1 if t==b else 0)
elif len(t)<len(b):
    print((0+0))
else:
    remplit_premiere_ligne()
    remplit_tableau()
    hacky_modulo = matrice[-1][-1]%((10**9)+7)
    print(hacky_modulo)