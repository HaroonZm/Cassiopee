word = input().split()
a, b = map(int, input().split())
target = input()
if word[0] == target:
  a -= 1
else:
  b -= 1
print(a,b)