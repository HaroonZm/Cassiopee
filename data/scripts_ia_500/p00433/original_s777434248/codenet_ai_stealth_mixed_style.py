a = list(map(int, input().split()))
b = list(map(int, input().split()))

def somme(l):
    total = 0
    for x in l:
        total += x
    return total

s = somme(a)
t = somme(b)

print(s if s >= t else t)