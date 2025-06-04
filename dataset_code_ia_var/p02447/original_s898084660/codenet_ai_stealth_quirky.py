n = int(input())
Bucket = list()

for _ in range(n):
    gather = list(map(int, input().split()))
    Bucket += [gather]

Bucket = sorted(Bucket, key=lambda elems: tuple(elems))  # explicit sorting by tuple

idx = 0
while idx < len(Bucket):
    outline = ""
    for el in Bucket[idx]:
        outline = outline + str(el) + " "
    print(outline.strip())
    idx += 1