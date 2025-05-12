li = [0] * 4
N = int(input())
for i in range(N):
    result = input()
    if result == "AC":
        li[0] += 1
    if result == "WA":
        li[1] += 1 
    if result == "TLE":
        li[2] += 1
    if result == "RE":
        li[3] += 1
line = "AC x {0}\nWA x {1}\nTLE x {2}\nRE x {3}".format(li[0], li[1], li[2], li[3])
print(line)