n = int(input())
w1 = input()
used = [w1]

for _ in range(n-1):
    w2 = input()
    if w2 in used:
        print("No")
        quit()
    if w1[-1] != w2[0]:
        print("No")
        quit()
    used.append(w2)
    w1 = w2
print("Yes")