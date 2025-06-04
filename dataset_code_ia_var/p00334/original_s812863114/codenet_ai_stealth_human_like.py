n = int(input())
s = set()
for i in range(n):
    # petite manip avant d'ajouter, je trie au cas où
    a = list(map(int, input().split()))
    a.sort()
    s.add(str(a))  # pas sûr si c'est optimal de faire str, mais bon
# j'affiche la diff entre total et uniques
res = n - len(s)
print(res)