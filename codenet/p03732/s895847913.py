n,m=input().split()
N = int(n)
M = int(m)
w_list = []
v_list = []
w1_values = []
w2_values = []
w3_values = []
w4_values = []
sum_w1_values = []
sum_w2_values = []
sum_w3_values = []
sum_w4_values = []
sum_v1 = 0
sum_v2 = 0
sum_v3 = 0
sum_v4 = 0

for i in range(N):
	w,v = input().split()
	w = int(w)
	v = int(v)
	w_list.append(w)
	v_list.append(v)

w1 = w_list[0]
for j in range(N):
	if(w_list[j] == w1):
		w1_values.append(v_list[j])

	elif(w_list[j] == w1+1):
		w2_values.append(v_list[j])

	elif(w_list[j] == w1+2):
		w3_values.append(v_list[j])

	elif(w_list[j] == w1+3):
		w4_values.append(v_list[j])

w1_values.sort()
w1_values.reverse()
w2_values.sort()
w2_values.reverse()
w3_values.sort()
w3_values.reverse()
w4_values.sort()
w4_values.reverse()

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

sum_w1_values.insert(0,0)
sum_w2_values.insert(0,0)
sum_w3_values.insert(0,0)
sum_w4_values.insert(0,0)

max_value = 0
count = 0
for w in range(len(sum_w4_values)):
	for x in range(len(sum_w3_values)):
		for y in range(len(sum_w2_values)):
			for z in range(len(sum_w1_values)):
				count = w+x+y+z
				weight = (w1)*z + (w1+1)*y +(w1+2)*x + (w1+3)*w
				if(count<=N and weight<=M and max_value<(sum_w1_values[z] + sum_w2_values[y] + sum_w3_values[x] + sum_w4_values[w])):
					max_value = sum_w1_values[z] + sum_w2_values[y] + sum_w3_values[x] + sum_w4_values[w]

print(max_value)