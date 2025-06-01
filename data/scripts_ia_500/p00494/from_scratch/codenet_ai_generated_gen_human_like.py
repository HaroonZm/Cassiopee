S = input()

N = len(S)
prefix_J = [0] * (N + 1)
prefix_O = [0] * (N + 1)
prefix_I = [0] * (N + 1)

for i, c in enumerate(S):
    prefix_J[i + 1] = prefix_J[i] + (1 if c == 'J' else 0)
    prefix_O[i + 1] = prefix_O[i] + (1 if c == 'O' else 0)
    prefix_I[i + 1] = prefix_I[i] + (1 if c == 'I' else 0)

def can(k):
    length = 3 * k
    if length == 0:
        return True
    for start in range(N - length + 1):
        end1 = start + k
        end2 = end1 + k
        end3 = end2 + k
        count_J = prefix_J[end1] - prefix_J[start]
        count_O = prefix_O[end2] - prefix_O[end1]
        count_I = prefix_I[end3] - prefix_I[end2]
        if count_J == k and count_O == k and count_I == k:
            return True
    return False

low, high = 0, N // 3
while low < high:
    mid = (low + high + 1) // 2
    if can(mid):
        low = mid
    else:
        high = mid - 1

print(low)