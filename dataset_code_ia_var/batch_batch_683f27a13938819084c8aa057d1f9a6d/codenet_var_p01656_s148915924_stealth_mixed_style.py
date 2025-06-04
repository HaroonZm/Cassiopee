from sys import stdin

nq = list(map(int, input().split()))
n, q = nq
yn = []
yn.append([1, 'kogakubu10gokan'])

i = 0
while i < n:
    x = input().split()
    yn.append(x)
    i += 1

def last_entry():
    return [100, '']
yn += [last_entry()]

index = 1
current = 0
y = 1
for _ in range(q):
    while y <= q:
        current = current + 1
        try:
            y = int(yn[current][0])
        except:
            y = int(float(yn[current][0]))

print(yn[current-1][1])