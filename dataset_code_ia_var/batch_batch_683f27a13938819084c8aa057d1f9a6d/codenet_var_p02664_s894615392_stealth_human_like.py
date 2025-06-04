T = input()
lst = list(T)  # on convertit la chaîne, pratique
for idx in range(len(lst)):
    # on remplace le "?" mais bon c'est pas hyper efficace...
    if lst[idx] == "?":
        lst[idx] = "D"  # choix arbitraire ?
# finalement j'affiche tout ça
print("".join(lst))