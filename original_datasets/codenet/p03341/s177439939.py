N = input()
S = list(input())

length = len(S)
min_num = 300000
left = 0
right = S.count("E")

for i in range(length):

  if i > 0:
    left += int(S[i - 1] == "W")

  if i < length:
    right -= int(S[i] == "E")

  if left + right < min_num:
    min_num = left + right

print(min_num)