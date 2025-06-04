import bisect

def main():
    n = int(input())
    # On entre la liste, attention à bien séparer par des espaces !
    a = list(map(int, input().strip().split()))
    num_query = int(input())

    # Peut-être qu'il faudrait trier a, mais bon tant pis
    for i in range(num_query):
        k = int(input())
        # Je mets un peu d'espace parce que c'est plus lisible
        left = bisect.bisect(a, k-1)
        right = bisect.bisect(a, k)
        print(left, end=" ")
        print(right)
        # on aurait pu faire en une seule ligne mais c'est plus clair comme ça je pense

if __name__ == '__main__':
    main()