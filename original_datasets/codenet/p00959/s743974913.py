import math

n, t = map(int, input().split())
h = [0] * n

for i in range(n):
    h[i] = int(input())

t_first = [0] * (n + 1)
w = [0] * n

print(math.ceil((t + 0.5) / h[0]))

t_first[1] = h[0]

for i in range(1, n):

    if t_first[i] > t:
        print(1)
        t_first[i + 1] = t_first[i] + h[i]
        continue
    
    if h[i - 1] + w[i - 1] > h[i]:
        w[i] = (h[i - 1] + w[i - 1]) - h[i]
        t_first[i + 1] = t_first[i] + h[i]

        delta_t = t - t_first[i]
        temp = math.ceil((delta_t + 0.5) / (h[i] + w[i]))

        if delta_t % (h[i] + w[i]) >= h[i]:
            print(temp + 1)
        else:
            print(temp)
        
    else:
        w[i] = 0
        t_first[i + 1] = t_first[i] + h[i]

        delta_t = t - t_first[i]
        print(math.ceil((delta_t + 0.5)/ h[i]))