N = int(input())
word = list(input())
X1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
X2 = ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Y1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
Y2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
x = 0
y = 0
answer = ""
for i in word:
  if i in X1:
    x += 1
  elif i in X2:
    x -= 1
  elif i in Y1:
    y += 1
  elif i in Y2:
    y -= 1
print(abs(x)+abs(y))
if abs(x)+abs(y) > 0:
  if x > 0:
    answer += "A" * x
  elif x < 0:
    answer += "N" * abs(x)
  if y > 0:
    answer += "a" * y
  elif y < 0:
    answer += "n" * abs(y)
  print(answer)