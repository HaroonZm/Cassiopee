nq = map(int, raw_input().split())
n = nq[0]
q = nq[1]

yn = [[1, 'kogakubu10gokan']]

for i in range(n):
    yn.append(raw_input().split())

yn.append([100,''])

y = 1
k = 0
while y <= q:
    k += 1
    y = int(yn[k][0])

print yn[k-1][1]