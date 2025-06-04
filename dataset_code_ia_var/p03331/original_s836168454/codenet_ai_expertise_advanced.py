n = int(input())
if n % 10 == 0:
    print(10)
else:
    print(sum(map(int, str(n))))