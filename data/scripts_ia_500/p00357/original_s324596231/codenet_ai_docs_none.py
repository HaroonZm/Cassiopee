n = 0
bounce = []

def IsReachable():
    current = 0
    for i in range(n):
        if current < 10*i:
            return False
        current = max(current, 10*i + bounce[i])
        if current >= 10*n:
            return True
    return False

n = int(input())
for i in range(n):
    bounce.append(int(input()))

if not IsReachable():
    print("no")
else:
    bounce.reverse()
    if IsReachable():
        print("yes")
    else:
        print("no")