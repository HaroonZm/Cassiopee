import heapq

num_sushi, chose_num = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(num_sushi)]
data.sort(key=lambda x: -x[1])
delicious_heap = []
count_d = 0
count_n = 0
neta_data = [0] * (num_sushi + 1)
i = 0
while i < chose_num:
    neta, oishisa = data[i]
    if neta_data[neta]:
        heapq.heappush(delicious_heap, oishisa)
    else:
        neta_data[neta] = 1
        count_n += 1
    count_d += oishisa
    i += 1
ans = count_d + count_n ** 2
j = chose_num
while j < num_sushi:
    if not delicious_heap:
        break
    neta, oishisa = data[j]
    if neta_data[neta]:
        j += 1
        continue
    neta_data[neta] = 1
    count_n += 1
    pop_oishisa = heapq.heappop(delicious_heap)
    count_d += oishisa - pop_oishisa
    ans = max(ans, count_d + count_n ** 2)
    j += 1
print(ans)