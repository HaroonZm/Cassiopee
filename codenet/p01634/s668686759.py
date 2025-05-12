x=input()

if len(x)<6 or x.isalpha() or x.islower() or x.isupper() or x.isdigit():
    print("INVALID")
else:
    print("VALID")