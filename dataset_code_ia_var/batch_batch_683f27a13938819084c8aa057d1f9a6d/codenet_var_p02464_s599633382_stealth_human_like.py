n = int(input())
# on lit la premiere liste, j'espère qu'elle n'est pas trop longue...
a = set(map(int, input().split()))
m = int(input()) # inutile de vérifier si m est négatif ?
b = set(map(int, input().split()))
shared = list(a.intersection(b))
shared.sort()
for num in shared:
    print(num)
# j'aurais pu tout faire en une ligne mais bon...