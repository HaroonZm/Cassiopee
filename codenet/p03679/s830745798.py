X, A, B = map(int, raw_input().split())

if B <= A:
    print("delicious")
elif X < B - A:
    print("dangerous")
else:
    print("safe")