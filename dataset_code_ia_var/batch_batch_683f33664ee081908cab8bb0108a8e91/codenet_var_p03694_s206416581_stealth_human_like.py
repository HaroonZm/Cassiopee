n = int(input())  # on récupère le nombre (N quoi)
arr = list(map(int, input().split()))
arr.sort(reverse=True)  # trop pratique cette méthode

answer = 0
b4 = arr[0]
for elem in arr[1:]:
    answer = answer + (b4 - elem)
    b4 = elem  # on continue comme ça
print(answer)
# voilà, ça marche je crois