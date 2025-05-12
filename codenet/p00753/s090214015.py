# 123456 * 2 以下の素数を列挙
MAX = 123456 * 2
prime = [True] * (MAX+1)
count = [0] * (MAX+1)
tmp = 0
prime[0] = False
prime[1] = False
for i in range(2, MAX+1):
    if prime[i]:
        tmp += 1
        for j in range(i * 2, MAX+1, i):
            prime[j] = False
    count[i] = tmp

# 個数出力
while True:
    n = int(input())
    if n == 0:
        break
    print(count[n * 2] - count[n])