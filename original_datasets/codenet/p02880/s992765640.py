N = int(input())
s = list(range(1, 10))

for i in s:
    if N%i == 0 and int(N/i) in s:
        print('Yes')
        break
else:
    print('No')