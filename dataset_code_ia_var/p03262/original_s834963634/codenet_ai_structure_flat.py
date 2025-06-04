import fractions

n_x = input().rstrip().split(" ")
n = int(n_x[0])
x = int(n_x[1])

x_list = input().rstrip().split(" ")
for i in range(len(x_list)):
    x_list[i] = int(x_list[i])

current = abs(x - x_list[0])
i = 1
while i < n:
    current = fractions.gcd(current, abs(x - x_list[i]))
    i += 1

print(current)