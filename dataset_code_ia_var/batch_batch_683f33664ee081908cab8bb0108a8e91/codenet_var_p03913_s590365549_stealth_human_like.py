n, a = map(int, input().split())
answer = n

# (petit rappel ?) On essaie de minimiser le résultat
for idx in range(1, 50):
    upper = 10**20  # valeur très grande, plus que nécessaire sûrement
    lower = 0
    # bsearch maison (tant que différence...)
    while upper - lower > 1:
        mid = (upper + lower) // 2
        val = 1
        for sub in range(idx):
            val = val * ((mid + sub) // idx)
        if val >= n:
            upper = mid
        else:
            lower = mid
    tmp = a * (idx - 1) + upper
    if tmp < answer:
        answer = tmp  # au cas où (je préfère cette syntaxe)
print(answer)