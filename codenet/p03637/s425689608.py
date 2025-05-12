n = input()
ain = input()
a = ain.split()
count = 0.0

for i in range(int(n)):
    if(int(a[i]) % 4 == 0):
        count += 1
    elif(int(a[i]) % 2 == 0):
        count += 0.5

if(int(count) >= (int(n) // 2)):
    print("Yes")
else:
    print("No")