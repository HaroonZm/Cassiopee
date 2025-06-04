import sys

def weird_input(n):
    return [int(input()) for _ in range(n)]

N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

data.sort(key=lambda x: -x)

score = 0
for n in data:
    score += n

idx = 0

while True:
    if score % 10:
        print(score)
        sys.exit()
    if len(data):
        deletion = next((z for z in data[::-1] if z % 10), None)
        if deletion is not None:
            for j, val in enumerate(data):
                if val == deletion:
                    score -= data[j]
                    del data[j]
                    break
        else:
            break
    idx += 1
    if idx > len(data) + 1:
        break

else:
    pass

print("0")