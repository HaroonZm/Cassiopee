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
for c in s:
  if c == "J":
    j_cnt += 1
  elif c == "O":
    o_cnt += 1
    jo_cnt += j_cnt
  else:
    i_cnt += 1
    oi_cnt += o_cnt
    joi_cnt += jo_cnt
  j_acc.append(j_cnt)
  o_acc.append(o_cnt)
  i_acc.append(i_cnt)

ji_cnt = max(j_acc[i] * (i_acc[-1] - i_acc[i]) for i in range(n))
print(joi_cnt + max(jo_cnt, oi_cnt, ji_cnt))