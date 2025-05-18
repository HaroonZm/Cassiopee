n = int(input())
li = list(map(int,input().split()))
s = sum(li)
lee = len(li)
kumi = lee//2
tmp = 0
for i in range(1,kumi+1):
    tmp += 2*li[2*(i-1)]
last = s - tmp
#print(last)
first = li[-1]*2-last
ans_li = [first]
for l in li:
    target = ans_li[-1]
    ans_li.append(l*2-target)
ans_li.pop(-1)
print(*ans_li)