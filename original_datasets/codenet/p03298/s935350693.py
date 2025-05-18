from collections import Counter
from itertools import product

N=int(input())
S=list(input())
S_rev=list(reversed(S[N:])) #右側から読んだ右半分の文字を考える

leftlist=[] #左半分の分け方の組み合わせを格納
rightlist=[] #右半分について同様

for bit in product(range(2),repeat=N):
  #左半分、右半分について赤と青に塗り分ける
  red_left='' 
  blue_left=''
  red_right=''
  blue_right=''
  for j in range(N):
    if bit[j] == 1:
      red_left+=S[j] #bitに1が立っているところを赤に
      blue_right+=S_rev[j]
    else:
      blue_left+=S[j]
      red_right+=S_rev[j]
  leftlist.append("".join(red_left + "|" + blue_left)) #左の塗り方をリストに格納
  rightlist.append("".join(blue_right + "|" + red_right)) #右について同様
left=Counter(leftlist)
right=Counter(rightlist)

answer=0

for key,value in left.items():
  answer+= value * right[key] #同じkey(分け方）に対するredとblueの通りを掛け合わせる
print(answer)