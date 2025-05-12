n = int(input())
li_a = list(map(int, input().split()))

li_aw = [0] + li_a + [0]

# 全ルートを回るコスト
total_cost = 0
for i in range(1, len(li_aw)):
    total_cost += abs(li_aw[i - 1] - li_aw[i])

for i in range(n):
    # li_aw上の取りやめポイントindex
    delete_index = i + 1
    delete_cost = abs(li_aw[delete_index - 1] - li_aw[delete_index]) + abs(li_aw[delete_index] - li_aw[delete_index + 1])
    add_cost = abs(li_aw[delete_index - 1] - li_aw[delete_index + 1])
    print(total_cost - delete_cost + add_cost)