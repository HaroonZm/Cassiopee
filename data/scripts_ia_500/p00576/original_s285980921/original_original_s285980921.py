N = int(input())
koma = list(map(int, input().split()))
M = int(input())
order = list(map(int, input().split()))
koma.append(0)

for i in range(M):
    koma[order[i]-1] += 1
    if koma[order[i]-1] == koma[order[i]] or koma[order[i]-1] == 2020:
        koma[order[i]-1] -= 1

del koma[-1]
for v in koma:
    print(v)