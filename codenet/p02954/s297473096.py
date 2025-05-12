s = input()
n = len(s)

ans = [0]*n
for i in range(n-1):
    if s[i:i+2] == "RL":
        for j in range(i , -1, -1):
            if s[j] == "R":
                ans[i + (i-j) % 2] += 1
            else:
                break
        for j in range(i+1, n):
            if s[j] == "L":
                ans[i + (j-i) % 2] += 1
            else:
                break
            
print(" ".join(map(str, ans)))