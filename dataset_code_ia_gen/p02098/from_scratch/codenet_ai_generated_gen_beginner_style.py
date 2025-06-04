theta1 = int(input())
theta2 = int(input())

diff = (theta2 - theta1) % 360
if diff > 180:
    diff = diff - 360
answer = (theta1 + diff / 2) % 360
print(round(answer, 4))