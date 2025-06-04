x = input()

if len(x) < 6:
    print("INVALID")
elif x.isalpha():
    print("INVALID")
elif x.islower():
    print("INVALID")
elif x.isupper():
    print("INVALID")
elif x.isdigit():
    print("INVALID")
else:
    print("VALID")