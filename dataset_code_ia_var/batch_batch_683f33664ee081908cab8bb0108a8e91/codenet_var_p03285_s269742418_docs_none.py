a = int(input())
for i in range(25):
    for j in range(15):
        if a - (4 * i + 7 * j) == 0:
            print("Yes")
            exit()
print("No")