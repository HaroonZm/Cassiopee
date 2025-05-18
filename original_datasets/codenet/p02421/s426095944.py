n = int(input())
taro = 0
hana = 0
for _ in range(n):
	taro_c, hana_c = input().split()
	if taro_c > hana_c:
		taro += 3
	elif hana_c > taro_c:
		hana += 3
	else:
		taro += 1
		hana += 1

print(taro, hana)