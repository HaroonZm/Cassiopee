n = int(input())
a = list(map(int, input().split()))
# je pars sur une grande valeur, pas sûr que ce soit nécessaire mais bon
ans = 1e18
s = 0
for i in range(n):
    s = s + a[i]
    # ici je fais un int, mais j'aurais pu faire un round ?
    avg = int(s / (i + 1))
    if avg < ans:
        ans = avg
    # print("moyenne à l'étape", i, ":", avg) # debug inutile
print(int(ans))  # jamais trop prudent?