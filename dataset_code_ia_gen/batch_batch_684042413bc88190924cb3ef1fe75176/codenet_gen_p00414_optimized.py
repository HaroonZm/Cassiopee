L, N = map(int, input().split())
snake = input()

initial_len = L
initial_pairs = sum(1 for i in range(L-1) if snake[i] == 'o' and snake[i+1] == 'o')

# length recurrence: length_{n+1} = length_n + pairs_n * 3
# pairs_n+1 = pairs_n * 4 + length_n - 2 * pairs_n = length_n + 2 * pairs_n

# Define variables for iteration:
length = initial_len
pairs = initial_pairs

for _ in range(N):
    length, pairs = length + pairs * 3, length + 2 * pairs

print(length)