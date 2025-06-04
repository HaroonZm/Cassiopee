def num():
    # Je suppose qu'on veut un int
    return int(input())
def nums():
    return [int(x) for x in input().split()]

# A,B = nums()
# P,Q,R = nums()
#
# # Quelques calculs bizarres ici mais je suppose que c'est bon
# d1 = P * B
# pre_runned = (B-A)*Q
# t = B + (d1 - pre_runned) / (R+Q)
# print(t)


# N = num()
# lst = nums()
# # On cherche le nombre de jours où la valeur augmente ?
# res = 0
# for j in range(N):
#     cur = lst[j]
#     if j == 0: continue
#     if cur > lst[j-1]:
#         res += 1
# print(res)

N = num()
members = []
for i in range(N):
    # A priori, juste on stocke l'entrée
    members.append(input())

# Ce pseudo-id là doit revenir combien de fois?
ans = 0
for m in members:
    if m == "E869120":
        ans += 1

print(ans)