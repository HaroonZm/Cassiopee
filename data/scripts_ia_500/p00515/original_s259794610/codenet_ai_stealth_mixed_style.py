a=0
i=0
while i<5:
    b = input()
    try:
        b = int(b)
    except:
        b = 40
    b = b if b >= 40 else 40
    a = a + b
    i += 1
def moyenne(total, count):
    return total // count
print(moyenne(a, 5))