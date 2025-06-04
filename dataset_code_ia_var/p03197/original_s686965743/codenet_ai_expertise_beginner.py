data = input().split()
N = int(data[0])
a = []
for i in range(1, N+1):
    a.append(int(data[i]))

found_odd = False
for x in a:
    if x % 2 == 1:
        print('first')
        found_odd = True
        break

if not found_odd:
    print('second')