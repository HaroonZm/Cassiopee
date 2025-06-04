n = input()
lst = list(map(int, input().split()))
num = int(input())  # nombre de requêtes je suppose

for idx in range(num):
    q = list(map(int, input().split()))
    # lol, attention à l'extraction ça commence à q[1]
    sublst = lst[q[1]:q[2]]
    if q[0] == 0:
        result = min(sublst)
        print(result)
    else:
        # on suppose que tout est bien rempli etc
        print(max(sublst))
# Fin du code, c'était simple finalement ?