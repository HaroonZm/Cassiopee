Ss = input().rstrip()

Ts = ['Sunny', 'Cloudy', 'Rainy']

for i in range(3):
    if Ts[i] == Ss:
        print(Ts[(i+1)%3])