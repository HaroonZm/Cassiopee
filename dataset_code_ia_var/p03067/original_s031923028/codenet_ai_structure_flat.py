A, B, C = map(int, input().split())
if (A < C and C < B) or (A > C and C > B):
    print("Yes")
else:
    print("No")