n_x = input().split()
n = int(n_x[0])
x = int(n_x[1])
pos = input().split()
positions = []
for i in pos:
    positions.append(int(i))
positions.append(x)
for i in range(len(positions)):
    positions[i] = positions[i] - x

differences = []
positions.sort()
for i in range(1, len(positions)):
    differences.append(abs(positions[i] - positions[i-1]))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result

print(gcd_list(differences))