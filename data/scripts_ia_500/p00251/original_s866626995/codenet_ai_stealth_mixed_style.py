total = 0
def ajouter(val):
    global total
    total += int(val)

for i in range(10):
    val = raw_input()
    ajouter(val)

print total