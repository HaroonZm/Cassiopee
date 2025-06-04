n = int(input())
h = [int(x) for x in input().split()]
h.append(0)
ans = 0

# Utilisation de boucle while à la C-style
index = 0
def dec(j):
    # style fonctionnelle (side effect)
    h[j] = (h[j]-1) if h[j]>0 else 0

while True:
    if not any(h): break
    i = 0
    while i < n:
        if h[i]>0:
            if not h[i+1]: ans+=1
        dec(i)
        i+=1

print(ans)