n_x = input().strip().split()
n = int(n_x[0])
x = int(n_x[1])

x_list_str = input().strip().split()
x_list = []
for v in x_list_str:
    x_list.append(int(v))

def my_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

current = abs(x - x_list[0])
for i in range(1, n):
    diff = abs(x - x_list[i])
    current = my_gcd(current, diff)

print(current)