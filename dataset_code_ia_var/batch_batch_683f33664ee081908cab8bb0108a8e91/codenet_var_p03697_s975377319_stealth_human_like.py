# ok, je vais essayer quelque chose
a, b = input().split()
a = int(a)
b = int(b)
# ça fait la somme ouf
res = a + b
if res > 9:
    print("error")  # trop grand
else:
    print(min(res, 10))  # on doit print le minimum, je crois