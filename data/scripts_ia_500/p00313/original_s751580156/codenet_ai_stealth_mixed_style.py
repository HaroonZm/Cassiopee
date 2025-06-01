n = int(input())
V = list(0 for _ in range(n))
for i in [1, 2, 4]:
    e_list = input().split()
    for idx in range(1, len(e_list)):
        V[int(e_list[idx]) - 1] += i
total = 0
for e in V:
    total += (e & 4 > 0) and (e != 5)
print(total)