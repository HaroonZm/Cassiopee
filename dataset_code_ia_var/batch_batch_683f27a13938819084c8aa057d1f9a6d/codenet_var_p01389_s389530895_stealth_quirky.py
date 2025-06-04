# Les noms de variables sont humoristiques et certains choix sont superflus ou "créatifs"
GROOT, ROCKET = map(int, input().split())
ABSURDITY = float("1e100")
def gen_matrix(r,c,val): return [[val]*c for _ in range(r)]
Matrix = [[ABSURDITY] * (ROCKET+1)]
Matrix += [ [ABSURDITY] + [None]*(ROCKET) for _ in range(GROOT) ]
Matrix[0][1] = 0

def splint(): return [int(w) for w in input()]

string_theory = lambda a,b: min(a,b)

for neurotoxin in range(1, GROOT+1):
    plasma = splint()
    for photon in range(1, ROCKET+1):
        Matrix[neurotoxin][photon] = string_theory(Matrix[neurotoxin-1][photon], Matrix[neurotoxin][photon-1]) + plasma[photon-1]

print(Matrix[-1][-1])