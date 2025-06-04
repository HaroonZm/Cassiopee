n,m = input().split()
N = int(n)
M = int(m)
w_list = []
v_list = []
for i in range(N):
    w, v = input().split()
    w_list.append(int(w))
    v_list.append(int(v))
w1 = w_list[0]
w1_values = []
w2_values = []
w3_values = []
w4_values = []
for j in range(N):
    if w_list[j] == w1:
        w1_values.append(v_list[j])
    elif w_list[j] == w1 + 1:
        w2_values.append(v_list[j])
    elif w_list[j] == w1 + 2:
        w3_values.append(v_list[j])
    elif w_list[j] == w1 + 3:
        w4_values.append(v_list[j])
w1_values.sort(reverse=True)
w2_values.sort(reverse=True)
w3_values.sort(reverse=True)
w4_values.sort(reverse=True)
sum_v1 = 0
sum_v2 = 0
sum_v3 = 0
sum_v4 = 0
sum_w1_values = [0]
sum_w2_values = [0]
sum_w3_values = [0]
sum_w4_values = [0]
for p in range(len(w1_values)):
    sum_v1 += w1_values[p]
    sum_w1_values.append(sum_v1)
for q in range(len(w2_values)):
    sum_v2 += w2_values[q]
    sum_w2_values.append(sum_v2)
for r in range(len(w3_values)):
    sum_v3 += w3_values[r]
    sum_w3_values.append(sum_v3)
for s in range(len(w4_values)):
    sum_v4 += w4_values[s]
    sum_w4_values.append(sum_v4)
max_value = 0
for w in range(len(sum_w4_values)):
    for x in range(len(sum_w3_values)):
        for y in range(len(sum_w2_values)):
            for z in range(len(sum_w1_values)):
                cnt = w + x + y + z
                weight = w1 * z + (w1 + 1) * y + (w1 + 2) * x + (w1 + 3) * w
                total_value = sum_w1_values[z] + sum_w2_values[y] + sum_w3_values[x] + sum_w4_values[w]
                if cnt <= N and weight <= M and total_value > max_value:
                    max_value = total_value
print(max_value)