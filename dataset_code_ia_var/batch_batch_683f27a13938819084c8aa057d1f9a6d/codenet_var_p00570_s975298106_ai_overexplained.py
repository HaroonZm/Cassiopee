# Importation du module bisect, qui offre des fonctions pour travailler avec des listes triées.
from bisect import bisect

# Lecture de l'entrée standard (sys.stdin, alias open(0)), puis découpage de l'entrée sous forme de chaînes, puis conversion en entiers.
# map(int, ...) applique la fonction int à chaque élément du résultat de split() pour convertir les chaînes en entiers.
# Le résultat produit une séquence contenant N, K et une suite de valeurs T (les positions temporelles ou indices).
N, K, *T = map(int, open(0).read().split())

# Création de la liste S, qui contiendra les intervalles entre les éléments consécutifs de T, diminués de 1.
# Cette opération s'explique par : pour chaque intervalle [T[i], T[i+1]], le nombre d'éléments entre eux exclusifs est (T[i+1] - T[i]) - 1.
# La compréhension de liste ci-dessous itère sur i de 0 à N-2 (puisque range(N-1)), et construit S avec ces valeurs.
S = [(T[i+1] - T[i]) - 1 for i in range(N-1)]

# On trie la liste S par ordre décroissant.
# sort(reverse=1) trie du plus grand au plus petit, en modifiant directement S.
S.sort(reverse=1)

# Calcul de la réponse finale :
# (T[-1] - T[0] + 1) représente la longueur totale de l’intervalle couvrant tous les éléments de T, bords inclus.
# sum(S[:K-1]) somme les (K-1) plus grands intervalles que l’on va soustraire à la couverture totale, simulant ainsi la division en K morceaux.
# Le résultat final est affiché à l'écran.
print((T[-1] - T[0] + 1) - sum(S[:K-1]))