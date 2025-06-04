a = []
try:
    while True:
        a.append(int(input()))
except EOFError:
    pass

counts = [0] * 101

for n in a:
    counts[n] += 1

for n in range(len(counts)):
    if counts[n] == max(counts):
        print(n)