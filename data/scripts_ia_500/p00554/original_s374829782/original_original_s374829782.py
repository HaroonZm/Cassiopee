N , M = map(int , input().split(' '))
A, B = [], []
hit = 0
for i in range(M):
    tmp = input().split(' ')
    A.append(int(tmp[0]))
    B.append(int(tmp[1]))

hit_card = 0
for i in range(M):
    if A[i] >= N:
        hit_card += 1

sorted_A = sorted(A, reverse=True)
need_money = 0

if hit_card < (M - 1):
    need_hit = (M - 1) - hit_card

    for i in range(need_hit):
        need_money += N - sorted_A[i + hit_card]

print(need_money)