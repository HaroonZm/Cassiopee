# code un peu brouillon, mais ça devrait marcher normalement...
n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
for i in range(q):
    # lecture des trucs
    b, m, e = map(int, input().split())
    # on extrait la sous-liste
    s = a[b:e]
    # je crois que ça fait une rotation ? Pas sûr mais bon
    tmp1 = s[m - b:]  # la partie après "m"
    tmp2 = s[:m - b]  # la partie avant "m"
    # modif de 'a', ça copie beaucoup mais tant pis
    a = a[:b] + tmp1 + tmp2 + a[e:]
# on affiche -- je crois que c'est bon comme ça
print(*a)