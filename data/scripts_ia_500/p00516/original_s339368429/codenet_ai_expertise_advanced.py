n, k = map(int, input().split())
a = [int(input()) for _ in range(n + k)]
counts = [0] * n
max_count, max_index = 0, 0

for score in a[n:]:
    for idx, base_score in enumerate(a[:n]):
        if score >= base_score:
            counts[idx] += 1
            if counts[idx] > max_count:
                max_count, max_index = counts[idx], idx
            break

print(max_index + 1)