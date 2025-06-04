N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()
numbers.reverse()
total = 0
for i in range(K):
    total = total + numbers[i]
print(total)