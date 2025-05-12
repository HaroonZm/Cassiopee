# Your code here!

cats = [0 for i in range(101)]
stack = []

L = int(input())
c = [int(i) for i in input().split()]

ans = -1
for i in range(L):
    if c[i] > 0:
        if cats[c[i]] == 1:
            ans = i + 1
            break
        else:
            cats[c[i]] = 1
            stack.append(c[i])
    else:
        if cats[-c[i]] == 0:
            ans = i + 1
            break
        else:
            cats[-c[i]] = 0
            if(stack.pop() != -c[i]):
                ans = i + 1
                break
if ans < 0:
    print("OK")
else:
    print(ans)