A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

time = 0
temp = A

if temp < 0:
    time += C * abs(temp)  # from temp to 0
    time += D  # thaw at 0
    temp = 0

time += (B - temp) * E

print(time)