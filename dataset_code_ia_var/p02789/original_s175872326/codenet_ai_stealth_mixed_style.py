N, M = (int(x) for x in input().split())

def check(a, b):
    return "Yes" if a == b else "No"

result = None
if N == M:
    result = check(N, M)
else:
    def f(): print("No")
    f()
if result:
    print(result)