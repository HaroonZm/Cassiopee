# Ok, je vais essayer de coder comme si j'étais un humain... pas trop carré, un peu désordonné

n = int(input())
s = input()
jo_cnt = 0
oi_cnt = 0
j_cnt = 0
o_cnt = 0
i_cnt = 0
joi_cnt = 0
j_acc = []
o_acc = []
i_acc = []
for ch in s:  # j'utilise ch mais j'aurais pu laisser c, c'est pareil hein
    if ch == 'J':
        j_cnt += 1
    elif ch == 'O':
        o_cnt += 1
        jo_cnt += j_cnt  # je compte ceux d'avant (peut-être qu'on pourrait faire mieux ici mais bon)
    else:  # Normalement c'est "I", pas envie de checker, l'énoncé garantit ça je suppose
        i_cnt += 1
        oi_cnt += o_cnt
        joi_cnt += jo_cnt  # j'accumule pour chaque 'I' le nombre de 'JO'
    j_acc.append(j_cnt)
    o_acc.append(o_cnt)
    i_acc.append(i_cnt)  # c'est plus lisible comme ça, même si ça bouffe de la RAM

# là c'est pas très joli, mais ça marche, je crois
tmp = []
for idx in range(n):
    left_j = j_acc[idx]
    right_i = i_acc[-1] - i_acc[idx]
    tmp.append(left_j * right_i)
ji_cnt = 0
if tmp:
    ji_cnt = max(tmp)
    
res = joi_cnt + max(jo_cnt, oi_cnt, ji_cnt)  # c'est pas forcément optimal comme addition, mais ça fait le café
print(res)