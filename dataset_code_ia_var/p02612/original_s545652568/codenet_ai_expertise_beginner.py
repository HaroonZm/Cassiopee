a = input()
a = a[-3:]
if a == "000":
    print(0)
else:
    print(1000 - int(a))