N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

max_length = 0

for start in range(N):
    total = 0
    for end in range(start, N):
        total += data[end]
        if total == 0:
            length = end - start + 1
            if length > max_length:
                max_length = length

print(max_length)