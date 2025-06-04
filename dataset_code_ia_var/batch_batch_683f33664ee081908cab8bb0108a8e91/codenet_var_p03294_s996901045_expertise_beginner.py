def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
numbers = list(map(int, input().split()))

current_lcm = numbers[0]
for num in numbers[1:]:
    current_lcm = lcm(current_lcm, num)

answer = 0
for num in numbers:
    answer += (current_lcm - 1) % num

print(answer)