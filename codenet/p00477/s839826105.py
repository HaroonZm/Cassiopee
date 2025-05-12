import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

sum_4 = a + b + c + d
minutes = int(sum_4 / 60)
seconds = sum_4 % 60

print(minutes)
print(seconds)