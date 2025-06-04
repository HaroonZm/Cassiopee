h, w, x, y = map(int, input().split())

somme = x + y
produit = h * w

if produit % 2 == 0:
    print("Yes")
else:
    if somme % 2 == 0:
        print("Yes")
    else:
        print("No")