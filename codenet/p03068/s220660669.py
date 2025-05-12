N = int(input())
S = input()
K = int(input())
point = S[K-1]
word = ''
for i in range(N):
  if S[i] == point:
    word += S[i]
  else:
    word += '*'
print(word)