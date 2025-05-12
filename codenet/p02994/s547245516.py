import math
n, l = map(int,input().split())
#print(n, l)

all_taste = 0
#全てのりんごを使った時の味
for i in range(1, n+1):
    #print(i)
    tmp = l + i - 1
    all_taste = all_taste + tmp

#print(all_taste)
act_taste = 0

#食べるりんご（味がいちばん低いもの）を求める
eat_apple = l + 1 - 1
for i in range(1, n+1):
    cmp_apple = l + i - 1
    #print(eat_apple, cmp_apple)
    if abs(cmp_apple) <= abs(eat_apple):
        eat_apple = cmp_apple
        act_taste = all_taste - eat_apple

#print(eat_apple)
print(act_taste)