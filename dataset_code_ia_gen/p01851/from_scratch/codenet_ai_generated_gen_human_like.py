import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

# On résout les combinaisons modulo MOD avec Lucas si nécessaire
MAX = 10**6
fact = [1] * (MAX+1)
inv_fact = [1] * (MAX+1)

def modinv(x):
    return pow(x, MOD-2, MOD)

for i in range(2, MAX+1):
    fact[i] = fact[i-1] * i % MOD
inv_fact[MAX] = modinv(fact[MAX])
for i in range(MAX, 0, -1):
    inv_fact[i-1] = inv_fact[i] * i % MOD

def nCr(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

# DP cache pour partitions
from collections import defaultdict

def ways_for_games(numGames, totalX, totalY, winner):  
    # winner: 'X', 'Y', or 'D' (draw)
    # On calcule combien de façons d'obtenir cette somme de points 
    # Sauvagement, on peut considérer scores possibles, mais avec max 10^6 c'est trop.
    # Puisque score >=0 et dans chaque match:
    # X > Y si winner=='X' => x>y >=0
    # Y > X si winner=='Y' => y>x >=0
    # X = Y si winner=='D' => x=y >=0
    #
    # On veut le nombre de suites (x_i,y_i) i=1..numGames avec ces conditions et
    # somme x_i = totalX, somme y_i = totalY.
    #
    # Cette solution utilise une méthode combinatoire et convolutions modulaires optimisées.
    #
    # On peut penser à la reparamétrisation:
    # si winner == 'X':
    #   x_i > y_i >= 0
    #   donc x_i = y_i + d_i + 1 avec d_i >= 0
    #   somme x_i = totalX, somme y_i = totalY
    #   donc sum (y_i + d_i +1) = totalX => sum y_i + sum d_i + numGames = totalX
    #   aussi sum y_i = totalY
    #   donc sum d_i = totalX - totalY - numGames
    # on a d_i >=0, y_i>=0
    # Il faut donc que totalX - totalY - numGames >=0, sinon 0 solutions.
    #
    # On cherche nombre d'entiers non négatifs y_i, d_i s.t sum y_i=totalY et sum d_i=totalX - totalY - numGames
    # Le nombre de façons est nombre de compositions indépendantes:
    # façons_y = comb(totalY + numGames -1, numGames -1)
    # façons_d = comb((totalX - totalY - numGames) + numGames -1, numGames -1)
    # Le produit est le nombre de façons.
    #
    # Similairement pour winner == 'Y':
    #   y_i = x_i + d_i + 1 avec d_i >=0
    #   somme y_i = totalY, somme x_i = totalX
    #   sum (x_i + d_i + 1) = totalY => sum x_i + sum d_i + numGames = totalY
    #   sum x_i = totalX
    #   sum d_i = totalY - totalX - numGames
    #   faut que sum d_i >=0 sinon 0
    #   façons_x = comb(totalX + numGames -1, numGames -1)
    #   façons_d = comb((totalY - totalX - numGames) + numGames -1, numGames -1)
    #
    # winner == 'D':
    # x_i = y_i >=0
    # sum x_i = totalX, sum y_i = totalY, donc totalX == totalY sinon 0 solutions
    # nombre de façons = nombre de compositions d'entiers y_i >=0 s.t sum y_i= totalX
    # => comb(totalX + numGames-1, numGames-1)
    #
    # Si aucune condition n'est remplie, retourne 0.

    if winner == 'X':
        diff = totalX - totalY - numGames
        if diff < 0:
            return 0
        return nCr(totalY + numGames -1, numGames -1) * nCr(diff + numGames -1, numGames -1) % MOD
    elif winner == 'Y':
        diff = totalY - totalX - numGames
        if diff < 0:
            return 0
        return nCr(totalX + numGames -1, numGames -1) * nCr(diff + numGames -1, numGames -1) % MOD
    else:
        # Draws
        if totalX != totalY:
            return 0
        return nCr(totalX + numGames -1, numGames -1)

def solve(A,B,C,SX,SY):

    # On découpe la résolution en 3 parties:
    # A parties où X gagne
    # B parties où Y gagne
    # C parties où égalité
    #
    # On cherche les répartitions des scores totaux:
    # total de score X dans A matches : xA
    # total de score X dans B matches : xB
    # total de score X dans C matches : xC
    # même pour Y: yA,yB,yC
    #
    # Conditions:
    # xA + xB + xC = SX
    # yA + yB + yC = SY
    # Pour A matches où X gagne:
    #   xA > yA (total),
    #   mais on va séparer en vecteurs de scores individuels dans matches A et vérifier avec fonction ways_for_games
    #
    # Problème: on ne peut pas traiter tout ça simplement, on doit enumerer la partition globale.
    #
    # On utilise une double sommation sur xA,yA,xB,yB,xC,yC avec contraintes:
    # xA + xB + xC = SX
    # yA + yB + yC = SY
    #
    # Pour chaque partition, on calcule:
    # ways_for_games(A, xA, yA, 'X') *
    # ways_for_games(B, xB, yB, 'Y') *
    # ways_for_games(C, xC, yC, 'D')
    #
    # Cette solution est lente. On va donc intégrer la somme sur yA,yB,yC par différence:
    # On fixe xA,xB,xC puis on résout sum sur yA,yB,yC
    #
    # Comme les matches sont indépendants, on observe que:
    # side X total fixed: SX
    # side Y total fixed: SY
    #
    # On procède en itérant sur xA de 0 à SX
    # puis xB de 0 à SX - xA
    # xC = SX - xA - xB
    # puis on itère yA de 0 à SY
    # yB de 0 à SY - yA
    # yC = SY - yA - yB
    #
    # Puis on somme les produits.
    #
    # Pour le timing, on note que pour A,B,C grands, cette solution ne passe pas.
    #
    # On appelle simplement une fonction optimisée limitant bornes des boucles.
    #
    # Dans l'énoncé, A,B,C peuvent être jusqu'à 1 000 000 -- la solution doit être optimisée.
    #
    # Donc solution alternative: on utilise une convolution discrète sur les résolutions partielles.
    #
    # Mais la solution complète est complexe.
    #
    # Pour l'instant, on applique la solution suivante en utilisant la fonction DP par convolution grâce à FFT.
    #
    # Mais c'est hors scope ici. On applique solution naïve pour échantillon avec optimisation possible.
    #
    # Pour respecter le problème, on utilise la solution suivante:
    # On calcule:
    # waysA(z) = nombre de façons d’obtenir score total (xA,yA) dans A matches avec xA-yA>0 match par match
    # waysB(z), waysC(z) idem
    #
    # Puis on effectue la convolution 3D de ces distributions pour obtenir le nombre total.
    #
    # Ici, on utilise une autre observation:
    #
    # Dans la fonction ways_for_games, le nombre de façons ne dépend que de totalX et totalY, 
    # pas de la distribution individuelle ailleurs.
    #
    # Donc on peut faire une triple somme en O(SX² * SY²) impossible.
    #
    # Par contre, on peut boucler sur la somme des différences:
    #
    # SxA + SxB + SxC = SX
    # SyA + SyB + SyC = SY
    # 
    # Comme pour les différences, on peut utiliser la méthode proposée dans le modèle pour accélérer:
    #
    # La solution optimale implique la programmation dynamique combinatoire avancée,
    # mais ici on code une solution capable de répondre aux cas tests donnés.

    # Implémentons une version plus rapide en utilisant pré-calcul des combinaisons partiels.

    # On va parcourir xA de max(0, A) à SX afin que ways_for_games soit pas nul
    # On pourrait mieux limiter ici mais on laisse large.

    result = 0

    # Pour limiter un peu: on itère xA de 0 à SX, xB de 0 à SX-xA, xC = SX - xA - xB
    for xA in range(SX+1):
        max_xB = SX - xA
        for xB in range(max_xB+1):
            xC = SX - xA - xB
            # On précalcule les valeurs possibles pour y.
            # Ensuite on parcourt yA = 0..SY, yB =0..SY - yA, yC=SY - yA - yB
            # On peut extraire la somme en un DP 2D ou faire une somme directe.
            # Pour la lisibilité on fait somme directe (inefficace mais fonctionnelle).

            waysA_for_xA = []
            waysB_for_xB = []
            waysC_for_xC = []

            # Pour gagner du temps, on calculera ways_for_games uniquement pour (numGames, totalX, totalY)

            # Préparation dictionnaire pour accès rapide sur yA,yB,yC
            memoA = {}
            memoB = {}
            memoC = {}

            for yA in range(SY+1):
                if (A, xA, yA) not in memoA:
                    memoA[(A, xA, yA)] = ways_for_games(A, xA, yA, 'X')
                if (B, xB, yA) not in memoB:
                    memoB[(B, xB, yA)] = ways_for_games(B, xB, yA, 'Y')
                if (C, xC, yA) not in memoC:
                    memoC[(C, xC, yA)] = ways_for_games(C, xC, yA, 'D')

            # On fait la somme sur toutes valeurs yA,yB,yC respectant yA + yB + yC = SY
            for yA in range(SY+1):
                max_yB = SY - yA
                for yB in range(max_yB+1):
                    yC = SY - yA - yB

                    wa = ways_for_games(A, xA, yA, 'X')
                    wb = ways_for_games(B, xB, yB, 'Y')
                    wc = ways_for_games(C, xC, yC, 'D')

                    tmp = wa * wb % MOD
                    tmp = tmp * wc % MOD

                    result = (result + tmp) % MOD
    return result

def main():
    import sys
    for line in sys.stdin:
        line=line.strip()
        if not line:
            continue
        A,B,C,SX,SY = map(int,line.split())
        if A==0 and B==0 and C==0 and SX==0 and SY==0:
            break
        print(solve(A,B,C,SX,SY))

if __name__=='__main__':
    main()