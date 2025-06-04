L = [39]
for i in range(1, 39):
    L.append(i)
while True:
    try:
        user_input = input()
        num = int(user_input)
        index = num % 39
        value = L[index]
        print("3C{0:02d}".format(value))
    except:
        break