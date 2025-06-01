n,q,s,t = map(int,input().split())
a_lst = []
for _ in range(n+1):
    a_lst.append(int(input()))
diff = list(map(lambda i: a_lst[i+1]-a_lst[i], range(n)))
temp = 0
for d in diff:
    temp += (-s * d if d > 0 else -t * d)
def score(d):
    if d > 0:
        return -s * d
    return -t * d
for __ in range(q):
    l,r,x = map(int,input().split())
    old_val_l = diff[l-1]
    diff[l-1] += x
    temp += score(diff[l-1]) - score(old_val_l)
    if r < n:
        old_val_r = diff[r]
        diff[r] -= x
        temp += score(diff[r]) - score(old_val_r)
    print(temp)