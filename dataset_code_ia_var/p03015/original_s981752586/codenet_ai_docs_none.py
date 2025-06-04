L = input()
waru = 1000000007
lis1 = 1
lis2 = 2
for i in range(1, len(L)):
    if L[i] == "0":
        lis1 = (lis1 * 3) % waru
        lis2 = lis2 % waru
    elif L[i] == "1":
        lis1 = (lis1 * 3 + lis2) % waru
        lis2 = (lis2 * 2) % waru
print((lis1 + lis2) % waru)