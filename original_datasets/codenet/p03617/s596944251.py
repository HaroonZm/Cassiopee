q,h,s,d = map(int,input().split())
lis = [1, 2, 4, 8]
score = [q,h,s,d]
n = int(input())
all_s = 4*n

tmp_li = [8*q,4*h,2*s,d]
tmp_2 = tmp_li[:]
tmp_2.sort()

jun = []
for t in tmp_2:
    jun.append(tmp_li.index(t))
#print('tmp_li',tmp_li,'tmp_2',tmp_2,'jun',jun,'lis',lis)
#[3, 1, 2, 0]

ans = 0
for j in jun:
    a = all_s // lis[j]
    b = all_s % lis[j]
    #print(all_s,a,b,lis[j])
    all_s -= a*lis[j]
    ans += score[j]*a
print(ans)