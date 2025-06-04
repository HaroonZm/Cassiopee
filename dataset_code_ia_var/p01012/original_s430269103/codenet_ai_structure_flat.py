m, n, x = [int(i) for i in input().split()]
k, l, y = [int(i) for i in input().split()]
res = 0.5
temp1 = (m**2 + n**2)**x
temp2 = (m + n)**(2*x)
res = res * (1.0 + temp1 / temp2)
res = res * 0.5
temp3 = (k**2 + l**2)**y
temp4 = (k + l)**(2*y)
res = res * (1.0 + temp3 / temp4)
print(res)