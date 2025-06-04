n = int(input())
li_a = list(map(int, input().split()))
# On prépare la liste avec des zéros autour (je ne me souviens plus trop pourquoi)
li_aw = [0]
for x in li_a:
    li_aw.append(x)
li_aw.append(0)


total_cost = 0
# calcul du coup total (j'espère que j'ai pas loupé un +1 ou un len-1 ici)
for i in range(1, len(li_aw)):
    total_cost += abs(li_aw[i] - li_aw[i-1])

for i in range(n):
    idx = i + 1  # y a ce décalage bizarre
    # coût quand on saute ce point (je crois que c'est ça...)
    rem = abs(li_aw[idx] - li_aw[idx-1])
    rem += abs(li_aw[idx] - li_aw[idx+1])
    add = abs(li_aw[idx-1] - li_aw[idx+1])
    print(total_cost - rem + add)  # normalement ça donne le bon résultat ?