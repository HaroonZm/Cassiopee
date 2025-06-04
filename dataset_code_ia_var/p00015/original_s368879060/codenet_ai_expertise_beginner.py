n = raw_input()
n = int(n)
k = 0
while k < n:
    a = raw_input()
    b = raw_input()
    somme = int(a) + int(b)
    if len(str(somme)) > 80:
        somme = "overflow"
    print somme
    k = k + 1