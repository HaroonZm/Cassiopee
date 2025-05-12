balls = [1,0,0]

while 1:
    try:
        a,b = input().split(',')
        i1 = ord(a) - ord("A")
        i2 = ord(b) - ord("A")
        balls[i1],balls[i2] = balls[i2],balls[i1]
    except:
        break
for i in range(0,3):
    if balls[i]:
        print(chr(i + ord("A")))