input()
A = set(int(x) for x in input().split())
input()
B = set(int(x) for x in input().split())

for i in sorted((A | B) - (A & B)):
    print(i)