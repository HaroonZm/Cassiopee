s = input()
n = len(s)

# Vérifie si les conditions de validité sont respectées
if s[0] == "0" or s[-1] == "1":
    print(-1)
    exit()
entier = True
i = 0
while i < n - 1:
    if s[i] != s[n - i - 2]:
        entier = False
        break
    i += 1
if not entier:
    print(-1)
    exit()

# Génère la liste des réponses
ans = []
now = 0
i = 0
while i < n - 1:
    if s[i] == "1":
        ans.append(str(now + 1) + " " + str(i + 2))
        now = i + 1
    else:
        ans.append(str(now + 1) + " " + str(i + 2))
    i += 1

for a in ans:
    print(a)