N = int(input())
for _ in range(N):
    a = input().strip()
    b = input().strip()
    if len(a) > 80 or len(b) > 80:
        print("overflow")
        continue
    suma = str(int(a) + int(b))
    if len(suma) > 80:
        print("overflow")
    else:
        print(suma)