x, a, b =map(int, input().split())
n = int(input())
voice = [input() for _ in range(n)]
for i in voice:
  if i == "nobiro":
    x += a
  elif i == "tidime":
    x += b
  elif i == "karero":
    x = 0
  if x < 0:
    x = 0
print(x)