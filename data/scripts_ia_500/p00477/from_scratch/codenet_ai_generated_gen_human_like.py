a = int(input())
b = int(input())
c = int(input())
d = int(input())

total_seconds = a + b + c + d
minutes = total_seconds // 60
seconds = total_seconds % 60

print(minutes)
print(seconds)