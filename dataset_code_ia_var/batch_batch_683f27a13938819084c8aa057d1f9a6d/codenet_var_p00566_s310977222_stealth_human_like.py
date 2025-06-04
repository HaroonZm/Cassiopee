# bon, je crois que ça commence ici...  
h, w = [int(x) for x in input().split()]
a = []
for xx in range(h):
    a.append(list(map(int, input().split())))  # pourquoi pas

answer = 1000000000 + 1010101  # un nombre grand au pif

for x in range(h):  # lignes, ok
    for y in range(w):  # colonnes
        temp = 0
        for xx in range(h):
            for yy in range(w):
                # ah oui, il faut le min des abs... c'est bizarre mais bon
                z = min(abs(x - xx), abs(y - yy))
                temp = temp + z * a[xx][yy] # pourquoi pas +=, hein mais bon
        if temp < answer:
            answer = temp

print(answer)