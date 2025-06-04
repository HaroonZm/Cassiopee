import sys
import threading

def main():
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N, M = map(int, input().split())
    # On crée une liste de booléens pour chaque ligne avec a éléments
    # indexed from 1 to a, donc on stocke à l'indice b-1
    # L'indice de la ligne est de 1 à N
    # On peut utiliser une liste de liste taille N, avec ligne i de taille i
    covered = [bytearray(a) for a in range(1, N+1)]

    for _ in range(M):
        A, B, X = map(int, input().split())
        # Les sommets :
        # (A,B), (A+X,B), (A+X,B+X)
        # Le "triangle bon" inclut tous les points :
        # pour i in [0..X], les points (A+i, B) à (A+X, B+i)
        # plus le diagonale du haut (ligne A, pos B) à (A+X, B+X)
        # mais le problème nous dit que le "triangle bon" se compose de tous les
        # points sur les côtés, mais le question est d'inclure les points entourés par le caoutchouc
        # Le triangle a 3 côtés :
        # - côté vertical entre (A,B) et (A+X,B)
        # - côté diagonal entre (A+X,B) et (A+X,B+X)
        # - côté horizontal entre (A,B) et (A+X,B+X)
        # Mais en fait il faut marquer tous les points à l'intérieur du triangle
        # La « bonne » définition est que tous les clous entre ces points sont recouverts, 
        # donc ce sont tous les points (a,b) tels que :
        # A ≤ a ≤ A+X
        # et b vérifie : b ∈ [B, B + (a - A)]
        # Donc pour chaque ligne a de A à A+X inclus:
        #    on couvre les clous de b allant de B à B+(a - A)
        for a in range(A, A + X + 1):
            start = B - 1
            end = B + (a - A) - 1
            for b in range(start, end + 1):
                covered[a - 1][b] = 1

    # On compte le nombre de vrais marqués
    result = 0
    for line in covered:
        result += sum(line)
    print(result)

threading.Thread(target=main).start()