w = int(input())
n = int(input())

lines = [i + 1 for i in range(w)]

for _ in range(n):
    a, b = input().split(',')
    a, b = int(a), int(b)
    # swap the numbers under the vertical lines a and b
    lines[a-1], lines[b-1] = lines[b-1], lines[a-1]

for num in lines:
    print(num)