a = input()[-3:]
print(0 if a == "000" else 1000 - int(a))