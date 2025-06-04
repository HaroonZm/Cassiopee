import math

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# franchement, on pourrait faire mieux ici mais bon ça passe
liste = [a, b, c, d, e]
min_num = min(liste)

# j'utilise encore math parce que c'est plus sûr
x = n // min_num
if n % min_num != 0:
    x += 1

# 4 c'est la constante magique ici on dirait bien ^^  
print(x+4)