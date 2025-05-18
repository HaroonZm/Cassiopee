N = int(input())
S = ""
while N > 0:
    N -= 1
    S += chr(ord('a') + N % 26)
    N //= 26
print(S[::-1])