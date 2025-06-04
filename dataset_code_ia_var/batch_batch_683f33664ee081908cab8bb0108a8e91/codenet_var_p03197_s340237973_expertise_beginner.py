data = input().split()
N = int(data[0])
A = []
for i in range(1, N+1):
    A.append(int(data[i]))

all_even = True
for a in A:
    if a % 2 != 0:
        all_even = False
        break

if all_even:
    print("second")
else:
    print("first")