import sys

n,k = map(int, input().split( ))
a = list(map(int, input().split( )))
tmp = max(a)
tmp2 = max(tmp,n,k)+1
chk = [0]*(tmp2)

for i in range(n):
    chk[a[i]] += 1

if 0 in chk[1:k+1]:
    print(0)
    sys.exit()

right = n-1
left = 0
L = []

while right < n:
    while chk[a[right]] > 1 or a[right] > k:
        chk[a[right]] -= 1
        right -= 1
        
    ln = right - left + 1
    L.append(ln)
    
    while chk[a[left]] > 1 or a[left] > k:
        chk[a[left]] -= 1
        left += 1
    ln = right - left + 1
    L.append(ln)
    chk[a[left]] -= 1
    left += 1
    while chk[a[left-1]] == 0:
        right += 1
        if right >= n:
            break
        chk[a[right]] += 1
    ln = right -left +1
    L.append(ln)
print(min(L))