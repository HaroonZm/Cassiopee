import fractions

(n,x) = map(int, input().rstrip().split(" "))

x_list = list(map(int, input().rstrip().split(" ")))

current = abs(x-x_list[0])
for i in range(1,n):
    current = fractions.gcd(current, abs(x-x_list[i]))

print(current)