a = 0
b = 0
o = 0
ab = 0

while True:
    try:
        data = input()
        parts = data.split(",")
        blood = parts[1]
        if blood == "A":
            a = a + 1
        elif blood == "B":
            b = b + 1
        elif blood == "O":
            o = o + 1
        elif blood == "AB":
            ab = ab + 1
    except:
        break

print(a)
print(b)
print(ab)
print(o)