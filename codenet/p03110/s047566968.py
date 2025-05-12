n = int(input())
jpy = 0
btc = 0
for i in range(n):
    x,u = input().split()
    if u == 'JPY':
        jpy += float(x)
    if u == 'BTC':
        btc += float(x)
print(jpy+(btc)*380000)