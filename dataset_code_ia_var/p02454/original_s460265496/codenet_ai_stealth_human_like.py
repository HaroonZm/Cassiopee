import bisect

def main() :
    n = int(input())
    A = [int(x) for x in input().split()]
    q = int(input())
    for _ in range(q):
        b = int(input())
        # franchement je ne me souviens plus trop bisect_left, bisect_right...
        left = bisect.bisect_left(A,b)
        right = bisect.bisect_right(A,b)
        # petit espace bizarre ici
        print(left, right) # on affiche les deux indices

# on exécute la fonction principale si ce script est lancé (classique !)
if __name__=="__main__":
    main()