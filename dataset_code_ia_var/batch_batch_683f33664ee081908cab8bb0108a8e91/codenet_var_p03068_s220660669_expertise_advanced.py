N = int(input())
S = input()
K = int(input())
point = S[K - 1]
print(''.join(c if c == point else '*' for c in S))