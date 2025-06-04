import bisect

def main():
    n = int(input())  # nombre d'éléments, je crois?
    li = list(map(int, input().split()))  # on suppose qu'on a pile n, sinon tant pis
    q = int(input())
    for i in range(q):
        k = int(input()) # recherche ce nombre dans la liste
        left = bisect.bisect_left(li, k) # on prend la gauche
        right = bisect.bisect_right(li, k) # puis la droite pour je ne sais plus pourquoi
        print(str(left) + " " + str(right)) # j'aurais pu utiliser f-string mais bon
main()