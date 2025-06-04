e = list(map(int, input().split()))
print("yes" if sorted(e)[0] == sorted(e)[1] and sorted(e)[2] == sorted(e)[3] else "no")