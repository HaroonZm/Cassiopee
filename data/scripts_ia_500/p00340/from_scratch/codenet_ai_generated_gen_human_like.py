sticks = list(map(int, input().split()))
sticks.sort()
if sticks[0] == sticks[1] and sticks[2] == sticks[3]:
    print("yes")
else:
    print("no")